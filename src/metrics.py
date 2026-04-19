"""UAS / LAS metrics for dependency parsing."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Gold:
    heads: list[int]
    deprels: list[str]


@dataclass(frozen=True)
class Prediction:
    heads: list[int]
    deprels: list[str]


def _aligned(pred: list[Prediction], gold: list[Gold]) -> None:
    if len(pred) != len(gold):
        raise ValueError(f"sentence count mismatch: {len(pred)} vs {len(gold)}")
    for p, g in zip(pred, gold):
        if len(p.heads) != len(g.heads):
            raise ValueError(
                f"token count mismatch: {len(p.heads)} vs {len(g.heads)}"
            )


def _is_punct(deprel: str) -> bool:
    return deprel == "punct" or deprel.startswith("punct:")


def uas(
    pred: list[Prediction],
    gold: list[Gold],
    exclude_punct: bool = True,
) -> float:
    """Unlabeled Attachment Score."""
    _aligned(pred, gold)
    correct = total = 0
    for p, g in zip(pred, gold):
        for ph, gh, gr in zip(p.heads, g.heads, g.deprels):
            if exclude_punct and _is_punct(gr):
                continue
            total += 1
            if ph == gh:
                correct += 1
    return correct / total if total else 0.0


def las(
    pred: list[Prediction],
    gold: list[Gold],
    exclude_punct: bool = True,
) -> float:
    """Labeled Attachment Score."""
    _aligned(pred, gold)
    correct = total = 0
    for p, g in zip(pred, gold):
        for ph, pd_, gh, gd in zip(p.heads, p.deprels, g.heads, g.deprels):
            if exclude_punct and _is_punct(gd):
                continue
            total += 1
            if ph == gh and pd_.split(":")[0] == gd.split(":")[0]:
                correct += 1
    return correct / total if total else 0.0
