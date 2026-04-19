"""Unified parser wrappers using gold tokenization for fair UAS/LAS comparison."""
from __future__ import annotations

from dataclasses import dataclass

import spacy
import stanza
from spacy.tokens import Doc


@dataclass(frozen=True)
class ParseResult:
    heads: list[int]    # 1-indexed, 0 = root
    deprels: list[str]


class SpacyParser:
    """Transition-based parser via spaCy with gold tokenization."""

    def __init__(self, model: str) -> None:
        self.name = f"spacy:{model}"
        self.nlp = spacy.load(model, disable=["ner", "lemmatizer", "attribute_ruler"])

    def parse(self, sentences: list[list[str]]) -> list[ParseResult]:
        results: list[ParseResult] = []
        docs = [Doc(self.nlp.vocab, words=words) for words in sentences]
        for doc in self.nlp.pipe(docs):
            heads, deprels = [], []
            for tok in doc:
                head_idx = 0 if tok.head == tok else tok.head.i + 1
                heads.append(head_idx)
                deprels.append(tok.dep_.lower())
            results.append(ParseResult(heads=heads, deprels=deprels))
        return results


class StanzaParser:
    """Graph-based (biaffine) parser via Stanza with gold tokenization."""

    def __init__(self, lang: str) -> None:
        self.name = f"stanza:{lang}"
        stanza.download(lang, processors="tokenize,pos,lemma,depparse", verbose=False)
        self.nlp = stanza.Pipeline(
            lang=lang,
            processors="tokenize,pos,lemma,depparse",
            tokenize_pretokenized=True,
            verbose=False,
        )

    def parse(self, sentences: list[list[str]]) -> list[ParseResult]:
        text = "\n".join(" ".join(toks) for toks in sentences)
        doc = self.nlp(text)
        results: list[ParseResult] = []
        for sent in doc.sentences:
            heads = [w.head for w in sent.words]
            deprels = [w.deprel for w in sent.words]
            results.append(ParseResult(heads=heads, deprels=deprels))
        return results
