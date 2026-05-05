# Bibliometric Analysis: VOSviewer Results

**Corpus:** 48 Scopus-indexed documents (2020–2025)
**Tool:** VOSviewer 1.6.20

---

## 1. Keyword Co-occurrence Analysis

### 1.1 Author Keywords

The author keyword co-occurrence map (min. 2 occurrences) identified 21 keywords organized into 5 clusters.

**Table 1: Author Keyword Co-occurrence Clusters**

| Cluster | Size | Core Keywords | Avg. Year | Thematic Interpretation |
|---------|------|--------------|-----------|------------------------|
| C1 (Red) | 5 | information retrieval (5), ranking (5), large language model (2), efficiency (2), product search (2) | 2023.4 | Core IR, Ranking, and LLM Integration |
| C2 (Green) | 4 | counterfactual LTR (2), document ranking (2), neural network (2), web search (2) | 2020.8 | Counterfactual Learning and Neural Ranking |
| C3 (Blue) | 4 | BERT (4), query expansion (3), dense retrieval (2), pseudo-relevance feedback (2) | 2022.0 | Dense Retrieval and Query Enhancement |
| C4 (Yellow) | 4 | fairness (4), recommender systems (4), popularity bias (3), context-aware (2) | 2023.0 | Fairness and Bias in Recommender Systems |
| C5 (Purple) | 4 | recommender system (3), learning to rank (2), position bias (2), cascade model (2) | 2021.8 | Position Bias and Learning to Rank |

**Table 2: Top Keywords by Network Centrality**

| Rank | Keyword | Occurrences | Links | Total Link Strength | Cluster |
|------|---------|-------------|-------|---------------------|---------|
| 1 | BERT | 4 | 4 | 7 | C3 |
| 2 | fairness | 4 | 4 | 7 | C4 |
| 3 | information retrieval | 5 | 5 | 7 | C1 |
| 4 | dense retrieval | 2 | 3 | 6 | C3 |
| 5 | pseudo-relevance feedback | 2 | 3 | 6 | C3 |
| 6 | ranking | 5 | 5 | 6 | C1 |
| 7 | recommender systems | 4 | 3 | 6 | C4 |
| 8 | query expansion | 3 | 3 | 6 | C3 |

**Cluster 1 — Core IR, Ranking, and LLM Integration (Red):** Anchored by information retrieval (5 occurrences) and ranking (5), this cluster represents the central research axis. Large language model (2 occurrences, TLS 4) is a recent addition (avg. year 2024.5), reflecting the ongoing integration of LLMs into core IR and ranking tasks. The presence of efficiency and product search indicates applied concerns with deployment viability.

**Cluster 2 — Counterfactual Learning and Neural Ranking (Green):** The earliest cluster temporally (avg. 2020.8), comprising foundational methodological work. Counterfactual learning to rank and neural network form the theoretical backbone, applied to document ranking and web search. This cluster bridges the causal inference literature and neural IR.

**Cluster 3 — Dense Retrieval and Query Enhancement (Blue):** The most internally cohesive cluster by link strength. BERT (4 occurrences, TLS 7) anchors a tightly connected sub-network with query expansion (3 occurrences, TLS 6), dense retrieval (TLS 6), and pseudo-relevance feedback (TLS 6). The co-occurrence of these terms reflects a mature research program around BERT-based dense retrieval augmented by pseudo-relevance feedback, exemplified by the ColBERT-PRF line of work (Wang et al., 2021, 2023).

**Cluster 4 — Fairness and Bias in Recommender Systems (Yellow):** The cluster with highest average citations (fairness: 87.75 avg. citations). Popularity bias (3 occurrences, avg. 70.67 citations) co-occurs strongly with fairness and recommender systems, indicating this cluster addresses the societal and ethical dimensions of ranking. Context-aware (2 occurrences, TLS 1) connects weakly to this cluster, suggesting context-awareness as a fairness mechanism is an emerging rather than established theme.

**Cluster 5 — Position Bias and Learning to Rank (Purple):** Connects position bias, learning to rank, recommender system, and cascade model around the shared concern with click-based relevance estimation. The cascade model keyword reflects the dominant user behavior model in unbiased LTR research. This cluster has the lowest average citations (7.5–30), reflecting its composition of incremental technical contributions rather than survey or high-impact conceptual papers.

