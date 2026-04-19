"""Shared plotting style for poster figures."""
from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns

PARSER_COLORS = {
    "spacy:en_core_web_trf": "#1f77b4",
    "spacy:ru_core_news_lg": "#1f77b4",
    "stanza:en": "#ff7f0e",
    "stanza:ru": "#ff7f0e",
}

FAMILY = {
    "spacy:en_core_web_trf": "transition-based",
    "spacy:ru_core_news_lg": "transition-based",
    "stanza:en": "graph-based",
    "stanza:ru": "graph-based",
}


def apply_poster_style() -> None:
    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams.update({
        "figure.dpi": 120,
        "savefig.dpi": 200,
        "axes.titleweight": "bold",
    })
