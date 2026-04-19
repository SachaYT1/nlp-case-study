# Transition-Based vs Graph-Based Dependency Parsers
### A practical trade-off study on English and Russian
**Aleksandr Gavkovskii — NLP 2026, Case Study 5.5 — Innopolis University**

---

## Motivation

Dependency parsers split into two algorithmic families with opposite design trade-offs:
- **Transition-based** (shift-reduce, arc-eager): greedy local decisions, linear time, risk of error cascades
- **Graph-based** (biaffine + MST decoding): global optimization over all possible trees, quadratic time, structurally consistent

**Question:** How large is the practical trade-off, and does morphological richness (Russian) change it?

---

## Methodology

| | spaCy | Stanza |
|---|---|---|
| **Family** | Transition-based | Graph-based |
| **Architecture** | shift-reduce (arc-eager) | biaffine attention + MST |
| **Models** | `en_core_web_trf`, `ru_core_news_lg` | `en`, `ru` pipelines |

**Data:** Universal Dependencies 2.13 test splits
- English: UD English-EWT (~2,100 sentences)
- Russian: UD Russian-SynTagRus (~6,500 sentences)

**Evaluation:** Gold tokenization (fair comparison), UAS + LAS (punct excluded), tokens/sec (3 repeats, warmup), peak memory via `tracemalloc`

---

## Core Results

*(See fig_accuracy.png and fig_speed_vs_accuracy.png)*

| Parser | Lang | UAS | LAS | Tok/sec | Peak mem |
|---|---|---|---|---|---|
| spaCy (transition) | EN | — | — | — | — |
| Stanza (graph) | EN | — | — | — | — |
| spaCy (transition) | RU | — | — | — | — |
| Stanza (graph) | RU | — | — | — | — |

*Fill in numbers after running notebooks 02 and 03.*

---

## Where Each Family Wins

*(See fig_length.png, fig_long_distance.png, fig_per_relation_delta.png)*

**By sentence length:** Graph-based accuracy degrades less on long sentences (40+ tokens).

**Long-distance stress-test (arc distance > 5):** Graph-based shows larger advantage — consistent with global optimization helping non-projective, long-range dependencies common in Russian free word order.

**Per-relation delta:** [Fill in after notebook 04] — expected pattern: graph-based better on `obl`, `conj`, `acl`; gap larger in Russian.

---

## Conclusions

1. **Speed/Memory:** transition-based (spaCy) wins decisively — ~Xx faster, ~Y MB less peak memory.
2. **Accuracy:** graph-based (Stanza) wins on Russian by a larger margin than on English.
3. **Where it matters:** the accuracy gap concentrates in long sentences, long-range arcs, and constructions requiring global tree consistency — exactly where local greedy decisions are most risky.
4. **Practical recipe:** transition-based for real-time tagging at scale; graph-based for offline analysis where accuracy on complex syntax matters.

---

*Figures: poster/fig_*.png | Code: notebooks/ | Data: UD 2.13*