### 1.2 Index Keywords

The index keyword co-occurrence map (min. 3 occurrences, Scopus-indexed) identified 36 keywords in 4 clusters, providing broader topical coverage:

| Cluster | Size | Anchor Keywords | Theme |
|---------|------|----------------|-------|
| C1 | 9 | ranking model (7), document ranking (6), large dataset (6), learning to rank (5) | Ranking Models and Learning Systems |
| C2 | 8 | embeddings (12), re-ranking (8), computational linguistics (7), semantics (7), language model (6) | Neural Embeddings and Semantic Retrieval |
| C3 | 7 | information retrieval (22), search engines (16), behavioral research (6) | Core IR Systems and User Behavior |
| C4 | 6 | recommender systems (9), contextual information (4), context-aware (3), context models (3) | Context-Aware Recommendation |

The index keyword analysis confirms the author keyword structure while revealing that contextual information (Cluster 4) forms a distinct theme when the broader Scopus vocabulary is used, validating the review's focus on context-aware ranking as a coherent subfield.

---

## 2. Co-authorship Network

Co-authorship analysis (min. 2 documents per author, min. 0 citations) identified 11 authors forming 3 research groups, representing the most productive collaboration clusters in the corpus:

**Table 3: Co-authorship Research Groups**

| Group | Members (papers) | Total Citations | Research Focus | Institution |
|-------|-----------------|-----------------|----------------|-------------|
| C1 (Red) | Liu Y. (5), Ma S. (5), Zhang M. (4), Chen J. (2), Ma W. (2) | 160 | Web search, click models, context-aware ranking | Tsinghua University |
| C2 (Green) | Yang T. (3), Ai Q. (2), Qiao Y. (2), Yang Y. (2) | 25 | Efficient neural ranking, AutoULTR | University of Utah / Industry |
| C3 (Blue) | Mao J. (4), Dou Z. (2) | 126 | Search diversification, user behavior simulation | Renmin University of China |

**Key observations:**

1. **Tsinghua University group (C1)** is the most productive and highly cited cluster (160 total citations), centered on Liu Yiqun, Ma Shaoping, and Zhang Min. This group has produced foundational work on context-aware click models (Chen et al., 2020) and context-aware recommendation (Chen et al., 2020).

2. **Renmin University group (C3)** centers on Mao Jiaxin and Dou Zhicheng, contributing to search diversification, generative retrieval, and user behavior modeling for ranking evaluation.

3. **Yang Tao group (C2)** represents the efficient neural ranking and AutoULTR research program, with work on lightweight BERT re-ranking (Yang et al., 2022) and multivariate scoring functions for unbiased LTR (Yang et al., 2020).

4. **The 186 unconnected authors** (94% of the corpus) indicate that the field is characterized by small, independent research groups with limited cross-institutional collaboration. This fragmentation is typical of rapidly evolving CS subfields where conference-driven publication incentivizes within-group rather than cross-group co-authorship.

---

## 3. Bibliographic Coupling Analysis

Bibliographic coupling analysis (min. 1 shared reference, 39 connected documents from 48 total, 5 clusters) groups papers by shared intellectual foundations.

**Table 4: Bibliographic Coupling Clusters**

| Cluster | Papers | Representative Documents | Shared Foundation |
|---------|--------|------------------------|-------------------|
| C1 | 13 | Hansen et al. (2020, 127c), Abdollahpouri et al. (2021, 125c), Dai et al. (2024, 121c), Klimashevskaia et al. (2024, 77c), Mateos & Bellogin (2025, 53c) | Recommender systems, popularity bias, fairness surveys |
| C2 | 9 | Wang et al. (2021, 60c), Wang et al. (2023, 46c), Guo et al. (2022, 30c), Zerveas et al. (2022a, 28c) | Dense retrieval, PRF, contextual re-ranking |
| C3 | 9 | Chen et al. (2020c, 47c), Kiyohara et al. (2022, 40c), Chen et al. (2021, 23c) | Click models, counterfactual LTR, off-policy evaluation |
| C4 | 6 | Su et al. (2021, 35c), Ma et al. (2022, 23c), Vuong et al. (2022, 11c) | Search diversification, context window effects, legal search |
| C5 | 2 | Zerveas et al. (2022b, 7c), Yang et al. (2022b, 4c) | Contextual embedding for efficient re-ranking (NLP-adjacent) |

