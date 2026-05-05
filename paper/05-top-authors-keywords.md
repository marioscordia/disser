# Top Authors, Keywords, and Thematic Trends

**Paper:** Relevance and Positioning: A Systematic Bibliometric Review of Context-Aware ML Ranking in Web Search and Recommendation Systems

---

## Table 1: Top 10 Most Influential Authors

| # | Author | Country / Affiliation | Research Focus | Key Representative Paper | Contribution Summary |
|---|--------|----------------------|----------------|-------------------------|----------------------|
| 1 | Liu Yiqun | China / Tsinghua University | Web search, click models, user behavior, context-aware ranking | Chen et al. (2020) — A context-aware click model for web search (47 cites) | Leads the most productive research group in the corpus (5 papers, 160 total citations). Pioneered context-aware click models integrating session, query, and document context for relevance estimation. |
| 2 | Ma Shaoping | China / Tsinghua University | Information retrieval, user behavior analysis, ranking evaluation | Wu et al. (2020) — Leveraging passage-level cumulative gain for document ranking (40 cites) | Co-leads the Tsinghua IR group (5 papers). Advanced passage-level signal integration for document ranking and context-aware factorization machines for recommendation. |
| 3 | Zhang Min | China / Tsinghua University | Search result evaluation, user modeling, context-aware ranking | Chen et al. (2020) — Efficient non-sampling factorization machines for context-aware recommendation (41 cites) | Core member of Tsinghua group (4 papers, 151 citations). Contributed to context-aware click models, recommendation, and search behavior analysis. |
| 4 | Mao Jiaxin | China / Renmin University of China | Search diversification, user behavior simulation, ranking evaluation | Su et al. (2021) — Modeling intent graph for search result diversification (35 cites) | Leads the Renmin research group (4 papers, 126 citations). Advanced modeling of user intent and behavior for relevance-oriented ranking and result diversification. |
| 5 | Avishek Anand | Germany / TU Delft, L3S Research Center | Efficient neural ranking, interpretability, data augmentation | Leonhardt et al. (2022) — Efficient neural ranking using forward indexes (12 cites) | Most prolific author in corpus (6 papers across co-authorship and coupling networks). Pioneered Fast-Forward indexes enabling CPU-only neural re-ranking with competitive effectiveness. |
| 6 | Wang Xiao | UK / University of Glasgow | Dense retrieval, pseudo-relevance feedback, ColBERT | Wang et al. (2023) — ColBERT-PRF: Semantic pseudo-relevance feedback (46 cites) | Led the most impactful dense retrieval research program in the corpus, demonstrating that contextualized PRF significantly improves dense passage and document retrieval. |
| 7 | Dou Zhicheng | China / Renmin University of China | Generative retrieval, search diversification, web search | Su et al. (2021) — Modeling intent graph for search result diversification (35 cites) | Advanced search result diversification through intent graph modeling and contributed to generative retrieval architectures bridging dense retrieval and LLM-based generation. |
| 8 | Yang Tao | USA / University of Utah | Efficient neural ranking, AutoULTR, lightweight BERT re-ranking | Yang et al. (2022) — Lightweight composite re-ranking for efficient keyword search with BERT (15 cites) | Leads a cross-institutional group (3 papers) focused on computationally efficient neural ranking — query decomposition, contextual quantization, and CPU-only re-ranking. |
| 9 | Qingyao Ai | China / Tsinghua University | Unbiased LTR, counterfactual learning, evaluation frameworks | Yang et al. (2020) — Analysis of multivariate scoring functions for AutoULTR (6 cites) | Advanced the theoretical foundations of automatic unbiased learning to rank through permutation invariance analysis and evaluation framework development. |
| 10 | Harrie Oosterhuis | Netherlands / Radboud University | Unbiased learning to rank, counterfactual evaluation | Gupta et al. (2023) — Recent advances in ULTR (5 cites) | Authored the foundational ULTR tutorial bridging theoretical counterfactual methods with practical industrial deployment. |

---

## Table 2: Top 10 Keywords by Network Centrality

