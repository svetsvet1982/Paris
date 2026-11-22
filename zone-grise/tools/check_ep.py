# -*- coding: utf-8 -*-
"""Usage (from zone-grise/): python3 tools/check_ep.py tools.part1.ep02_data"""
import sys, os, importlib, re
sys.path.insert(0, os.getcwd())
d = importlib.import_module(sys.argv[1])
turns = [x for x in d.D if x[0]]
n = len(turns)
wc = [len(re.findall(r"[\wÀ-ÿ'-]+", f)) for _, f, _ in turns]
short = [f for (_, f, _), w in zip(turns, wc) if w <= 8]
tiny = [f for (_, f, _), w in zip(turns, wc) if w <= 3]
from collections import Counter
print(f"turns={n} (need 120-150)  avg_words={sum(wc)/n:.1f}  short<=8: {len(short)} ({100*len(short)/n:.0f}%, need <=10%)  tiny<=3: {len(tiny)} (need 0)")
print("speakers:", dict(Counter(s for s, _, _ in turns)))
print(f"VOCAB={len(d.VOCAB)} (20-25)  GRAM={len(d.GRAM)} (6-8)  CULTURE={len(d.CULTURE)} (1-2)")
bad = [v for v in d.VOCAB if v[0] not in ("B1","B2","C1","JARGON")]
assert not bad, bad
assert all(len(x) == 3 and x[1] and x[2] for x in d.D), "every D entry needs (speaker, fr, ko) non-empty"
for k in ("part","ep","part_label","title_fr","title_ko","place","chars","situation","focus","jargon","levelmix","next"):
    assert k in d.META, k
for f in tiny: print("  TINY:", f)
for f in short: print("  short:", f)
ok = 120 <= n <= 150 and not tiny and len(short) <= 0.10*n and 20 <= len(d.VOCAB) <= 25 and 6 <= len(d.GRAM) <= 8
print("RESULT:", "OK" if ok else "FIX NEEDED")
