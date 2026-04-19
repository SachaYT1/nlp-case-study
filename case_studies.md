# NLP 2026. Case Studies

## What are Case Studies?

Case studies are individual mini-projects for students to obtain practical skills and explore the NLP-related topics more deeply. This document contains more than 50 case study titles with their brief descriptions. The case studies will be distributed over all the students for individual performance. Read below for more details on case studies distribution, deliverables, deadlines, and grading.

## Case Studies Distribution (Bidding)

The students are required to select 3 preferrable case studies from the List of Case Studies and provide their preferences in the [special form](https://forms.yandex.ru/u/69a6dcbe902902487e5a5b5c) until **March 8, 23:59**. The students are also allowed to provide their own case studies by proivding the title and the brief description in the same special form. By March 11, the list of case studies assigned to the students will be published. 

**Note**: Maximum 2 students may take the same case study and work independently. Even though the instructors will try to assign the case studies according to the students' preferences, **the preferred case studies are not guaranteed**. A random case study may be assigned to a student if many students select the same case study. To ensure you obtain the case study you want, you may provide your own case study. 

## Expected Deliverables

As a result of conducting the case studies, the students are expected to provide a **link to the GitHub repository** in Moodle. 

The GitHub repository should contain:

1. One or more **Jupiter notebooks** with the source code of the conducted experiments. 

    **Note**: The notebooks must be structured, clear, sufficiently commented, and contain no major errors, otherwise the grade will be decreased. 

2. A **poster** in .pdf format containing the motivation for the case study, methodology, experimental setup (datasets, models, etc.), results, and conclusions. Adding visuals is recommended and may positively affect the grade. 

    [Example of a poster](https://disk.yandex.ru/i/6OJMmrcJXO9dOA)

## Deadlines

1. The students fill in the case study preference form: **March 8, 23:59**
2. The instructors publish the list of case studies assigned to the students: **March 11**
3. The students submit and present the results of the case studies: **Final Exam (Datetime to be announced)** 

## Grading

The case studies will be graded during the final exam. The students must present the results by providing 1) **background of the case study**, 2) **experimental results** and 3) **conclusions**. It is expected that the students accompany the explanations with the poster.

The case study presentation is awared with **50% of the grade of the Final Exam**. The case studies will be graded by how well the experiments are performed and whether the experiments indeed justify the conclusions.

## List of Case Studies

### 1. Tokenization

1. **Impact of Tokenization on Text Classification**

    The goal of this case study is to investigate how different tokenization methods affect the performance of NLP models on downstream tasks such as text classification. Students need to compare traditional tokenization approaches (word-level, rule-based) with modern subword methods (Byte-Pair Encoding, WordPiece, SentencePiece) to see which methods preserve information better and improve model performance.

2. **Tokenization Across Languages**

    The goal of this case study is to analyze and compare different tokenization methods across languages with varying morphological complexity. Students need to explore how tokenization strategies perform on morphologically rich languages (e.g., Finnish, Turkish, Hungarian) and analytic languages (e.g., English, Chinese). Students will investigate tokenizer efficiency, vocabulary size, sequence lengths, and downstream NLP performance for these languages.

3. **Domain-specific Tokenization**

    The purpose of this case study is to develop and evaluate a tokenizer tailored to a specific domain, such as biomedical literature, legal documents, or social media text. Students need to explore how domain characteristics affect tokenization, and how customizing tokenization can improve downstream NLP tasks like classification, information extraction, or named entity recognition (NER).

4. **Multilingual Tokenization**

    The goal of this case study is to investigate how tokenization behaves across multiple languages, particularly low-resource languages, and to develop strategies that improve token coverage and downstream NLP performance.

    Students need to explore challenges such as:
    - High out-of-vocabulary (OOV) rates in low-resource languages
    - Tokenizer inefficiency when applied to multilingual corpora
    - Subword vs. word-level tokenization for languages with complex morphology

