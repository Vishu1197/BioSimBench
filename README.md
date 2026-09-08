# BioSimBench

**Lightweight GROMACS simulation quality-control and reporting tool.**

BioSimBench inspects a GROMACS simulation directory, checks expected files, reads basic `.mdp` and `.log` metadata, detects obvious fatal termination patterns, and produces a human-readable HTML QC report.

> MVP v0.1 — intentionally conservative. A PASS means a structural/file-level check passed; it does **not** prove scientific convergence or simulation validity.

## Features

- GROMACS file inventory (`.tpr`, `.gro`, `.top`, `.xtc`, `.edr`, `.log`, `.mdp`)
- Basic `.mdp` metadata extraction
- Run-completion / fatal-log checks
- Simple QC summary
- Standalone HTML report
- Python CLI

## Install

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -e .
```

## Usage

```bash
biosimbench path/to/md_run --html report.html
```

Or without installation:

```bash
python -m biosimbench.cli path/to/md_run
```

## Roadmap

- Parse `gmx energy` output for temperature, pressure, potential and total energy
- Automated RMSD/RMSF/Rg analysis through GROMACS commands
- Trajectory integrity checks
- Publication-quality plots
- JSON output/API
- Interactive dashboard

The planned analyses map directly to standard GROMACS analysis programs such as `gmx rms`, `gmx rmsf`, and `gmx gyrate`. citeturn0search12

## License

MIT
