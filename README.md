# 🧬 BioSimBench

### 🔬 Lightweight GROMACS Simulation Quality-Control & Reporting Tool

**BioSimBench** is a lightweight Python-based tool designed to inspect **GROMACS molecular-dynamics simulation directories**, perform structural and metadata-level quality checks, and generate a clean, human-readable **HTML quality-control report**.

> ⚠️ **MVP v0.1 — Conservative by Design**
> A `PASS` indicates that a structural/file-level check passed. It **does not** establish scientific convergence, trajectory quality, force-field validity, or biological correctness.

---

## 🚀 Why BioSimBench?

Molecular-dynamics simulations can generate a large collection of files and parameters:

```text
.tpr   .gro   .top   .mdp   .xtc   .edr   .log
```

Before performing downstream analysis, researchers often need to answer simple but important questions:

* 📁 Are the expected simulation files present?
* ⚙️ What parameters were used?
* ⏱️ How long was the simulation configured to run?
* ✅ Did the simulation terminate normally?
* 🚨 Does the log contain obvious fatal-error patterns?
* 📊 Can the simulation be summarized in a readable report?

**BioSimBench aims to automate these initial checks.**

---

# ✨ Features

| Feature                    | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| 📁 **File Inventory**      | Detects common GROMACS simulation files                  |
| ⚙️ **MDP Parser**          | Extracts basic simulation parameters                     |
| ⏱️ **Simulation Metadata** | Estimates configured simulation duration                 |
| 📝 **Log Inspection**      | Searches for completion and obvious fatal-error patterns |
| 🩺 **QC Summary**          | Produces PASS / WARN / FAIL checks                       |
| 🌐 **HTML Reports**        | Generates standalone browser-readable reports            |
| 💻 **CLI Interface**       | Designed for terminal-based workflows                    |
| 🐍 **Python Package**      | Easy to install and extend                               |

---

# 🧪 Current Analysis Pipeline

```text
              🧬 GROMACS Simulation
                       │
                       ▼
              📂 Simulation Folder
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     📄 Files       ⚙️ .mdp         📝 .log
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                🔍 BioSimBench
                       │
              ┌────────┴────────┐
              ▼                 ▼
        🩺 QC Checks       📊 Metadata
              │                 │
              └────────┬────────┘
                       ▼
                📋 QC Summary
                       │
                       ▼
              🌐 HTML QC Report
```

---

# 📦 Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Vishu1197/BioSimBench.git
cd BioSimBench
```

## 2️⃣ Create a virtual environment

### 🪟 Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 🐧 Linux / WSL / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3️⃣ Install BioSimBench

```bash
pip install -e .
```

---

# ▶️ Usage

Point BioSimBench toward a GROMACS simulation directory:

```bash
biosimbench path/to/md_run
```

Generate an HTML report:

```bash
biosimbench path/to/md_run --html report.html
```

The generated report can be opened directly in a web browser.

### 🐍 Run without installing the CLI

```bash
python -m biosimbench.cli path/to/md_run
```

---

# 📊 Example QC Output

A typical BioSimBench summary looks like:

```text
╔════════════════════════════════════════════╗
║              BioSimBench QC                ║
╠════════════════════════════════════════════╣
║ Overall Status: PASS                       ║
╠════════════════════════════════════════════╣
║                                            ║
║ ✓ Run input       md.tpr                   ║
║ ✓ Structure       md.gro                   ║
║ ✓ Topology        topol.top                ║
║ ✓ Trajectory      md.xtc                   ║
║ ✓ Energy          md.edr                   ║
║ ✓ Log             md.log                   ║
║ ✓ Parameters      md.mdp                   ║
║ ✓ Completion      Detected                 ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

# 🌐 HTML Reporting

BioSimBench can generate a standalone HTML report containing:

### 📋 Simulation Summary

* Simulation directory
* Detected GROMACS files
* Overall QC status

### ⚙️ Configuration

* `dt`
* `nsteps`
* Estimated simulation duration
* Other available `.mdp` metadata

### 🩺 Quality Checks

* File availability
* Log status
* Completion detection
* Fatal-error detection

### 📊 Report Status

BioSimBench uses three basic states:

🟢 **PASS** — Check completed successfully
🟡 **WARN** — Potential issue requiring review
🔴 **FAIL** — Check failed or required information is missing

---

# 🧬 Supported GROMACS Files

BioSimBench currently recognizes common simulation artifacts:

```text
├── md.tpr       🔧 Portable Run Object
├── md.gro       🧬 Coordinate / Structure File
├── topol.top    🧩 Topology
├── md.mdp       ⚙️ Simulation Parameters
├── md.xtc       🎞️ Compressed Trajectory
├── md.trr       🎞️ Full-precision Trajectory
├── md.edr       ⚡ Energy File
└── md.log       📝 Simulation Log
```