5. **Tokenization Impact on Transformers**

    The purpose of this case study is to explore how different tokenization strategies influence Transformer-based models like BERT, RoBERTa, GPT, or DistilBERT.

    Students will study:
    - How tokenization affects sequence length and vocabulary coverage
    - Impact on training time and computational efficiency
    - Effect on downstream task performance (accuracy, F1-score)

    The focus is on understanding the trade-offs between tokenizer granularity and model efficiency/performance.

6. **Neural Tokenizers**

    The goal of this case study is to implement a neural network-based tokenizer and compare its performance with traditional tokenization approaches such as Byte-Pair Encoding (BPE) and WordPiece.

7. **Tokenization for Noisy Texts**

    The goal of this case study is to design and evaluate tokenization strategies that are robust to noisy text, such as:

    - OCR outputs (errors in character recognition, missing spaces)
    - ASR transcriptions (misheard words, lack of punctuation)
    - Social media text (misspellings, emojis, hashtags, mentions, abbreviations)

    Students will explore how noisy text affects tokenization and its impact on downstream NLP tasks, and propose strategies to improve token coverage and model performance.

8. **Tokenization for Code-Switched and Mixed-Language Text**

    The goal of this case study is to investigate how tokenization methods handle code-switched and mixed-language text, where multiple languages appear within the same sentence or document (e.g., English–Spanish, Hindi–English, Arabic–French).

    Students will explore:
    - How traditional (word-level) vs. subword (BPE, WordPiece, SentencePiece) tokenizers handle intra-sentence language switching
    - The impact of shared vs. language-specific vocabularies on token fragmentation and OOV rates
    - Sequence length inflation caused by mixed-language morphology and script differences
    - The effect of tokenization strategies on downstream tasks such as sentiment analysis, named entity recognition (NER), and machine translation

    Students will design experiments comparing monolingual tokenizers, multilingual tokenizers, and hybrid approaches (e.g., language-ID-aware tokenization), and evaluate their impact on model efficiency and task performance.

9. **Tokenization of Numerical Expressions and Structured Data**

    The goal of this case study is to investigate how different tokenization strategies handle numerical expressions and structured data (e.g., dates, times, currency, percentages, scientific notation), and how this affects downstream NLP performance.

    Students will explore:
    
    - How word-level vs. subword tokenizers (BPE, WordPiece, SentencePiece) segment large numbers (e.g., 1,000,000 vs. 1000000), decimals (3.14159), scientific notation (1.2e-5), dates and times (2026-03-01, 10:45 PM), currency values ($19.99, €1,200), percentages (12.5%), fractions (3/4)
    
    - Vocabulary fragmentation: Do tokenizers split numbers into many sub-tokens? Are frequent numbers stored as single tokens? How does this affect sequence length?
    
    - Generalization and compositionality: Can models generalize to unseen numbers? Does digit-level tokenization improve numerical reasoning?
    
    - Impact on downstream tasks: Financial text classification, Scientific document understanding, Question answering involving quantities, Numerical reasoning benchmarks

    The focus is on understanding trade-offs between vocabulary size, model efficiency, numerical reasoning ability, and downstream task accuracy.

### 2. Language Modelling

1. **Adaptive Domain N-gram Benchmark**

    Collect a small in-domain corpus (e.g., finance, medical, or gaming forums), train baseline 3-gram/5-gram models with standard smoothing, then iteratively adapt the model with incremental domain data to study how perplexity, coverage, and rare-word handling evolve.

2. **Smoothing Strategies for Low-Resource Corpora**

    Implement and compare Laplace, Good-Turing, absolute discounting, and Kneser–Ney smoothing on shrinking subsets of a corpus to document when each technique breaks down and to propose a decision guide for practitioners.

3. **Hybrid Word+Character N-gram for Error Correction**

    Combine character-level and word-level n-grams to detect and auto-correct noisy OCR or social-media text, evaluating accuracy on synthetic noise datasets and reporting gains over vanilla word n-grams.

4. **Edge-Friendly Feed-forward Language Model** 

    Design a compact FFNN LM with shared embeddings and projection bottlenecks, measure its latency/throughput on CPU-only hardware, and compare accuracy/perplexity against a same-parameter n-gram baseline.

