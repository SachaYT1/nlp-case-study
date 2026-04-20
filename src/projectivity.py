"""Non-projectivity detection for dependency trees.

An arc (head, dep) is *non-projective* iff some token strictly between
head and dep (in linear order) has its own head outside the [min, max]
span. This is the standard linear-order definition used in UD and matches
the textbook "crossing arcs" notion.

Heads are 1-indexed (0 = ROOT). Token indices below are 0-based positions
into the `heads` list; their linear position is `i + 1`.
"""
from __future__ import annotations


def nonprojective_arc_mask(heads: list[int]) -> list[bool]:
    """Return a per-token mask: True iff that token's incoming arc is non-projective."""
    n = len(heads)
    mask = [False] * n
    for i in range(n):
        h = heads[i]
        if h == 0:
            continue
        dep_pos = i + 1
        lo, hi = min(dep_pos, h), max(dep_pos, h)
        for j in range(n):
            pos_j = j + 1
            if not (lo < pos_j < hi):
                continue
            h_j = heads[j]
            if h_j == 0 or h_j < lo or h_j > hi:
                mask[i] = True
                break
    return mask


def sentence_is_projective(heads: list[int]) -> bool:
    return not any(nonprojective_arc_mask(heads))
