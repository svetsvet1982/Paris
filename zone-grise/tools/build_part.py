# Usage (from zone-grise/): python3 tools/build_part.py 2 13 18
import sys, re, subprocess, unicodedata, importlib, os, glob
sys.path.insert(0, os.getcwd())
part, a, b = map(int, sys.argv[1:4])
os.makedirs(f"part{part}", exist_ok=True)
for n in range(a, b + 1):
    mod = f"tools.part{part}.ep{n:02d}_data"
    if not os.path.exists(f"tools/part{part}/ep{n:02d}_data.py"):
        print(f"ep{n}: missing"); continue
    d = importlib.import_module(mod)
    t = unicodedata.normalize('NFKD', d.META['title_fr']).encode('ascii', 'ignore').decode()
    t = re.sub(r"[^A-Za-z0-9]+", "_", t).strip('_')
    for old in glob.glob(f"part{part}/ep{n:02d}_*"): os.remove(old)
    out = f"part{part}/ep{n:02d}_{t}.docx"
    r = subprocess.run(["python3", "tools/build_ep.py", out, mod], capture_output=True, text=True)
    if r.returncode: print(out, "FAILED", r.stderr[-400:]); continue
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", f"part{part}", out], capture_output=True)
    print(out, "OK")
