import argparse
from pathlib import Path
from .parser import inspect_directory, parse_mdp, parse_log
from .qc import summary
from .report import render_html

def main():
    ap=argparse.ArgumentParser(description="BioSimBench: GROMACS simulation QC")
    ap.add_argument("directory", help="GROMACS simulation directory")
    ap.add_argument("--html", default="biosimbench_report.html", help="HTML report path")
    args=ap.parse_args(); p=Path(args.directory)
    if not p.is_dir(): ap.error(f"Not a directory: {p}")
    files, checks=inspect_directory(p)
    mdp=parse_mdp(files.get('.mdp')); log=parse_log(files.get('.log'))
    if '.log' in files:
        checks.append({"name":"Run completion","status":"PASS" if log['completed'] and not log['has_fatal'] else "WARN","detail":"Completed marker detected" if log['completed'] else "Completion marker not detected"})
        if log['has_fatal']: checks.append({"name":"Fatal errors","status":"FAIL","detail":"Fatal error/termination pattern detected in log"})
    metadata={"integrator":mdp.get("integrator"),"dt_ps":mdp.get("dt"),"nsteps":mdp.get("nsteps"),"estimated_time_ps":(float(mdp['dt'])*int(mdp['nsteps']) if mdp.get('dt') and mdp.get('nsteps') and mdp['dt'].replace('.','',1).isdigit() and mdp['nsteps'].isdigit() else None)}
    s=summary(checks)
    print(f"BioSimBench | Overall: {s['overall']} | PASS {s['pass']} | WARN {s['warn']} | FAIL {s['fail']}")
    for c in checks: print(f"[{c['status']}] {c['name']}: {c['detail']}")
    render_html(args.html,"BioSimBench Report",checks,s,metadata)
    print(f"Report written to: {args.html}")

if __name__ == '__main__': main()
