# Transition-Based vs Graph-Based Dependency Parsers
### A practical trade-off study on English and Russian
**Aleksandr Gavkovskii — NLP 2026, Case Study 5.5 — Innopolis University**

---

## Motivation

Dependency parsers split into two algorithmic families with opposite design trade-offs:
- **Transition-based** (shift-reduce, arc-eager): greedy local decisions, linear time, risk of error cascades
- **Graph-based** (biaffine + MST decoding): global optimization over all possible trees, quadratic time, structurally consistent

**Questions:**
1. How large is the practical speed/accuracy trade-off in production-grade implementations?
2. Does morphological richness and free word order (Russian) amplify the gap?
3. Where, structurally, does the graph-based family earn its wins?

---

## Methodology

| | spaCy | Stanza |
|---|---|---|
| **Family** | Transition-based | Graph-based |
| **Architecture** | shift-reduce (arc-eager) | biaffine attention + MST decoding |
| **EN model** | `en_core_web_trf` (RoBERTa) | `en` pipeline |
| **RU model** | `ru_core_news_lg` | `ru` pipeline |

**Data:** Universal Dependencies 2.13 test splits
- English: UD English-EWT — 2,077 sentences
- Russian: UD Russian-SynTagRus — 8,800 sentences

**Evaluation:** gold tokenization for fair comparison, UAS + LAS (punctuation excluded), tokens/sec on CPU (3 repeats + warmup), peak memory via `tracemalloc`.

**Caveat — EN LAS:** `en_core_web_trf` emits CLEAR-style labels (`dobj`, `pobj`, `prep`) rather than pure UD (`obj`, `obl`, `case`). This depresses its EN LAS by construction. We report UAS as the label-scheme-neutral accuracy metric and treat the LAS gap on EN as an **upper bound** rather than a fair attack.

---

## Core Results

| Parser | Lang | UAS | LAS | Tok/sec | Peak mem |
|---|---|---|---|---|---|
| spaCy (transition)  | EN | 0.615 | 0.450\* | 1,231 | 25.3 MB |
| Stanza (graph)      | EN | **0.907** | **0.883** |   488 | **13.6 MB** |
| spaCy (transition)  | RU | 0.895 | 0.845 | **12,435** | 70.9 MB |
| Stanza (graph)      | RU | **0.936** | **0.904** |   729 | **9.3 MB** |

\*EN LAS for spaCy reflects label-scheme mismatch with UD, not pure attachment error — see caveat.

![Accuracy — UAS and LAS by parser family](fig_accuracy.png)
*Figure 1. UAS and LAS by parser family on EN-EWT and RU-SynTagRus. The EN LAS bar for spaCy is depressed by label-scheme mismatch (see caveat above).*

![Speed vs accuracy trade-off](fig_speed_vs_accuracy.png)
*Figure 2. LAS vs tokens/sec (log scale). Transition-based (spaCy) sits top-right on RU — high throughput, acceptable accuracy. Graph-based (Stanza) dominates the accuracy axis on both languages.*

- **Speed:** transition-based is 2.5× faster on EN (transformer backbone) and **17× faster on RU** (lg CNN backbone).
- **Memory:** graph-based uses ~2× *less* peak memory in both languages — at the cost of throughput.
- **Accuracy (UAS):** Stanza leads everywhere; gap is **+29 pts on EN** (inflated by the LAS-label issue propagating into attachment choices) and **+4.1 pts on RU** on a fair UD head-to-head.

---

## Where Each Family Wins

### Sentence length
![LAS by sentence length bucket](fig_length.png)
*Figure 3. LAS by bucket (1–10, 11–20, 21–40, 40+ tokens). Both parsers degrade on long sentences; the graph-based gap widens slightly on RU 40+.*

Stanza degrades gracefully; spaCy is flatter only because it starts much lower.
**RU, UAS 1–10 → 40+:** Stanza 0.941 → 0.913 (−2.8 pt); spaCy 0.904 → 0.865 (−3.9 pt). The gap **widens from 3.7 pt to 4.9 pt** as sentences grow — consistent with greedy decisions accumulating more errors on long inputs.

### Long-distance arcs (head–dependent distance > 5)
![Long-distance arc stress test](fig_long_distance.png)
*Figure 4. Accuracy restricted to arcs where |head − dependent| > 5 tokens. The graph–transition gap is largest here, especially on EN (+37 pt UAS), and more than doubles on RU (9.8 pt vs 4.1 pt aggregate).*

| | EN UAS on long arcs | RU UAS on long arcs |
|---|---|---|
| spaCy (transition) | 0.388 | 0.742 |
| Stanza (graph) | **0.760** | **0.840** |
| Δ (graph − transition) | **+37.2 pt** | **+9.8 pt** |

This is the largest structural gap in the study. Long, often non-projective arcs are exactly the case where MST decoding pays off and greedy shift-reduce pays its error-cascade cost.
**On RU the long-arc delta (9.8 pt) is more than 2× the overall delta (4.1 pt)** — the aggregate number under-states how much graph-based actually helps on hard dependencies.

### Per-relation delta
![Per-relation accuracy delta heatmap](fig_per_relation_delta.png)
*Figure 5. (graph − transition) per-relation accuracy delta, top-15 most frequent UD relations per language. Red = graph-based better. The RU column isolates the fair comparison; note spaCy's `xcomp` / `iobj` wins as blue cells.*

**Russian (fair UD-vs-UD):** Stanza's biggest wins are on `compound` (+65 pt), `vocative` (+59 pt), `expl` (+67 pt), `flat` (+19 pt), `obl` (+16 pt), `parataxis` (+24 pt) — relations that span long distances, violate projectivity, or require global tree consistency. spaCy wins on a small set — notably `xcomp` (+6.9 pt) and `iobj` (+4.0 pt) — short-range, lexically-cued relations where local features suffice.

**Top RU confusions** (from [confusion_top.csv](../results/confusion_top.csv)) confirm the mechanism: spaCy's dominant error is mis-routing oblique arguments (`obl → advmod`, `obl → nmod`, `obl → obj`) — head-selection mistakes that propagate through the greedy stack.

---

## Conclusions

1. **Speed/Memory is not a tie.** Transition-based (spaCy) wins throughput decisively — **17× on RU, 2.5× on EN** — but *uses more* peak memory, because the CNN/transformer tagger dominates, not the parser. If you only care about throughput, the choice is obvious.
2. **Accuracy gap is real but narrower than folklore on RU.** Once label-scheme artefacts are controlled for, graph-based leads RU UAS by ~4 pt overall — meaningful, not dramatic.
3. **The gap concentrates where theory predicts.** Long arcs (+9.8 pt RU UAS), long sentences (widens by ~1 pt per length band), non-projective / global-structure relations (`obl`, `flat`, `parataxis`, `compound`). Exactly the regimes where greedy local decisions are most fragile.
4. **Morphological richness alone does not flip the verdict.** Russian is where you'd expect graph-based to dominate; it does, but the effect is strongest on *long-distance* constructions, not on morphology per se. RU's short-arc accuracy is already high for both families.
5. **Practical recipe:**
   - **High-volume, real-time, short text (chat, logs, search):** transition-based. The throughput is worth the 4-point UAS trade on RU.
   - **Offline analysis, long documents, legal / literary Russian, linguistic research:** graph-based. The gap on long arcs and non-projective constructions is structural, not incidental.
   - **Picking a label scheme matters.** If you need UD-conformant output, check label coverage before trusting an out-of-the-box LAS number.

---

*Figures: [poster/fig_*.png](.) | Code: [notebooks/](../notebooks/) | Results: [results/](../results/) | Data: UD 2.13*