Additional filenames are supported as long as they use the expected GROMACS extensions.

---

# 🔬 Scientific Scope

BioSimBench is intentionally divided into two concepts:

### 🩺 Simulation QC

Checks whether the simulation appears structurally complete and whether obvious configuration or termination problems are present.

### 🔬 Scientific Analysis

Future versions will perform quantitative molecular-dynamics analyses such as:

* RMSD
* RMSF
* Radius of gyration
* Temperature stability
* Pressure
* Potential energy
* Total energy
* Hydrogen-bond analysis
* Solvent-accessible surface area
* Trajectory integrity
* Convergence diagnostics

This distinction is important:

> **A technically completed simulation is not necessarily a scientifically valid or converged simulation.**

BioSimBench therefore avoids treating basic file checks as proof of simulation quality.

---

# 🛣️ Roadmap

## 🟢 v0.1 — MVP

* [x] GROMACS file inventory
* [x] `.mdp` metadata extraction
* [x] `.log` inspection
* [x] Completion detection
* [x] Basic QC engine
* [x] CLI
* [x] HTML reporting

## 🟡 v0.2 — Energy Analysis

* [ ] `gmx energy` integration
* [ ] Temperature analysis
* [ ] Pressure analysis
* [ ] Potential energy
* [ ] Total energy
* [ ] Energy stability indicators

## 🟠 v0.3 — Structural Analysis

* [ ] RMSD
* [ ] RMSF
* [ ] Radius of gyration
* [ ] Hydrogen bonds
* [ ] SASA
* [ ] Automated trajectory processing

## 🔵 v0.4 — Advanced QC

* [ ] Trajectory integrity checks
* [ ] Periodic-boundary-condition diagnostics
* [ ] Drift detection
* [ ] Replicate comparison
* [ ] Basic convergence indicators

## 🟣 v1.0 — Research Dashboard

* [ ] Interactive dashboard
* [ ] Publication-quality plots
* [ ] JSON output
* [ ] REST/API interface
* [ ] Batch analysis
* [ ] Multi-replicate comparison
* [ ] Automated report generation

---

# 🏗️ Project Structure

```text
BioSimBench/
│
├── 📁 src/
│   └── 📁 biosimbench/
│       ├── 🐍 __init__.py
│       ├── 🖥️ cli.py
│       ├── ⚙️ parser.py
│       ├── 🩺 qc.py
│       └── 🌐 report.py
│
├── 📁 tests/
│   └── 🧪 test_qc.py
│
├── 📁 examples/
│   ├── 📂 sample_run/
│   └── 🌐 sample_report.html
│
├── 📄 pyproject.toml
├── 📄 README.md
├── 📄 LICENSE
└── 📄 .gitignore
```

---

# 🧪 Development

Run the test suite:

```bash
pytest
```

Expected result:

```text
2 passed
```

The project is designed to remain modular so that GROMACS analysis functions can be added without rewriting the existing QC engine.

---

# 🔭 Future Vision

BioSimBench is intended to evolve from a simple simulation checker into a **research-oriented molecular-dynamics quality-control and analysis framework**.

The long-term goal is:

```text
              GROMACS Simulation
                      │
                      ▼
                🧬 BioSimBench
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    🩺 QC          📊 Analysis    📈 Visualization
       │              │              │
       └──────────────┼──────────────┘
                      ▼
               🔬 Interpretation
                      │
                      ▼
               📋 Research Report
```

The emphasis is on **reproducibility, transparent checks, and researcher-friendly reporting** rather than replacing established GROMACS analysis tools.

---

# 🤝 Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

If you would like to contribute:

```bash
git clone https://github.com/Vishu1197/BioSimBench.git
cd BioSimBench
```

Create a feature branch:

```bash
git checkout -b feature/my-feature
```

Make your changes, run the tests, and submit a pull request.

---

# 📚 Scientific Software Philosophy

BioSimBench follows a simple principle:

> **Automate the checks, expose the evidence, and let the researcher make the scientific judgment.**

The tool should help researchers identify potential problems quickly without presenting automated QC results as definitive scientific conclusions.

---

# 📜 License

Released under the **MIT License**.

---

## 👨‍🔬 Author

**Vishal Chanda**

Bioinformatics • Computational Biology • Molecular Dynamics • Scientific Software

🔗 GitHub: **Vishu1197**

---

### ⭐ If BioSimBench is useful to you

Consider giving the repository a ⭐ on GitHub and sharing it with researchers working with GROMACS and molecular-dynamics simulations.

**BioSimBench — From simulation files to actionable QC.** 🧬🔬📊
