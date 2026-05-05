# Results

## 1. Corpus Overview

The systematic search and screening process identified 69 studies for inclusion in the qualitative synthesis, supplemented by 71 Scopus-indexed records for bibliometric analysis. Table 1 presents the distribution of included studies by year and document type.

**Table 1: Distribution of Included Studies by Year and Type**

| Year | Articles | Conference Papers | Reviews / Book Chapters | Total |
|------|----------|-------------------|-------------------------|-------|
| 2020 (early) | 1 | 5 | 1 | 7 |
| 2021 | 2 | 7 | 1 | 10 |
| 2022 | 2 | 7 | 1 | 10 |
| 2023 | 3 | 7 | 0 | 10 |
| 2024 | 6 | 5 | 0 | 11 |
| 2025 | 15 | 10 | 2 | 27 |
| 2026 (early) | 3 | 0 | 0 | 3 |
| **Total** | **32** | **41** | **5** | **78** |

*Note: The bibliometric corpus (71 Scopus records) partially overlaps with the qualitative synthesis corpus (69 papers). Total exceeds 69/71 due to multi-year publication coverage across corpora.*

The included studies span 44 distinct publication venues. Table 2 lists the most frequent sources.

**Table 2: Top Publication Venues**

| Source | Papers | Type | Quartile |
|--------|--------|------|----------|
| IEEE Access | 7 | Open Access Journal | Q2 |
| CIKM 2025 Proceedings | 6 | Conference | Q1 |
| ACM Transactions on Information Systems | 6 | Journal | Q1 |
| SIGIR Proceedings (2021, 2023, 2025) | 5 | Conference | Q1 |
| Lecture Notes in Computer Science (ECIR) | 4 | Conference Proceedings | Q3 |

## 2. Thematic Clusters

Content analysis of the 69 papers identified five thematic clusters. Table 3 presents the cluster structure with representative studies.

**Table 3: Thematic Clusters in ULTR and Context-Aware IR Research**

| Cluster | Title | Papers | Core Focus | Representative Studies |
|---------|-------|--------|------------|----------------------|
| C1 | Bias Detection and Correction in LTR | 20 | Position, selection, examination, and personalized bias correction | Niu et al. (2025), Amala & Rajeswari (2025a), Fang et al. (2020), Zhuang et al. (2021) |
| C2 | Context-Aware Neural Ranking Architectures | 10 | BERT/GAT-based ranking, efficient dual-encoders, interpretable models | Haddad et al. (2025), Kumar et al. (2026), Leonhardt et al. (2024) |
| C3 | Recommender System Bias and Fairness | 11 | Popularity bias, multi-carousel evaluation, fair ranking aggregation | Carnovalini et al. (2025), He et al. (2024), Cachel & Rundensteiner (2023) |
| C4 | Generative IR and LLM-Based Ranking | 12 | GenIR, LLM-as-ranker, RAG with re-ranking | Luo et al. (2025), Li et al. (2025), Deng et al. (2025), Karlovic et al. (2025) |
| C5 | Evaluation, Surveys, and Cross-Cutting Methods | 16 | Novel metrics, systematic reviews, domain-specific IR | Batri et al. (2025a), Gupta et al. (2023), Manta-Caro et al. (2025) |

### Cluster 1: Bias Detection and Correction in Learning to Rank

This cluster, comprising 20 papers (29% of the corpus), represents the largest and most methodologically mature research area. The studies address a progression of bias types: position bias (the most studied, appearing in 14 papers), selection bias (Ovaisi et al., 2020), interactional observation bias (Chen et al., 2021), personalized bias (Niu et al., 2025), and context bias in feeds recommendation (Wu et al., 2021). Methodologically, the cluster shows a clear evolution from IPS-based estimation (Qin et al., 2020) through doubly robust learning (Luo et al., 2023) to two-tower neural architectures that jointly estimate bias and relevance (Amala & Rajeswari, 2025a). Fang et al. (2020) established the theoretical result that permutation invariance is a necessary and sufficient condition for multivariate scoring functions to converge under AutoULTR algorithms. The most recent work (Niu et al., 2025) addresses personalized bias through user-aware IPS estimation, demonstrating that modeling user-specific propensity distributions yields lower variance than population-average approaches.

### Cluster 2: Context-Aware Neural Ranking Architectures

Ten papers (14% of the corpus) constitute this architecturally focused cluster. The dominant pattern is the integration of BERT-based semantic relevance scoring with complementary mechanisms: Graph Attention Networks for contextual similarity (Haddad et al., 2025), Markov Random Fields for verbose query term dependencies (Podder et al., 2025), and cross-passage attention for long-document integration (Kumar et al., 2026). An important sub-theme is computational efficiency: Leonhardt et al. (2022, 2024) show that dual-encoder models with pre-computed passage vectors and lightweight query encoders achieve competitive effectiveness while eliminating GPU dependency. Yang et al. (2022) demonstrate that composite re-ranking without transformer computation at inference time can approximate BERT cross-encoder quality. Krasakis et al. (2025) address the underexplored problem of compositional and negated queries, showing that zero-shot linear algebra on learned sparse representations can handle set operations that standard retrievers fail on.

### Cluster 3: Recommender System Bias and Fairness

Eleven papers (16% of the corpus) address bias from a fairness and evaluation perspective. Carnovalini et al. (2025) provide a narrative review documenting how popularity bias originates from both human cognitive tendencies (herd behavior, mere exposure effect) and algorithmic amplification (collaborative filtering favoring popular items). He et al. (2024) present the largest-scale empirical study in the corpus, analyzing three bias types across 667 million training samples from a major e-commerce platform, with online A/B tests showing +2.4% CTR, +1.2% CVR, and +6.5% GMV improvements. A distinct sub-theme addresses evaluation methodology: Felicioni et al. (2021) and Ferrari Dacrema et al. (2022) show that multi-carousel user interfaces fundamentally change relative algorithm rankings compared to traditional single-list evaluation, leading to different conclusions about which recommendation algorithms are optimal.