5. **CNN vs RNN LM for Code-Switching Streams**

    Build comparable CNN and GRU LMs, augment training data with short bilingual snippets, and analyze which architecture better tracks long-span dependencies and predicts switch points.

6. **Parameter-Efficient Transformer Fine-tuning**

    Take a small pretrained transformer LM, apply adapters or LoRA layers to specialize it for a niche domain corpus, and document the trade-offs between adaptation speed, GPU memory footprint, and downstream perplexity.

7. **Cross-Lingual Transfer for Low-Resource Language Modeling**

    Train a multilingual language model on a high-resource language (e.g., English) and adapt it to a typologically related low-resource language (e.g., Swahili or Welsh) using limited monolingual text. Compare strategies such as continued pretraining, vocabulary re-tokenization, and lightweight adapter tuning. Evaluate improvements in perplexity, morphological generalization, and zero-shot transfer on downstream tasks (e.g., text classification or next-word prediction). The case study would analyze how linguistic similarity and shared subword vocabularies influence transfer efficiency and data requirements.

8. **Retrieval-Augmented Language Modeling for Factual Consistency**

    Develop a retrieval-augmented language model that dynamically accesses an external document index during prediction. Compare its performance to a standard parametric transformer of similar size on fact-heavy corpora such as news or technical documentation. Measure gains in perplexity, factual accuracy, and robustness to outdated knowledge. Additionally, analyze latency overhead and memory trade-offs, proposing guidelines for when retrieval augmentation meaningfully improves modeling performance over purely parametric approaches.

9. **Context-Length Scaling and Memory Mechanisms in Long-Document Language Modeling**

    Investigate how different architectural strategies handle very long contexts (e.g., 8K–64K tokens) in document-level language modeling. Compare baseline transformer models with extended positional encodings, recurrent memory transformers, and sliding-window attention mechanisms on tasks such as long-form story continuation, legal document modeling, or research paper completion. Measure perplexity as a function of context length, attention sparsity, and memory reuse, while also tracking computational cost and stability during training. The study would aim to identify when increasing context length yields diminishing returns and which memory mechanisms most efficiently preserve long-range coherence.

### 3. Embeddings

1. **Effect of Corpus Size and Domain on Word Embeddings**

    The purpose of this case study is to analyze how the size and thematic focus of a training corpus influence the quality and semantic properties of the resulting word embeddings. Students will train identical embedding architectures (e.g., Word2Vec) on corpora of varying sizes (e.g., a small, focused news corpus vs. a large, general Wikipedia dump) and from different domains (e.g., biomedical literature vs. social media text). They will then evaluate the learned embeddings intrinsically, using word similarity benchmarks and analogy tasks, and extrinsically, by using them as features in a downstream task like text classification. The study aims to quantify the trade-offs between data quantity, domain specificity, and the resulting semantic fidelity of the embeddings.

2. **Window Size and Context Effects in Word2Vec**

    This case study is designed to investigate the critical role of the context window hyperparameter in Word2Vec models and its effect on the types of linguistic relationships captured in the embedding space. Students will train multiple Word2Vec models, systematically varying the context window size (e.g., from very narrow 2-word windows to much wider 10+ word windows). They will then analyze the resulting embeddings to determine which window sizes favor syntactic relationships (e.g., verb-tense, adjective-adverb) and which favor semantic or topical relationships (e.g., synonymy, "part-of" relationships). The goal is to develop a practical understanding of how this hyperparameter can be tuned to produce embeddings best suited for a specific NLP application.

3. **CBOW vs. Skip-gram Architectures**

    The goal of this case study is to conduct a detailed comparison of the Continuous Bag-of-Words (CBOW) and Skip-gram architectures within the Word2Vec framework, focusing on their training dynamics and the quality of the resulting word representations. Students will train both models on a common corpus and evaluate them on a range of NLP tasks, such as word analogy, concept categorization, and as input features for a simple text classifier. The investigation will cover training efficiency (time to convergence), their relative performance on frequent vs. rare words, and the qualitative differences in the semantic and syntactic relationships they capture. Students will synthesize their findings to recommend which architecture is preferable under different task constraints and data conditions.

