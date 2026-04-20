"""CLEAR-style → UD label mapping for spaCy's `en_core_web_trf`.

`en_core_web_trf` predicts CLEAR-style dependency labels (ClearNLP),
not pure UD. This biases raw LAS numbers downward by construction.
Use `remap_label` to translate a predicted deprel to its closest UD
equivalent before computing LAS.

Mapping is a *majority rule*: where a CLEAR label covers several UD
relations (e.g. pobj ⊃ {obl, nmod}), we pick the most frequent UD
counterpart observed in UD English-EWT test, and acknowledge the
resulting LAS is a lower-bound — a full conversion would also need to
re-structure heads around the preposition chain.
"""
from __future__ import annotations


CLEAR_TO_UD: dict[str, str] = {
    # Prepositional chain: CLEAR uses PREP(prep) -> pobj(NOUN) headed by prep.
    # UD uses case(prep) headed by NOUN; NOUN is obl/nmod of its own head.
    # Label-only remap can't fix the head structure, so UAS on these tokens
    # still penalises spaCy — LAS here is an upper bound under fair labels.
    "prep": "case",
    "pobj": "obl",        # majority: obl 963 > nmod 715 in top confusions
    "dobj": "obj",
    "poss": "nmod",
    "nsubjpass": "nsubj",
    "auxpass": "aux",
    "relcl": "acl",
    "npadvmod": "obl",
    "prt": "compound",
    "neg": "advmod",
    "attr": "xcomp",
    "acomp": "xcomp",
    "oprd": "xcomp",
    "quantmod": "advmod",
    "agent": "case",
    "dative": "iobj",
    "intj": "discourse",
    "preconj": "cc",
    "predet": "det",
    "meta": "parataxis",
}


def remap_label(label: str) -> str:
    """Return UD-normalised label; subtypes split on ':' like existing metrics."""
    base = label.split(":")[0]
    return CLEAR_TO_UD.get(base, base)