| # | Keyword | Occurrences | Total Link Strength | Cluster | Definition | Relevance to Topic | Category |
|---|---------|-------------|---------------------|---------|------------|-------------------|----------|
| 1 | Information Retrieval | 5 | 7 | C1 | The science of searching for and retrieving relevant information from large collections | Core domain of the review; context-aware ranking operates within IR systems to determine result relevance and positioning | Domain |
| 2 | BERT | 4 | 7 | C3 | Bidirectional Encoder Representations from Transformers — a pre-trained language model | Dominant neural architecture for context-aware document and passage ranking, enabling semantic relevance estimation beyond lexical matching | Technology |
| 3 | Fairness | 4 | 7 | C4 | The principle that ranking algorithms should not systematically disadvantage protected groups or amplify inequalities | Central concern for positioning: biased ranking systematically disadvantages certain web resources in search results | Ethics/Quality |
| 4 | Ranking | 5 | 6 | C1 | The process of ordering documents or items by estimated relevance to a query or user | Core mechanism determining the positioning of web resources; context-aware ML directly impacts ranking decisions | Mechanism |
| 5 | Recommender Systems | 4 | 6 | C4 | Algorithms that suggest relevant items based on user preferences, behavior, and context | Major application domain where context-aware ranking affects which resources users see and in what order | Application |
| 6 | Dense Retrieval | 2 | 6 | C3 | Retrieval using dense vector representations (embeddings) rather than sparse lexical matching | Key technology for context-aware relevance estimation; embeddings capture contextual semantics beyond keywords | Technology |
| 7 | Pseudo-Relevance Feedback | 2 | 6 | C3 | Technique using top-ranked results from an initial query to expand and improve subsequent retrieval | Method for dynamically incorporating retrieval context to improve relevance and re-position results | Method |
| 8 | Query Expansion | 3 | 6 | C3 | Technique that enriches user queries with additional terms to improve retrieval | Context-aware mechanism that adapts ranking to implicit query context, directly affecting which resources surface | Method |
| 9 | Popularity Bias | 3 | 5 | C4 | Systematic tendency for recommendation and ranking algorithms to favor already-popular items | Major distortion in resource positioning: popular items dominate rankings regardless of relevance to specific contexts | Bias Type |
| 10 | Position Bias | 2 | 3 | C5 | Tendency for users to click higher-ranked results regardless of relevance | Fundamental mechanism through which ranking position distorts perceived relevance, creating feedback loops | Bias Type |

---

## 3. Co-authorship Research Groups

VOSviewer co-authorship analysis (min. 2 documents) identified 11 authors forming 3 disconnected research groups:

| Group | Core Members | Papers | Citations | Research Focus | Institution |
|-------|-------------|--------|-----------|---------------|-------------|
| C1 | Liu Y., Ma S., Zhang M., Chen J., Ma W. | 5 | 160 | Web search, click models, context-aware ranking and recommendation | Tsinghua University |
| C2 | Yang T., Ai Q., Qiao Y., Yang Y. | 3 | 25 | Efficient neural ranking, AutoULTR, lightweight BERT re-ranking | University of Utah |
| C3 | Mao J., Dou Z. | 2 | 126 | Search diversification, user behavior simulation, generative retrieval | Renmin University of China |

The 186 remaining authors (94%) appear in only 1 paper each, indicating a field characterized by small, independent research groups with limited cross-institutional collaboration — typical of rapidly evolving CS subfields where conference-driven publication incentivizes within-group co-authorship.

---

## 4. Thematic Summary

The synthesis of author contributions, keyword distributions, and co-authorship patterns reveals a field organized around the tension between relevance optimization and positioning fairness. The Tsinghua University group (Liu, Ma, Zhang, Mao) dominates the empirical study of context-aware ranking, producing foundational work on context-aware click models, passage-level relevance estimation, and user behavior simulation. The dense retrieval research program (Wang et al., ColBERT-PRF) demonstrates that contextualized embeddings and pseudo-relevance feedback substantially improve relevance estimation, directly affecting which web resources are positioned prominently. Simultaneously, the fairness-and-bias cluster — represented by high-impact surveys on popularity bias (Abdollahpouri, 125 cites; Klimashevskaia, 77 cites) — documents how context-aware algorithms can amplify unfair resource positioning when contextual signals encode popularity rather than relevance. The keyword network confirms this tension: information retrieval and ranking (Cluster 1) anchor the relevance axis, fairness and popularity bias (Cluster 4) anchor the positioning-fairness axis, and context-aware appears in Cluster 4 with the weakest link strength (TLS 1) in the entire network — quantitatively confirming that the intersection of context-awareness and fair positioning remains the field's most underexplored frontier.

---

✅ TOP 10 authors, keywords, and thematic trends successfully generated.