4. **Static vs. Contextual Embeddings**

    The purpose of this case study is to empirically compare static embeddings (e.g., Word2Vec, GloVe) with contextual embeddings (e.g., BERT, RoBERTa) to understand their respective strengths and weaknesses in downstream NLP tasks. Students will select a benchmark task, such as Named Entity Recognition (NER) or Semantic Textual Similarity, and implement pipelines using both types of embeddings. They will analyze performance differences in terms of accuracy (F1-score, precision, recall), especially for polysemous words, out-of-vocabulary terms, and complex syntactic structures. The study aims to highlight the advantages of context-aware representations and identify scenarios where simpler, static embeddings might still be a computationally efficient and effective choice.

5. **Dynamic Embeddings for Temporal Language Change**

    This case study challenges students to use word embeddings as a tool for diachronic semantic analysis to track how word meanings evolve over time. Students will source a large, temporally-ordered corpus (e.g., historical newspaper archives, a decade of conference proceedings) and partition it into distinct time periods. They will then train separate embedding models for each time slice and align the resulting vector spaces to make them comparable. By tracking the cosine distance of a specific word's nearest neighbors across different time periods, students will identify and visualize semantic shifts, such as drift, broadening, or narrowing of meaning. The final output will be a quantitative and qualitative analysis of semantic change for a set of target words.

6. **Semantic Search Engine using Embeddings**

    The goal of this case study is to build a semantic search engine that moves beyond keyword matching to retrieve documents based on conceptual similarity using sentence embeddings. Students will take a collection of documents (e.g., research abstracts, news articles) and precompute their embeddings using a model like Sentence-BERT. They will then implement a search system where a user's query is embedded with the same model, and documents are retrieved by finding the nearest neighbors in the embedding space (e.g., using cosine similarity). Students will evaluate the system's performance by comparing its results to a standard keyword-based search (like TF-IDF) on a set of test queries, analyzing its ability to find relevant documents even when they contain no keyword overlap with the query.

7. **Plagiarism Detection using Embedding Similarity**

    The purpose of this case study is to develop a plagiarism detection system capable of identifying not only exact copies but also heavily paraphrased or semantically rewritten text by leveraging embedding similarity. Students will create a dataset of original documents and a set of "plagiarized" versions, generated through techniques like synonym substitution, sentence paraphrasing, and changes in sentence structure. They will then use sentence or document embeddings to compare the suspicious texts against the originals, flagging those with a similarity score above a certain threshold. The project will involve experimenting with different embedding models and similarity metrics to optimize for detecting different types of semantic plagiarism while minimizing false positives on unrelated texts.

8. **Recommendation Systems using Text Embeddings**

    This case study focuses on building a content-based recommendation system that uses text embeddings to suggest items to users based on the semantic content of their profiles or past interactions. Students will work with a dataset of items that have textual descriptions, such as movies (plots), news articles (headlines + text), or products (reviews). They will create user profiles by aggregating the embeddings of items a user has interacted with positively. The recommendation engine will then suggest new items by finding those whose embeddings are most similar to the user's profile vector. Students will evaluate their system's ability to make relevant and diverse recommendations, comparing its performance to a simple keyword-based recommender.

9. **Chatbot Response Ranking using Embeddings**

    The goal of this case study is to implement a response ranking module for a chatbot that selects the most appropriate reply from a set of candidates by computing its semantic similarity to the conversation context. Students will use a dataset of conversation turns (e.g., from Reddit or customer support logs). For a given context (the conversation history), they will embed it and compare it against embeddings of several candidate responses, which include both a correct "gold" response and several incorrect or less relevant distractors. By ranking the candidates based on cosine similarity and calculating metrics like Mean Reciprocal Rank (MRR) or Recall@k, students will evaluate the feasibility of using embeddings to guide dialogue generation and improve the coherence of open-domain chatbots.

