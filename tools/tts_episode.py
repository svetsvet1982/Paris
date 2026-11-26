# -*- coding: utf-8 -*-
"""에피소드 프랑스어 대화문 → MP3 (Microsoft Edge 온라인 Neural 음성).

대화문(화자가 있는 줄)만 읽고, 지문(speaker None)·한글 해석·분석은 제외한다.
화자별로 다른 목소리를 쓰고, 턴 사이에 짧은 무음을 넣어 하나의 MP3로 합친다.

사용법:
    python tools/tts_episode.py 1            # ep01 → part1/ep01_<제목>.mp3
    python tools/tts_episode.py 1 5 12       # 여러 화
    python tools/tts_episode.py 1 -o out.mp3 # 출력 경로 지정 (한 화일 때)
    python tools/tts_episode.py 1 --rate -10%   # 전체 속도 조절 (학습용으로 느리게)
    python tools/tts_episode.py --pdf vendanges.pdf 1 -o out.mp3
        # 데이터 파일이 없는 PDF(예: « Le Phare » 시리즈)에서 N화 대화문을 직접 추출

필요: pip install edge-tts, ffmpeg
"""
import argparse, asyncio, importlib.util, os, re, shutil, subprocess, sys, tempfile, unicodedata
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent

# 주요 인물 고정 음성 (voice, rate, pitch)
VOICES = {
    "Léa":     ("fr-FR-DeniseNeural", "+0%", "+0Hz"),
    "Antoine": ("fr-FR-HenriNeural", "+0%", "+0Hz"),
    "Gaston":  ("fr-FR-RemyMultilingualNeural", "-5%", "-6Hz"),
    "Margaux": ("fr-FR-EloiseNeural", "+0%", "+0Hz"),
}
# « Le Phare » 시리즈 (PDF 입력 시)
PHARE_VOICES = {
    "Léa":     ("fr-FR-DeniseNeural", "+0%", "+0Hz"),
    "Julien":  ("fr-FR-HenriNeural", "+0%", "+0Hz"),
    "Karim":   ("fr-FR-RemyMultilingualNeural", "+0%", "+0Hz"),
    "Hélène":  ("fr-CH-ArianeNeural", "+0%", "+0Hz"),
    "Camille": ("fr-FR-VivienneMultilingualNeural", "+0%", "+0Hz"),
    "Aubry":   ("fr-CH-FabriceNeural", "-8%", "-6Hz"),
    "Serveur": ("fr-BE-GerardNeural", "+0%", "+0Hz"),
    "Sophie":  ("fr-BE-CharlineNeural", "+0%", "+0Hz"),
}
FEMALE_POOL = ["fr-FR-VivienneMultilingualNeural", "fr-CH-ArianeNeural", "fr-BE-CharlineNeural", "fr-CA-SylvieNeural"]
MALE_POOL = ["fr-BE-GerardNeural", "fr-CH-FabriceNeural", "fr-CA-JeanNeural", "fr-CA-ThierryNeural"]
FEMALE_HINT = re.compile(r"^(Mme|Madame|La |Une |L'apicultrice|Mère|Directrice|Guichetière|Caissière)"
                         r"|(Nicole|Anne|Aya|Margaux|Nathalie|Yasmine|Sophie)", re.I)

GAP_SEC = 0.6        # 턴 사이 무음
CONCURRENCY = 6
RETRIES = 4


def load_episode(ep: int):
    part = (ep - 1) // 12 + 1
    path = ROOT / "tools" / f"part{part}" / f"ep{ep:02d}_data.py"
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return part, mod


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


SPEAKER_RE = re.compile(r"^([A-ZÀ-Ý][A-Za-zÀ-ÿ' .-]{0,25}):\s*(.*)$")
HANGUL = re.compile(r"[\uac00-\ud7a3]")


def load_pdf_episode(pdf: Path, ep: int):
    """PDF에서 N화의 (화자, 프랑스어) 대화만 추출.
    형식: 'Speaker: 프랑스어' (줄바꿈 시 다음 줄이 왼쪽 정렬로 이어짐), 한글 해석은 들여쓰기.
    괄호 지문 (en entrant) 등은 제거한다."""
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True,
                         capture_output=True, text=True).stdout.splitlines()
    head = re.compile(r"^\s*\d+\s*부\s*(\d+)\s*화\.\s*(.*)$")
    title, turns, on = None, [], False
    for line in txt:
        m = head.match(line)
        if m:
            if on:
                break
            if int(m.group(1)) == ep:
                on, title = True, m.group(2).strip()
            continue
        if not on:
            continue
        if line.startswith("📚"):
            break
        if not line.strip() or line[0].isspace() or HANGUL.search(line):
            continue                     # 한글 해석·머리말·쪽 번호
        m = SPEAKER_RE.match(line)
        if m:
            turns.append([m.group(1).strip(), m.group(2)])
        elif turns and not line.startswith(("수준:", "핵심 표현:")):
            turns[-1][1] += " " + line.strip()
    if not turns:
        sys.exit(f"{pdf}: {ep}화를 찾지 못했습니다.")
    out = []
    for sp, fr in turns:
        fr = re.sub(r"\([^)]*\)", " ", fr)
        fr = clean_text(fr)
        if re.search(r"[A-Za-zÀ-ÿ]", fr):
            out.append((sp, fr))
    return title, out


