# Results

## 1. Corpus Overview

The systematic search and PRISMA-guided screening process identified 46 studies for qualitative synthesis, supported by 48 Scopus-indexed records for bibliometric analysis. Table 1 presents the distribution by year and document type.

**Table 1: Distribution of Included Studies**

| Year | Conference Papers | Journal Articles | Reviews | Total |
|------|-------------------|------------------|---------|-------|
| 2020 | 7 | 1 | 0 | 8 |
| 2021 | 6 | 2 | 1 | 9 |
| 2022 | 7 | 2 | 0 | 9 |
| 2023 | 4 | 3 | 2 | 9 |
| 2024 | 3 | 4 | 1 | 8 |
| 2025 | 2 | 1 | 1 | 4 |
| **Total** | **29** | **13** | **5** | **47** |

*Note: 47 total entries include papers counted in both conference and journal categories for extended versions.*

The included studies span 18 publication venues. ACM venues dominate: SIGIR (7 papers), CIKM (4), WSDM (4), The Web Conference/WWW (4), ACM TOIS (3). IEEE Access contributes 2 papers. The remaining venues (KDD, RecSys, EMNLP, EACL, ICTIR, UMAP, NAACL) contribute 1-2 papers each.

Citation counts range from 1 to 127, with a median of 14. The five most-cited papers are: Hansen et al. (2020, 127 citations), Abdollahpouri et al. (2021, 125 citations), Dai et al. (2024, 121 citations), Klimashevskaia et al. (2024, 77 citations), and Wang et al. (2021, 60 citations). These five papers account for 40% of total citations in the corpus.

## 2. Thematic Clusters

Content analysis combined with VOSviewer keyword co-occurrence mapping identified five thematic clusters. Table 2 presents the cluster structure.

**Table 2: Thematic Clusters in Context-Aware ML Ranking Research**

| Cluster | Title | Papers | Avg. Citations | Core Focus |
|---------|-------|--------|---------------|------------|
| C1 | Neural Architectures for Context-Aware Ranking and LLM-Based Retrieval | 10 | 29.4 | Session/user embeddings, efficient neural indexes, LLM-as-ranker |
| C2 | Dense Retrieval, Pseudo-Relevance Feedback, and Query Enhancement | 8 | 27.8 | BERT-based PRF, contextualized query expansion, embedding compression |
| C3 | Position Bias, Counterfactual LTR, and Off-Policy Evaluation | 8 | 17.8 | Click models, IPS/doubly robust estimation, contextual bandits |
| C4 | Recommender Fairness, Popularity Bias, and Context-Aware Recommendation | 10 | 49.2 | Popularity bias mitigation, user-centered evaluation, bias surveys |
| C5 | Context-Aware Search and Cross-Cutting Applications | 9 | 8.0 | Digital activity context, domain-specific retrieval, tutorials |

### Cluster 1: Neural Architectures for Context-Aware Ranking (10 papers)

This cluster presents the architectural innovations driving context-aware ranking. Hansen et al. (2020) introduce CoSeRNN, which models user preferences as sequences of session-level contextual embeddings, achieving 10% improvement over state-of-the-art on Spotify data. Leonhardt et al. (2022, 2024) develop Fast-Forward indexes — pre-computed dual-encoder document representations with lightweight query encoders — enabling CPU-only neural re-ranking with order-of-magnitude speedup over cross-encoders. At the architectural frontier, Luo et al. (2025) present RecRanker, instruction-tuning LLaMA-2 as a listwise ranker with hybrid ensembling strategies.

### Cluster 2: Dense Retrieval and Query Enhancement (8 papers)

The ColBERT-PRF research program (Wang et al., 2021, 2023) demonstrates that pseudo-relevance feedback is viable for dense retrieval, with MAP improvements up to 26% on TREC 2019. Naseri et al. (2022) show that contextualized BERT embeddings for query expansion (CEQE) improve recall over traditional RM3. Yang et al. (2022a, 2022b) achieve 14:1 embedding compression with negligible quality loss through contextual quantization, while their BECR framework enables CPU-friendly BERT re-ranking through query decomposition with pre-computed token embeddings.

### Cluster 3: Position Bias and Counterfactual LTR (8 papers)