**Key observations:**

1. **Cluster 1 (Recommender Fairness)**, despite being the largest by paper count, has the weakest within-cluster coupling (avg. link strength 11.3). This reflects the diversity of approaches to bias in recommendation — from user-centered evaluation (Abdollahpouri) to LLM-era surveys (Dai) to algorithmic mitigation (Chang).

2. **Cluster 2 (Dense Retrieval)** shows the strongest coupling (avg. link strength 23.2), with Wang et al. (2021, 2023) forming a dense reference core around ColBERT-based pseudo-relevance feedback. This cluster represents the most cumulative research program in the corpus.

3. **Cluster 3 (Click Models / Counterfactual LTR)** bridges the theoretical ULTR literature and applied ranking evaluation, with cross-coupling to both C1 (through bias terminology) and C2 (through retrieval evaluation methodology).

4. **Nine unconnected papers** were excluded from the coupling network (zero shared references with the main corpus). These include domain-specific applications and methodology papers using frameworks not shared by the core IR literature.

---

## 4. Temporal Trends

The average publication year per keyword cluster reveals the field's developmental trajectory:

- **2020–2021 (Foundation):** Counterfactual LTR, neural networks, web search, position bias, cascade model form the early methodological core (Clusters 2 and 5).
- **2022–2023 (Architecture Maturation):** BERT, dense retrieval, pseudo-relevance feedback, query expansion crystallize as a distinct research program (Cluster 3). Efficiency emerges as a concern within the core IR cluster.
- **2023–2024 (Fairness and LLM Inflection):** Fairness, popularity bias, and recommender systems surge in attention (Cluster 4), driven by high-impact surveys. Large language model enters the core IR cluster (Cluster 1) at avg. year 2024.5.

The overlay visualization of the keyword co-occurrence map confirms this trajectory: earlier keywords (position bias, counterfactual LTR, cascade model, neural network, web search, document ranking — all avg. 2020–2021) cluster in the right and upper-right quadrants, while recent keywords (LLM, popularity bias, fairness, context-aware, efficiency — all avg. 2023–2024.5) concentrate in the left and lower-left quadrants.

---

## 5. Research Gaps Identified Through Bibliometric Analysis

1. **Context-aware ranking—fairness disconnection:** Context-aware (Cluster 4, TLS 1) has the weakest link strength in the network, connected only to fairness through a single co-occurrence. This quantitative evidence confirms that context-awareness as a mechanism for fair or unbiased ranking is an underexplored intersection.

2. **LLM evaluation gap:** Large language model (Cluster 1, avg. 2024.5) has no direct co-occurrence link with fairness (Cluster 4), despite both being in the top 10 by TLS. The LLM-fairness intersection in ranking — how LLM-based rankers handle popularity bias, position bias, and demographic fairness — lacks keyword-level representation.

3. **Co-authorship fragmentation:** Only 11 of 197 authors (5.6%) appear in 2+ papers, with 3 disconnected research groups. Cross-institutional collaboration on context-aware ranking is virtually absent from the bibliometric record.

4. **Citation concentration:** The top 5 most-cited papers (Hansen 2020: 127, Abdollahpouri 2021: 125, Dai 2024: 121, Klimashevskaia 2024: 77, Mateos 2025: 53) account for 40% of all citations in the corpus, all in the recommender fairness cluster. Technical ranking papers (Clusters 2, 3, 5) show systematically lower citation impact despite forming the methodological core.

---

## 6. Conclusion

The VOSviewer bibliometric analysis of the 48-document corpus reveals a field organized around five thematic clusters, with dense retrieval and fairness forming the most internally cohesive research programs. The co-authorship network identifies three productive research groups (Tsinghua, Renmin, Utah/Industry) operating independently. The most significant bibliometric finding is the structural weakness of the context-aware—fairness connection (TLS 1), quantitatively confirming that the intersection of contextual ranking and algorithmic fairness remains an underexplored frontier — directly motivating this review's focus on the impact of context-aware ranking on relevance and positioning.

---

✅ Bibliometric analysis based on VOSviewer network data successfully generated.