def assign_voices(speakers, fixed=None):
    fixed = fixed or VOICES
    out, fi, mi = {}, 0, 0
    for sp in speakers:
        if sp in fixed:
            out[sp] = fixed[sp]
        elif FEMALE_HINT.search(sp):
            out[sp] = (FEMALE_POOL[fi % len(FEMALE_POOL)], "+0%", "+0Hz"); fi += 1
        else:
            out[sp] = (MALE_POOL[mi % len(MALE_POOL)], "+0%", "+0Hz"); mi += 1
    return out


def clean_text(t: str) -> str:
    t = t.replace("« ", "“").replace(" »", "”").replace("«", "“").replace("»", "”")
    return re.sub(r"\s+", " ", t).strip()


async def synth(i, text, voice, rate, pitch, dst, sem, proxy):
    err = None
    async with sem:
        for attempt in range(RETRIES):
            try:
                await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, proxy=proxy).save(str(dst))
                if dst.stat().st_size > 0:
                    return
            except Exception as e:  # 네트워크 일시 오류 재시도
                err = e
            await asyncio.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"turn {i}: TTS 실패 ({voice}): {err or 'empty audio'}")


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


async def build(ep: int, out: Path | None, global_rate: str | None, pdf: Path | None = None):
    if pdf:
        title, turns = load_pdf_episode(pdf, ep)
        title_fr = re.sub(r"\s*\([^)]*\)\s*$", "", title)
        voices = assign_voices(dict.fromkeys(sp for sp, _ in turns), PHARE_VOICES)
        album = "Le Phare"
        if out is None:
            out = Path.cwd() / f"ep{ep:02d}_{slug(title_fr)}.mp3"
    else:
        part, mod = load_episode(ep)
        turns = [(sp, clean_text(fr)) for sp, fr, _ko in mod.D if sp]   # 대화문만
        voices = assign_voices(dict.fromkeys(sp for sp, _ in turns))
        title_fr, album = mod.META["title_fr"], "La Cave des Abbesses"
        if out is None:
            out = ROOT / f"part{part}" / f"ep{ep:02d}_{slug(title_fr)}.mp3"
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")

    tmp = Path(tempfile.mkdtemp(prefix=f"tts_ep{ep:02d}_"))
    try:
        sem = asyncio.Semaphore(CONCURRENCY)
        jobs = []
        for i, (sp, text) in enumerate(turns):
            v, r, p = voices[sp]
            jobs.append(synth(i, text, v, global_rate or r, p, tmp / f"{i:03d}.mp3", sem, proxy))
        await asyncio.gather(*jobs)

        # 모두 24kHz mono WAV로 맞춘 뒤 무음을 끼워 연결 → MP3
        silence = tmp / "gap.wav"
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(GAP_SEC), silence])
        lst = tmp / "list.txt"
        with lst.open("w") as f:
            for i in range(len(turns)):
                w = tmp / f"{i:03d}.wav"
                run(["ffmpeg", "-y", "-i", tmp / f"{i:03d}.mp3", "-ar", "24000", "-ac", "1", w])
                f.write(f"file '{w}'\nfile '{silence}'\n")
        out.parent.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
             "-ar", "24000", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "64k",
             "-metadata", f"title=Épisode {ep} · {title_fr}",
             "-metadata", f"album={album}", "-metadata", f"track={ep}", out])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"ep{ep:02d}: {len(turns)} turns → {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    for sp, (v, *_ ) in voices.items():
        print(f"   {sp:<14} {v}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("episodes", nargs="+", type=int)
    ap.add_argument("-o", "--out", type=Path)
    ap.add_argument("--pdf", type=Path, help="데이터 파일 대신 PDF에서 대화문 추출")
    ap.add_argument("--rate", help="모든 화자 속도 덮어쓰기, 예: -10%%")
    a = ap.parse_args()
    if a.out and len(a.episodes) > 1:
        sys.exit("-o 는 한 화만 지정할 때 사용하세요.")
    for ep in a.episodes:
        asyncio.run(build(ep, a.out, a.rate, a.pdf))


if __name__ == "__main__":
    main()