### 4. Sequence Labelling for Parts of Speech and Named Entities

1. **Comparative Error Analysis of POS Taggers**

    The goal of this case study is to compare four sequence labelling approaches for POS tagging on the same benchmark split: averaged perceptron, HMM+Viterbi, CRF, and a compact BiLSTM tagger. Students will focus not only on final accuracy, but on *why* models fail by building confusion matrices, analyzing errors by sentence length and unknown-word rate, and inspecting frequent tag confusions (e.g., NN/JJ, VBD/VBN). The project outcome should include a practical recommendation of which model family works best under different constraints (data size, speed, interpretability) within a 4-5 week experimental scope.

2. **Feature Engineering Study for CRF-based POS and NER**

    This case study investigates how handcrafted features influence CRF performance on sequence labelling tasks. Students will design and compare feature sets such as token shape, prefixes/suffixes, capitalization, punctuation patterns, and local context windows for both POS and NER. They will run ablation experiments to quantify feature contribution and report trade-offs between model simplicity and quality.

3. **Unknown-Word Handling in HMM POS Tagging**

    The purpose of this case study is to evaluate different unknown-word strategies in HMM POS tagging with Viterbi decoding. Students will compare methods such as suffix-based heuristics, pseudo-word classes (e.g., NUM, ALLCAPS, hyphenated), add-k smoothing variants, and simple character-level backoff probabilities. Experiments should be conducted under controlled low-resource settings by subsampling training data. The project should identify which unknown-word strategy most improves tagging robustness when annotated data is limited.

4. **Domain Adaptation for Sequence Labelling**

    This case study focuses on transferring a POS/NER model trained on news text to a different domain such as social media, support tickets, or biomedical abstracts. Students will evaluate at least two adaptation strategies (for example, continued training on small in-domain labels, self-training with pseudo-labels, or simple vocabulary normalization). They will measure in-domain gains and quantify which error types decrease after adaptation. The final deliverable should highlight practical adaptation recipes feasible in 4-5 weeks.

5. **Pipeline Interaction: POS Tags as Features for NER**

    The goal of this case study is to test whether predicted POS tags improve downstream NER quality. Students will build a two-stage pipeline where a POS model provides features to a NER model, then compare against a NER baseline without POS input and, optionally, with gold POS tags as an upper bound. The study should include error propagation analysis to show when POS mistakes help or hurt entity recognition. Results should clarify whether adding POS in a pipeline is beneficial for realistic noisy settings.

6. **Character-aware BiLSTM for Robust Sequence Labelling**

    This case study explores whether character-level information improves sequence labelling robustness compared to word-only BiLSTM baselines. Students will implement or reuse a lightweight char-CNN or char-LSTM encoder and evaluate on OOV-heavy slices of POS or NER datasets. They should also test model behavior under synthetic noise (misspellings, casing changes, token splits/merges). The project objective is to quantify gains in robustness, not only aggregate scores.

7. **Annotation-Efficient NER with Active Learning**

    The purpose of this case study is to simulate limited annotation budgets and compare active learning strategies for NER. Students will start from a small labelled seed set and iteratively select new sentences using methods such as uncertainty sampling, entropy, or random selection baseline. They will track F1 versus annotation effort and estimate how many labels are saved by active selection. The outcome should be a practical guideline for building a NER system in 4-5 weeks with minimal manual labelling.

8. **BIO vs BIOES Label Encoding for NER**

    This case study examines how sequence label encoding schemes affect model quality and decoding stability in NER. Students will train comparable models (e.g., CRF or BiLSTM-CRF) under BIO and BIOES tags, then compare span-level F1, invalid transition rate, convergence speed, and class-wise performance on short vs long entities. They may add constrained decoding to enforce valid transitions.

