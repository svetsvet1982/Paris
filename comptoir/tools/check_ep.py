# -*- coding: utf-8 -*-
"""Usage: python3 -I check_ep.py <module_name>   (run from comptoir/tools/part1)"""
import sys, re, importlib
sys.path.insert(0, ".")
from collections import Counter
d = importlib.import_module(sys.argv[1]); M = d.META
turns = [x for x in d.D if x[0]]
cnt = Counter(x[0] for x in turns)
ok = True
def bad(m):
    global ok; ok = False; print("ERROR:", m)
if len(turns) != 120: bad(f"turns={len(turns)} (need 120)")
if not 2 <= len(cnt) <= 4: bad(f"speakers={dict(cnt)}")
for s,f,k in d.D:
    if not f.strip() or not k.strip(): bad(f"empty fr/ko: {s} {f[:30]}")
    if s and re.match(r"^\s*\d+\s*[.)]", f): bad("turn numbered: "+f[:30])
long = [(s,f) for s,f,k in turns if max(len(re.findall(r"\S+", x)) for x in re.split(r"[.!?…]+", f) if x.strip() or True) > 20]
print("speakers:", dict(cnt)); print("long-sentence (>20 words) turns:", len(long))
for s,f in long[:8]: print("  ", s, f[:90])
sl = sum(1 for s,f,k in turns if re.search(r"\[속어\]", f)); 
print("vocab:", len(d.VOCAB), "gram:", len(d.GRAM), "read:", len(d.READ), "culture:", len(d.CULTURE))
lv = Counter(v[0] for v in d.VOCAB); print("vocab levels:", dict(lv))
if len(d.VOCAB) < 18: bad("need >=18 VOCAB")
if len(d.GRAM) < 5: bad("need >=5 GRAM")
if len(d.READ) < 5: bad("need >=5 READ")
for v in d.VOCAB:
    if v[0] not in ("A2","B1","B2","C1"): bad("bad level "+str(v[0]))
print("OK" if ok else "FAILED")
sys.exit(0 if ok else 1)
