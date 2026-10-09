#!/usr/bin/env python3
"""Check each episode file: exactly turns 1..100, required sections present."""
import re, sys, glob
bad = 0
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "partie*/p*e*.md")):
    t = open(f, encoding="utf-8").read()
    dial = t.split("## Dialogue", 1)[-1].split("\n## 해설", 1)[0]
    nums = [int(m.group(1)) for m in re.finditer(r"^\*\*(\d+)\.\s", dial, re.M)]
    probs = []
    if nums != list(range(1, 101)): probs.append(f"turns={len(nums)} (not 1..100)")
    for s in ["① 구절 번역", "② 구절 해설", "③ 사용 맥락 분석", "④", "⑤"]:
        if s not in t: probs.append(f"missing {s}")
    if "오늘의 인용" not in t: probs.append("missing quote header")
    print(("FAIL " if probs else "ok   ") + f, "; ".join(probs)); bad += bool(probs)
sys.exit(1 if bad else 0)