9. **Latency-Constrained Sequence Labelling on CPU**

    This case study targets production-like constraints by benchmarking sequence labelling models under CPU-only inference budgets. Students will compare at least three models (for example, HMM, CRF, and BiLSTM) and report quality together with latency, throughput, and memory usage. Optional optimizations include batching, quantization, or vocabulary pruning. The project should end with a model selection recommendation for a real-time tagging scenario where both speed and quality matter.

### 5. Parsing

1. **Parsing Legal Contracts with Constituency Trees**

    This case study examines how constituency parsing can improve the interpretation of complex legal contracts. Legal sentences often contain deeply nested clauses, coordinated phrases, and long-distance dependencies. By using phrase structure trees, systems can better identify clause boundaries, embedded conditions, and hierarchical argument structures. The study evaluates how models such as those trained on the Penn Treebank enhance clause segmentation and support downstream tasks like obligation extraction and risk detection.

2. **Dependency Parsing for Social Media Text Normalization**

    This case study investigates the challenges of applying dependency parsing to informal social media text. Non-standard grammar, emojis, and ellipsis make traditional parsers struggle. The study compares transition-based dependency parsers with graph-based approaches when trained on adapted corpora derived from Universal Dependencies. It explores how dependency relations help recover implicit subjects and improve sentiment analysis performance.

3. **Cross-Linguistic Parsing in Morphologically Rich Languages**

    Focusing on languages such as Turkish and Finnish, this case study evaluates the relative strengths of constituency versus dependency parsing. Morphologically rich languages exhibit flexible word order, making phrase structure assumptions less reliable. The research analyzes how dependency parsing better captures head-dependent relations independent of surface order, while constituency parsing provides clearer phrase boundaries for semantic composition.

4. **Neural Constituency Parsing with Contextual Embeddings**

    This case study explores improvements in constituency parsing through contextual embeddings such as those from BERT. By integrating pretrained transformer representations into chart-based parsing architectures, researchers achieve state-of-the-art accuracy on benchmark datasets. The study highlights how contextual embeddings help resolve structural ambiguities like prepositional phrase attachment and coordination scope.

5. **Comparing Transition-Based and Graph-Based Dependency Parsers**

    This study contrasts transition-based parsers (e.g., shift-reduce systems) with graph-based global optimization approaches. Using datasets from CoNLL shared tasks, it evaluates parsing speed, memory efficiency, and accuracy trade-offs. The findings show that transition-based parsers excel in low-latency environments, while graph-based models provide higher global consistency in syntactic relations.

6. **Parsing for Question Answering Systems**

    This case study analyzes how constituency and dependency parses support question answering systems. Dependency structures help identify predicate-argument relationships crucial for fact extraction, while constituency trees assist in determining focus and scope in complex questions. The study demonstrates performance gains when integrating parse trees into transformer-based QA models trained on datasets such as SQuAD.

7. **Error Propagation in Downstream NLP Tasks**

    This case study investigates how parsing errors affect downstream applications such as machine translation and information extraction. It compares how mistakes in constituency boundaries versus incorrect dependency arcs influence semantic role labeling. Using benchmarks from Stanford NLP Group tools, the study proposes hybrid parsing representations to mitigate cascading errors and improve robustness.

8. **Hybrid Graph-Constituency Parsing for Biomedical Text Mining**

    This case study explores the integration of constituency and dependency parsing for extracting complex relations in biomedical literature. Scientific sentences often contain dense nominal compounds, appositions, and multi-level modifiers that challenge single-representation parsers. By combining phrase structure trees for accurate noun phrase boundary detection with dependency graphs for capturing predicate-argument relations, the study evaluates improvements in tasks such as protein–protein interaction extraction and event detection. Experiments conducted on corpora derived from the GENIA Project demonstrate that hybrid representations reduce ambiguity in coordination and attachment, leading to more precise entity-relation modeling.