### Cluster 4: Generative IR and LLM-Based Ranking

Twelve papers (17% of the corpus) represent the newest and fastest-growing cluster. Li et al. (2025) categorize GenIR into two paradigms — generative retrieval (generating document identifiers directly) and reliable response generation (producing answers grounded in retrieved evidence). Luo et al. (2025) demonstrate that instruction-tuned LLMs can serve as effective listwise rankers, with adaptive user sampling and hybrid ensembling strategies. Deng et al. (2025) present DIVAgent, an LLM-powered search diversification agent that outperforms unsupervised baselines by 3.1% in alpha-nDCG. Application-focused studies show the versatility of the paradigm: Karlovic et al. (2025) evaluate seven LLMs for tourism recommendation via RAG with semantic re-ranking, and Ghosh and Mittal (2025) apply KG-based RAG to engineering code interpretation. However, Dai et al. (2024) identify five new bias types introduced by LLMs — source bias, factuality bias, position bias, popularity bias, and instruction-hallucination bias — that lack the formal counterfactual treatment developed for traditional IR biases.

### Cluster 5: Evaluation, Surveys, and Cross-Cutting Methods

Sixteen papers (23% of the corpus) form a heterogeneous cluster encompassing evaluation methodology innovations, comprehensive surveys, and domain-specific IR applications. Batri et al. (2025a) introduce Rmeasure, a search engine consistency framework that applies Weber-Fechner psychophysical modeling to quantify rank stability, revealing significant consistency differences between Google and Bing. Batri et al. (2025b) propose a parabolic term-weighting mechanism inspired by Lenz's Law that outperforms BM25 on standard TREC benchmarks. Heuss et al. (2025) extend SHAP to listwise feature attribution, enabling identification of biased features in ranking models. Survey contributions include Gupta et al. (2023) on ULTR foundations, Mateos and Bellogin (2025) on context-aware recommender systems, and Manta-Caro et al. (2025) on IR for IoT and Web of Things. Domain-specific applications span edge computing service ranking (Huang et al., 2025), financial sentiment analysis (De Leon & Medda, 2025), and music discovery interfaces (Melchiorre et al., 2023).

## 3. Bibliometric Findings

### 3.1 Keyword Co-occurrence Analysis

Table 4 lists the most frequent author keywords and their co-occurrence patterns.

**Table 4: Top 15 Keywords by Frequency**

| Rank | Keyword | Frequency | Strongest Co-occurrence Partner |
|------|---------|-----------|-------------------------------|
| 1 | information retrieval | 12 | ranking (3 shared papers) |
| 2 | recommender systems | 7 | evaluation (2 shared papers) |
| 3 | ranking | 7 | information retrieval (3), interpolation (2) |
| 4 | position bias | 6 | click models (2), examination bias (2) |
| 5 | unbiased learning to rank | 5 | click model (2), two-tower model (2) |
| 6 | learning to rank | 5 | position bias (2) |
| 7 | evaluation | 4 | recommender systems (2) |
| 8 | large language model | 4 | ranking (1), recommender system (1) |
| 9 | recommender system | 3 | large language model (1) |
| 10 | click models | 3 | examination bias (2), position bias (2) |

### 3.2 Temporal Trends

Figure 1 (described) illustrates the temporal evolution of dominant keywords. The period 2021–2022 is characterized by foundational ULTR work (position bias, click models, evaluation). By 2023, survey papers and tutorials codify the field's knowledge (ULTR tutorial, bias taxonomy). The year 2024 marks an inflection point: "large language model" enters the top-5 keyword list, and LLM-based IR research proliferates. The year 2025 shows accelerated growth (27 papers, 38% of the bibliometric corpus) driven by CIKM 2025 proceedings (6 papers) and expanding GenIR research.

### 3.3 Top Authors

Table 5 lists the most prolific and cited authors identified through the bibliometric and content analysis.

**Table 5: Top 10 Authors**

| Author | Papers | Research Focus | Country |
|--------|--------|---------------|---------|
| Avishek Anand | 5+ | Neural ranking, interpretability, Fast-Forward indexes | Netherlands |
| Harrie Oosterhuis | 4+ | ULTR, counterfactual LTR, click models | Netherlands |
| Qingyao Ai | 4+ | AutoULTR, doubly robust LTR, evaluation | China |
| Zhicheng Dou | 4+ | Generative retrieval, diversification, GenIR | China |
| Ji-Rong Wen | 3+ | Personalized bias, web search, generative retrieval | China |
| Maarten de Rijke | 3+ | Diversification, explainability, neural IR | Netherlands |
| Jurek Leonhardt | 4 | Efficient ranking, Fast-Forward, extractive explanations | Germany |
| Weinan Zhang | 3+ | Deep LTR, survival analysis, utility optimization | China |
| K.J. Amala | 3 | Neural LTR, bias correction, nonparametric click models | India |
| Sebastian Hofstatter | 3 | Position bias, efficient transformers, annotations | Austria |

### 3.4 PRISMA Flow Results

The PRISMA flow diagram (Section 2, Methodology) documents the study selection process. Of 155 initially identified records, 32 duplicates were removed, 28 were excluded during title/abstract screening, and 26 were excluded during full-text eligibility assessment. The final corpus of 69 studies was included in qualitative synthesis, with 71 Scopus-indexed records (partially overlapping) providing structured bibliometric data. The most common exclusion reasons at full-text stage were unavailability of full text (n = 8), insufficient methodological detail (n = 6), and extended versions of already-included papers (n = 5).
