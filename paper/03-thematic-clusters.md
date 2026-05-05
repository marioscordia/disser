# Thematic Clusters and Comparative Analysis

**Research Topic:** Unbiased Learning to Rank (ULTR) and Context-Aware Information Retrieval (2021–2025)
**Total Papers Analyzed:** 69

---

## 1. Thematic Clusters

### Cluster 1: Position Bias, Selection Bias, and Unbiased Learning to Rank

| Dimension | Description |
|-----------|-------------|
| **Cluster Title** | Bias Detection and Correction in Learning to Rank |
| **Common Characteristics** | Studies in this cluster address various bias types (position, selection, examination, personalized) that distort click-based relevance signals. They employ counterfactual estimation (IPS, doubly robust), EM-based propensity modeling, and two-tower architectures to jointly estimate bias and relevance. |
| **Representative Studies** | Ovaisi et al. (2020) — selection bias correction via Heckman two-stage; Zhuang et al. (2021) — Cross-Positional Attention for flexible examination bias; Niu et al. (2025) — personalized bias via user-aware IPS; Amala & Rajeswari (2025a, 2025b) — APCP two-tower network and DPMM nonparametric click model; Fang et al. (2020) — permutation invariance for AutoULTR |
| **Summary of Key Findings** | Position bias remains the most studied bias type, but newer work addresses selection bias, context bias (in feeds), interactional observation bias, and personalized bias. Permutation invariance is necessary for AutoULTR convergence. IPS-based methods are increasingly replaced by doubly robust and two-tower architectures. Combined propensity models (position × context) consistently outperform single-bias methods. |

### Cluster 2: Context-Aware Neural Ranking and Transformer Architectures

| Dimension | Description |
|-----------|-------------|
| **Cluster Title** | Neural Architectures for Contextualized Document Ranking |
| **Common Characteristics** | Papers in this cluster develop and optimize neural ranking architectures that incorporate contextual signals — BERT-based cross-encoders, Graph Attention Networks, Fast-Forward indexes, and attention mechanisms. Focus on efficiency-interpretability tradeoffs and handling diverse query types (verbose, compositional, negated). |
| **Representative Studies** | Haddad et al. (2025) — ReGAT-BERT fusing BERT with GAT; Kumar et al. (2026) — 2P-BEnc two-phase BERT encoder (300x speedup); Leonhardt et al. (2022, 2024) — Fast-Forward indexes for efficient dual-encoder ranking; Hofstatter et al. (2021) — position bias mitigation in Transformer re-rankers; Krasakis et al. (2025) — zero-shot negation handling via disentangled LSR |
| **Summary of Key Findings** | Cross-encoder BERT architectures achieve highest ranking quality but are computationally prohibitive for first-stage retrieval. Dual-encoder + interpolation strategies provide competitive effectiveness with orders-of-magnitude lower cost. Lightweight query encoders and pre-computed passage vectors enable CPU-only neural ranking. Contextual embeddings and graph-based methods substantially improve handling of verbose and compositional queries. |

### Cluster 3: Recommender System Bias, Fairness, and Diversity

| Dimension | Description |
|-----------|-------------|
| **Cluster Title** | Fairness-Aware and Diversity-Promoting Recommendation |
| **Common Characteristics** | Studies addressing how ranking and recommendation algorithms create or amplify unfairness — popularity bias amplifying "rich-get-richer" dynamics, disparate exposure across demographic groups, diversity-relevance tradeoffs, and UI-driven evaluation biases (carousel layouts). |
| **Representative Studies** | Carnovalini et al. (2025) — narrative review of popularity bias origins and mitigation; He et al. (2024) — 3-type bias study with 667M-sample e-commerce data (online A/B: +2.4% CTR, +6.5% GMV); Cachel & Rundensteiner (2023) — fair Kemeny rank aggregation; Felicioni et al. (2021) & Ferrari Dacrema et al. (2022) — multi-carousel offline evaluation protocols; Chen et al. (2021) — tutorial on 6 bias categories in RS |
| **Summary of Key Findings** | Popularity bias is the most pervasive bias type in recommender systems, originating from both human cognitive tendencies (herd behavior) and algorithmic feedback loops. Fair ranking interventions (re-ranking, propensity weighting) can improve demographic balance but do not always translate to fair downstream outcomes (e.g., shortlisting). Multi-carousel UI layouts fundamentally change relative algorithm rankings compared to single-list evaluation. Industrial-scale studies confirm that bias correction yields measurable business impact. |

### Cluster 4: Generative Information Retrieval and LLM-Based Ranking

| Dimension | Description |
|-----------|-------------|
| **Cluster Title** | Large Language Models as Retrievers, Rankers, and Evaluators |
| **Common Characteristics** | Emerging paradigm where LLMs replace or augment traditional IR components: generative document retrieval (generating docIDs instead of indexing), LLM-as-ranker (instruction-tuned listwise ranking), LLM-as-evaluator (automated relevance judgments), and Retrieval-Augmented Generation (RAG) with semantic re-ranking. |
| **Representative Studies** | Li et al. (2025) — comprehensive GenIR survey; Luo et al. (2025) — RecRanker instruction-tuned LLM ranker; Deng et al. (2025) — DIVAgent LLM-powered diversification; Karlovic et al. (2025) — RAG with 7 LLMs + Cohere re-ranker for tourism; Ghosh & Mittal (2025) — KG-based RAG for engineering codes; Dai et al. (2024) — bias survey in LLM-era IR |
| **Summary of Key Findings** | GenIR represents a paradigm shift from similarity-matching to generative retrieval, potentially eliminating large-scale indexes. LLMs as rankers (RecRanker) outperform traditional models through instruction tuning and hybrid ensembling. RAG + semantic re-ranking pipelines achieve high relevance in domain-specific applications. However, LLMs introduce new bias types (source bias, hallucination bias, instruction bias) and face challenges in consistency, cost, and incremental learning. |