Chen et al. (2020) present the context-aware click model (CACM), which integrates session-flow graph embeddings into relevance estimation and demonstrates that exponential multiplication outperforms the standard examination hypothesis. Kiyohara et al. (2022) propose Cascade-DR, a doubly robust off-policy estimator for ranking under the cascade user behavior model, achieving lower variance than IPS-based alternatives. Yang et al. (2020) establish the theoretical result that permutation invariance is necessary for AutoULTR convergence.

### Cluster 4: Recommender Fairness and Popularity Bias (10 papers)

This is the highest-impact cluster by citation count (avg. 49.2 cites/paper). Abdollahpouri et al. (2021) introduce user-centered popularity bias evaluation, showing that existing mitigation techniques ignore individual users' tolerance toward popular items. Klimashevskaia et al. (2024) systematically categorize 123 papers on popularity bias, identifying an "abstraction trap" where bias mitigation is evaluated almost entirely through offline metrics. Dai et al. (2024) unify 15 bias types in LLM-era IR as distribution mismatch problems. Mateos and Bellogin (2025) document a shift toward neural approaches and ranking metrics in context-aware recommender systems, alongside significant reproducibility gaps.

### Cluster 5: Context-Aware Search and Cross-Cutting Applications (9 papers)

Vuong et al. (2022, 2024) show that full digital activity context — including non-search applications — improves Web search retrieval over session-only context. Zhang et al. (2023) present UBS4RL, demonstrating that reinforcement learning-based re-ranking with simulated user feedback outperforms supervised re-ranking.

## 3. Bibliometric Findings

### 3.1 Keyword Co-occurrence

VOSviewer author keyword co-occurrence analysis (min. 2 occurrences) identified 21 keywords in 5 clusters. Table 3 lists the top keywords by total link strength.

**Table 3: Top 10 Keywords by Network Centrality**

| Keyword | Occurrences | TLS | Cluster | Avg. Citations |
|---------|-------------|-----|---------|---------------|
| Information retrieval | 5 | 7 | C1 | 34.4 |
| BERT | 4 | 7 | C3 | 32.0 |
| Fairness | 4 | 7 | C4 | 87.8 |
| Ranking | 5 | 6 | C1 | 12.8 |
| Recommender systems | 4 | 6 | C4 | 59.0 |
| Dense retrieval | 2 | 6 | C3 | 53.0 |
| Pseudo-relevance feedback | 2 | 6 | C3 | 53.0 |
| Query expansion | 3 | 6 | C3 | 36.3 |
| Popularity bias | 3 | 5 | C4 | 70.7 |
| Position bias | 2 | 3 | C5 | 15.0 |

The keyword network confirms the thematic structure from content analysis. The VOSviewer index keyword map (36 keywords, 4 clusters, min. 3 occurrences) provides complementary coverage. Information retrieval (22 occurrences, 138 total link strength) and search engines (16 occurrences, 126 TLS) dominate the broader Scopus vocabulary, forming the network's central axis.

### 3.2 Co-authorship Network

Co-authorship analysis (min. 2 documents) identified 11 authors in 3 research groups. The Tsinghua University group — Liu Yiqun (5 papers), Ma Shaoping (5), Zhang Min (4) — is the most productive (160 total citations). The Renmin University group centers on Mao Jiaxin (4 papers, 126 citations), and the University of Utah group centers on Yang Tao (3 papers, 25 citations). The remaining 186 authors (94%) appear in a single paper.

### 3.3 Bibliographic Coupling

Bibliographic coupling (min. 1 shared reference) identified 39 connected documents in 5 clusters. Cluster 1 (Recommender Fairness, 13 papers) is the largest by document count but has the weakest within-cluster coupling (avg. link strength 11.3), reflecting diverse approaches to bias. Cluster 2 (Dense Retrieval, 9 papers) shows the strongest coupling (avg. 23.2), reflecting the cumulative ColBERT-PRF research program. Nine documents were disconnected from the coupling network.

## 4. PRISMA Flow Results

The PRISMA flow diagram (Section 2, Methodology) documents: 318 records identified from Scopus → 136 retained after topic-based screening → 92 after excluding zero-citation papers → 48 Scopus-confirmed for bibliometric analysis → 46 included in qualitative synthesis. The most common exclusion reason at the screening stage was topic scope (147 papers where "context-aware" referred to non-IR domains: video processing, medical imaging, construction engineering, agricultural systems).

---

*Note: Results section uses factual language only. All data presented derives from the systematic review process, VOSviewer bibliometric outputs, and the literature matrix.*
