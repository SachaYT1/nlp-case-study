# NLP Case Study 5.5 — Transition-Based vs Graph-Based Dependency Parsers

**Aleksandr Gavkovskii · Innopolis University · NLP 2026**

A practical comparison of two dependency-parsing families on English and Russian:

- **spaCy** — transition-based (shift-reduce, arc-eager)
- **Stanza** — graph-based (biaffine attention + MST decoding)

Measured: **accuracy** (UAS / LAS), **throughput** (tokens/sec), **peak memory**, plus error analysis by sentence length, long-distance arcs, projectivity, per-relation deltas, and an EN label-fairness check (CLEAR → UD remap).

**Deliverable:** [`poster/poster.md`](poster/poster.md) + seven figures under [`poster/`](poster/).

## Repository layout

```
data/           UD 2.13 .conllu test files (downloaded via scripts/download_data.py)
src/            data loading, parsers, metrics, perf, plotting, projectivity, label_map
notebooks/      01 setup → 06 extra experiments + kaggle_run_all (master)
results/        output CSVs (accuracy, performance, by_length, projectivity, etc.)
poster/         poster.md + fig_*.png
tests/          pytest for metrics and data loading
```

## Reproducing the experiments

### Local (Python 3.12)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_trf
python -m spacy download ru_core_news_lg
python scripts/download_data.py
```

Then run notebooks **in order**:

| Notebook | Writes to |
|---|---|
| `01_setup_and_data.ipynb` | sanity check only |
| `02_benchmark_accuracy.ipynb` | `results/accuracy.csv` |
| `03_benchmark_speed_memory.ipynb` | `results/performance.csv` |
| `04_error_analysis.ipynb` | `results/accuracy_by_length.csv`, `accuracy_by_relation.csv`, `long_distance_stress.csv`, `confusion_top.csv` |
| `06_extra_experiments.ipynb` | `results/projectivity.csv`, `en_label_fairness.csv` |
| `05_poster_figures.ipynb` | `poster/fig_*.png` (reads all CSVs above) |

Notebooks 02 / 03 / 04 / 06 each re-parse full test sets — cache predictions if you iterate.

### Kaggle (one-click)

Open [`notebooks/kaggle_run_all.ipynb`](notebooks/kaggle_run_all.ipynb) on Kaggle. It clones the repo, installs deps, downloads UD, and runs 02 → 06 → 05 in sequence. Each individual notebook also has a self-contained Kaggle/Colab bootstrap cell, so they can be opened standalone.

### Tests

```bash
pytest tests/
```

## Design notes

- **Gold tokenization everywhere** — isolates the parser, not the tokenizer.
- **Punctuation excluded** from UAS/LAS (standard UD practice); label subtypes normalized via `.split(":")[0]`.
- **Family mapping** lives in [`src/plotting.py::FAMILY`](src/plotting.py) — single source of truth.
- When adding an experiment: write a CSV to `results/`, read it in `05_poster_figures.ipynb`, and reference the figure from `poster/poster.md`.

## License & attribution

Data: Universal Dependencies 2.13 (CC BY-SA 4.0 per treebank licenses — UD-EWT, UD-SynTagRus).
Models: spaCy (MIT), Stanza (Apache 2.0).
