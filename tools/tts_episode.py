# -*- coding: utf-8 -*-
"""에피소드 프랑스어 대화문 → MP3 (Microsoft Edge 온라인 Neural 음성).

대화문(화자가 있는 줄)만 읽고, 지문(speaker None)·한글 해석·분석은 제외한다.
화자별로 다른 목소리를 쓰고, 턴 사이에 짧은 무음을 넣어 하나의 MP3로 합친다.

사용법:
    python tools/tts_episode.py 1            # ep01 → part1/ep01_<제목>.mp3
    python tools/tts_episode.py 1 5 12       # 여러 화
    python tools/tts_episode.py 1 -o out.mp3 # 출력 경로 지정 (한 화일 때)
    python tools/tts_episode.py 1 --rate -10%   # 전체 속도 조절 (학습용으로 느리게)

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
FEMALE_POOL = ["fr-FR-VivienneMultilingualNeural", "fr-CH-ArianeNeural", "fr-BE-CharlineNeural", "fr-CA-SylvieNeural"]
MALE_POOL = ["fr-BE-GerardNeural", "fr-CH-FabriceNeural", "fr-CA-JeanNeural", "fr-CA-ThierryNeural"]
FEMALE_HINT = re.compile(r"^(Mme|Madame|La |Une |L'apicultrice)|(Nicole|Anne|Aya|Margaux)", re.I)

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


def assign_voices(speakers):
    out, fi, mi = {}, 0, 0
    for sp in speakers:
        if sp in VOICES:
            out[sp] = VOICES[sp]
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


async def build(ep: int, out: Path | None, global_rate: str | None):
    part, mod = load_episode(ep)
    turns = [(sp, clean_text(fr)) for sp, fr, _ko in mod.D if sp]   # 대화문만
    voices = assign_voices(dict.fromkeys(sp for sp, _ in turns))
    if out is None:
        out = ROOT / f"part{part}" / f"ep{ep:02d}_{slug(mod.META['title_fr'])}.mp3"
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
             "-metadata", f"title=Épisode {ep} · {mod.META['title_fr']}",
             "-metadata", "album=La Cave des Abbesses", "-metadata", f"track={ep}", out])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"ep{ep:02d}: {len(turns)} turns → {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    for sp, (v, *_ ) in voices.items():
        print(f"   {sp:<14} {v}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("episodes", nargs="+", type=int)
    ap.add_argument("-o", "--out", type=Path)
    ap.add_argument("--rate", help="모든 화자 속도 덮어쓰기, 예: -10%%")
    a = ap.parse_args()
    if a.out and len(a.episodes) > 1:
        sys.exit("-o 는 한 화만 지정할 때 사용하세요.")
    for ep in a.episodes:
        asyncio.run(build(ep, a.out, a.rate))


if __name__ == "__main__":
    main()
