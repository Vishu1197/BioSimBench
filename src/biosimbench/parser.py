from pathlib import Path
import re

REQUIRED = {".tpr": "Run input", ".gro": "Structure", ".top": "Topology"}
OPTIONAL = {".xtc": "Trajectory", ".trr": "Full trajectory", ".edr": "Energy", ".log": "Log", ".mdp": "Parameters"}

def inspect_directory(path):
    p = Path(path)
    files = {f.suffix.lower(): f for f in p.iterdir() if f.is_file()}
    checks = []
    for ext, label in REQUIRED.items():
        ok = ext in files
        checks.append({"name": label, "status": "PASS" if ok else "WARN", "detail": files[ext].name if ok else f"Missing {ext}"})
    for ext, label in OPTIONAL.items():
        if ext in files:
            checks.append({"name": label, "status": "PASS", "detail": files[ext].name})
    return files, checks

def parse_mdp(path):
    result = {}
    if not path or not path.exists(): return result
    for line in path.read_text(errors="ignore").splitlines():
        line=line.split(';',1)[0].strip()
        if '=' in line:
            k,v=line.split('=',1); result[k.strip()]=v.strip()
    return result

def parse_log(path):
    text = path.read_text(errors="ignore") if path and path.exists() else ""
    completed = bool(re.search(r'Finished mdrun|Finished mdrun on|Writing final coordinates', text, re.I))
    return {"completed": completed, "has_fatal": bool(re.search(r'Fatal error|SIGTERM|Segmentation fault', text, re.I))}
