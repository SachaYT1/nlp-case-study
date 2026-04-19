"""CoNLL-U loading utilities."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import conllu


@dataclass(frozen=True)
class Sentence:
    sent_id: str
    tokens: list[str]
    heads: list[int]
    deprels: list[str]
    upos: list[str]


def load_sentences(path: Path | str) -> list[Sentence]:
    """Load sentences from a CoNLL-U file, skipping multi-word expansions."""
    text = Path(path).read_text(encoding="utf-8")
    out: list[Sentence] = []
    for tree in conllu.parse(text):
        tokens, heads, deprels, upos = [], [], [], []
        for tok in tree:
            if not isinstance(tok["id"], int):
                continue
            tokens.append(tok["form"])
            heads.append(tok["head"])
            deprels.append(tok["deprel"])
            upos.append(tok["upos"])
        out.append(Sentence(
            sent_id=tree.metadata.get("sent_id", ""),
            tokens=tokens, heads=heads, deprels=deprels, upos=upos,
        ))
    return out


def bucket_by_length(sentences: list[Sentence]) -> dict[str, list[Sentence]]:
    """Group sentences into length buckets: 1-10, 11-20, 21-40, 40+."""
    buckets: dict[str, list[Sentence]] = {"1-10": [], "11-20": [], "21-40": [], "40+": []}
    for s in sentences:
        n = len(s.tokens)
        if n <= 10: buckets["1-10"].append(s)
        elif n <= 20: buckets["11-20"].append(s)
        elif n <= 40: buckets["21-40"].append(s)
        else: buckets["40+"].append(s)
    return buckets