9. **Low-Resource Parsing with Multilingual Transfer Learning**

    This case study investigates how constituency and dependency parsers can be adapted for low-resource languages using cross-lingual transfer techniques. Leveraging multilingual pretrained models fine-tuned on treebanks from the Universal Dependencies initiative, the research compares zero-shot and few-shot transfer strategies. The study examines whether dependency structures, due to their cross-linguistic consistency, transfer more effectively than phrase structure annotations. Results indicate that while dependency parsing benefits more from multilingual alignment, lightweight constituency parsers augmented with projection methods can improve syntactic depth modeling, ultimately enhancing tasks like part-of-speech tagging and morphological disambiguation in under-resourced languages.

### 6. Knowlege Graphs

1. **From Raw Text to Domain Knowledge Graph**

    The goal of this case study is to build a complete mini KG pipeline from a domain corpus (e.g., movie plots, research abstracts, or product reviews): entity extraction, relation extraction, triple normalization, and graph construction. Students should compare at least two extraction strategies (rule-based patterns vs off-the-shelf NLP extraction) and evaluate precision with manual sampling. The project should produce both the graph artifact and a quality audit of extracted triples.

2. **Relation Extraction Strategies for KG Construction**

    This case study focuses specifically on the relation extraction step and its impact on downstream KG usability. Students will compare dependency-pattern rules, OpenIE-style extraction, and a lightweight supervised classifier for selected relation types. They will measure relation precision/recall and error categories such as wrong argument boundaries or relation label confusion. The expected outcome is a recommendation of relation-extraction setup suitable for a 4-5 week student project.

3. **Ontology Granularity and Graph Quality**

    The purpose of this case study is to investigate how schema design changes KG quality and utility. Students will define two ontology variants for the same domain: a coarse schema (few entity/relation types) and a fine-grained schema (more specialized types). They will rebuild the KG under both settings and compare coverage, consistency, and downstream query usefulness. The project should highlight practical trade-offs between annotation complexity and graph expressiveness.

4. **Knowledge Graph Embedding Benchmark with PyKEEN**

    This case study compares multiple KGE models in a controlled setup using PyKEEN (e.g., TransE, PairRE, and ConvE or DistMult). Students will keep data split and evaluation protocol fixed, then report MRR and Hits@k for each model. They should additionally compare training time and parameter count to discuss efficiency-quality trade-offs. The final deliverable is a reproducible benchmark notebook and model selection rationale.

5. **Negative Sampling Study for KGE Training**

    This case study examines the effect of negative sampling design in sLCWA training. Students will vary the number/type of corrupted triples and compare training stability, convergence speed, and final link-prediction metrics. They may contrast sampled training against smaller-scale exhaustive LCWA-style settings when computationally feasible. The project should provide evidence-based guidance on which negative sampling configuration is most effective.

6. **Noise Robustness in Knowledge Graph Embeddings**

    The goal of this case study is to measure how KGE models degrade under noisy graph construction. Students will inject controlled amounts of noise (random triples, swapped entities, duplicated/conflicting relations) and evaluate robustness of MRR/Hits@k. They should compare at least two embedding models to identify which architecture is less sensitive to noisy triples.

7. **Graph-based Recommendation via Link Prediction**

    This case study applies KG methods to recommendation by modeling users, items, and metadata as a heterogeneous graph. Students will train a link-prediction model to infer likely user-item interactions and compare against a simple non-graph baseline (e.g., popularity or content similarity). Evaluation can use Recall@k, NDCG@k, and hit rate. The expected output is a compact recommendation prototype demonstrating the value of KG structure.

8. **Incremental KG Updates and Embedding Drift**

    This case study studies what happens when new triples are added over time. Students will simulate periodic KG updates, then compare full retraining against lightweight continued training and track embedding drift, metric changes, and update cost. They should analyze whether old relations degrade after new information is added. The project outcome should include a practical update policy for maintaining KGE models in evolving graphs.

9. **Explaining Link Predictions with Graph Paths**

    The purpose of this case study is to improve interpretability of KG link prediction results. Students will generate top-k predicted triples, then build path-based explanations (short relation chains) connecting head and tail entities. They will evaluate explanation quality through manual assessment criteria such as plausibility and relation coherence. The project should conclude with a simple explainability layer that makes embedding-based predictions easier to trust and debug.
