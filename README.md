# NLP Case Study 5.5 — Transition-Based vs Graph-Based Dependency Parsers

Comparison of spaCy (transition-based) and Stanza (graph-based) dependency parsers on UD-EWT (English) and UD-SynTagRus (Russian).

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_trf
python -m spacy download ru_core_news_lg
python scripts/download_data.py
```

## Run

Execute notebooks in order: `01_setup_and_data.ipynb` → `05_poster_figures.ipynb`.