### Cluster 5: Evaluation, Survey, and Cross-Cutting Methodologies

| Dimension | Description |
|-----------|-------------|
| **Cluster Title** | Evaluation Frameworks, Systematic Reviews, and Domain-Specific IR |
| **Common Characteristics** | This cluster encompasses: (a) novel evaluation metrics beyond precision/recall (rank stability, EEG-based usefulness, 2D carousel NDCG); (b) comprehensive surveys and systematic reviews synthesizing the field; (c) domain-specific IR applications (IoT, edge computing, e-commerce, engineering, finance); (d) interpretability and feature attribution methods for ranking models. |
| **Representative Studies** | Batri et al. (2025a) — Rmeasure for rank stability; Batri et al. (2025b) — parabolic weighting via Lenz's Law; Gupta et al. (2023) — ULTR tutorial; Mateos & Bellogin (2025) — CARS systematic review; Manta-Caro et al. (2025) — IoT/WoT IR survey; Heuss et al. (2025) — RankingSHAP listwise feature attribution; Lyu et al. (2024) — feature selection interpretability for neural LTR |
| **Summary of Key Findings** | Traditional IR evaluation metrics (precision, recall, NDCG) are insufficient for capturing modern concerns: rank consistency across repeated queries, result diversity, fairness, and interpretability. Systematic reviews reveal that evaluation standardization remains a critical gap, particularly for context-aware systems. Domain-specific IR applications (IoT, edge computing, engineering RAG) face unique challenges around data sparsity, real-time constraints, and multimodal data integration. |

---

## 2. Cross-Cluster Comparative Analysis

### Similarities Across Clusters

All five clusters share a common theoretical foundation in addressing how user interaction signals (clicks, dwell time, ratings) are distorted by various biases and contextual factors. The dominant methodological approach across clusters is neural: BERT-based architectures, transformer attention mechanisms, and deep learning feature extraction appear in every cluster. A clear convergence trend exists toward two-tower architectures (separately modeling relevance and bias) — this pattern appears in Cluster 1 (bias correction), Cluster 2 (efficient ranking), and Cluster 4 (LLM-based ranking). Furthermore, all clusters demonstrate increasing concern with fairness and evaluation rigor, moving beyond traditional precision/recall metrics toward multidimensional assessment frameworks that account for diversity, consistency, and demographic balance.

### Differences Across Clusters

The clusters diverge primarily in their treatment of context. Cluster 2 operationalizes context as a feature to improve ranking accuracy (contextual embeddings, query-document interactions), while Cluster 3 treats context as a source of unfairness to be mitigated (exposure bias from UI layout, popularity feedback loops). Cluster 4 represents the most radical departure — shifting from retrieval as similarity matching to retrieval as generation, fundamentally changing the architecture of IR systems. Methodologically, Cluster 1 is the most theoretically rigorous (counterfactual causal inference, propensity estimation with formal guarantees), while Cluster 5 is the most heterogeneous, encompassing evaluation, surveys, and niche domain applications. The temporal distribution also differs: Cluster 1 (bias correction) has the deepest historical roots dating to early ULTR work (2020-2021), while Cluster 4 (GenIR/LLM) is the newest and fastest-growing, with most papers from 2025.

### Research Gaps

Several critical gaps emerge from this analysis. First, the intersection of ULTR and GenIR is severely underexplored — how do position bias, selection bias, and other click-based distortions manifest when LLMs generate results directly? Second, most bias correction methods have been validated on single platforms (Google, JD.com, Meituan) with limited cross-platform generalizability evidence. Third, fairness interventions are predominantly evaluated offline; online A/B tests measuring real-world fairness outcomes remain rare (only He et al., 2024 and a few industry papers). Fourth, context-aware ranking research remains dominated by a narrow set of context types (time, location, device), with little exploration of affective context, social context, or longitudinal user behavior patterns. Fifth, almost no work addresses bias in multimodal retrieval (text + images + structured data), despite growing industrial deployment of multimodal search. Finally, the reproducibility crisis is evident — many proposed architectures lack open-source implementations or standardized benchmark protocols, making fair comparison difficult.

---

## 3. Future Research Directions

Future research should prioritize: (1) **Unified bias frameworks for GenIR** — extending ULTR counterfactual methods to generative retrieval settings where documents are not retrieved but generated, requiring new formalizations of bias in LLM outputs. (2) **Cross-platform and longitudinal fairness evaluation** — moving beyond single-platform offline metrics to multi-platform, online A/B studies that measure real-world fairness outcomes over time. (3) **Multi-modal and multi-context bias modeling** — developing ranking frameworks that simultaneously account for diverse context types (affective, social, behavioral) and multiple media modalities. (4) **Computationally efficient debiasing** — creating lightweight bias correction methods compatible with real-time ranking pipelines, particularly for resource-constrained edge and IoT deployments. (5) **Standardized benchmarks and reproducibility infrastructure** — establishing shared evaluation protocols, open-source implementations, and benchmark datasets that enable rigorous comparison of bias correction and context-aware ranking methods across research groups.

---

✅ Thematic clustering and comparative synthesis successfully generated — ready for integration into the review results chapter.
