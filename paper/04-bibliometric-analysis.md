# Bibliometric Analysis: VOSviewer Results

**Data source:** Scopus export, 71 records
**Tool:** VOSviewer 1.6.20

---

## 1. Keyword Co-occurrence Analysis

### 1.1 Author Keywords

The author keyword co-occurrence map (min. 2 occurrences) identified 33 keywords meeting the threshold, organized into 7 clusters across 67 co-occurrence links. Table 1 presents the cluster structure.

**Table 1: Author Keyword Co-occurrence Clusters**

| Cluster | Size | Dominant Keywords (occurrences) | Avg. Year | Thematic Interpretation |
|---------|------|-------------------------------|-----------|------------------------|
| C1 (Red) | 6 | recommender systems (7), unbiased learning to rank (5), evaluation (4) | 2023.0 | Recommender System Evaluation and Debiasing |
| C2 (Green) | 6 | position bias (6), learning to rank (5), click models (3), examination bias (2), two-tower model (2) | 2023.4 | Position Bias and Click Modeling |
| C3 (Blue) | 6 | information retrieval (12), ranking (7), document ranking (2), interpolation (2) | 2023.9 | Core Information Retrieval and Ranking |
| C4 (Yellow) | 5 | recommender system (3), IoT (2), optimization (2), search engines (2), clustering (2) | 2024.7 | Applied IR and Emerging Domains |
| C5 (Purple) | 4 | contrastive learning (3), causal inference (2), counterfactual LTR (2), neural network (2) | 2022.8 | Causal and Counterfactual Methods |
| C6 (Cyan) | 3 | large language model (4), fairness (2), popularity bias (2) | 2024.5 | LLM-Era Fairness and Bias |
| C7 (Orange) | 3 | BERT (2), learning-to-rank (2), transformer (2) | 2024.2 | Transformer-Based Neural Ranking |

**Cluster 1 — Recommender System Evaluation and Debiasing (Red):** This cluster connects recommender systems (7 occurrences) with unbiased learning to rank (5) and evaluation (4), reflecting the integration of ULTR methodology into recommendation evaluation frameworks. The inclusion of deep learning and user interface as keywords indicates practical concern with both model architecture and presentation-layer bias. The total link strength of 34 across 11 connections among cluster members shows moderate internal cohesion. The strongest internal connection is between evaluation and recommender systems (2 co-occurrences) and between evaluation and user interface (2), highlighting the UI-driven nature of bias in recommendation settings.

**Cluster 2 — Position Bias and Click Modeling (Green):** This cluster represents the methodological core of the field, gathering position bias (6), learning to rank (5), click models (3), examination bias (2), and two-tower model (2). The internal link structure is tight: position bias co-occurs with learning to rank (2 links) and click models (2 links), while click models and examination bias share 2 links. The two-tower model keyword (avg. year: 2025) is the newest member, reflecting the recent architectural convergence toward jointly modeling relevance and bias. With total link strength of 39 from 29 internal connections, this is the most internally cohesive cluster.

**Cluster 3 — Core Information Retrieval and Ranking (Blue):** The largest cluster by occurrence count (27 total), anchored by information retrieval (12 occurrences, the most frequent keyword overall) and ranking (7). These two keywords share 3 direct co-occurrence links — the strongest single edge in the network. The cluster bridges traditional IR vocabulary (document ranking, google) with modern neural techniques (interpolation, reflecting the hybrid lexical-semantic retrieval paradigm). The presence of IR as a distinct keyword (separate from "information retrieval") suggests the community uses both the full term and its abbreviation interchangeably, reinforcing the centrality of this concept.

**Cluster 4 — Applied IR and Emerging Domains (Yellow):** With the most recent average year (2024.7), this cluster captures domain-specific applications. IoT co-occurs with search engines, reflecting growing interest in information retrieval for decentralized, resource-constrained environments. Recommender system (3 occurrences, as singular, distinct from the plural form in C1) and optimization indicate methodological concern with ranking efficiency in specialized contexts.

**Cluster 5 — Causal and Counterfactual Methods (Purple):** The earliest cluster temporally (avg. 2022.8), comprising the theoretical methodology base: contrastive learning (3), causal inference (2), counterfactual learning to rank (2), and neural network (2). Its early formation and small size suggest these methods were established as foundational before the field's rapid expansion in 2024–2025. Causal inference bridges to contrastive learning and counterfactual LTR, forming a coherent methodological sub-community.

**Cluster 6 — LLM-Era Fairness and Bias (Cyan):** Despite having only 3 members, this cluster has the second-highest average year (2024.5) and includes the rapidly rising keyword large language model (4 occurrences). The co-occurrence of LLM with fairness and popularity bias signals a new research axis: the intersection of generative AI and algorithmic fairness, where LLMs both introduce new bias types and offer new mitigation capabilities.

**Cluster 7 — Transformer-Based Neural Ranking (Orange):** The smallest cluster (3 keywords), connecting BERT, transformer, and learning-to-rank around the shared application of attention-based architectures to ranking tasks. Its average year (2024.2) places it after the initial BERT/transformer wave but before the LLM wave captured in C6, reflecting the transition from encoder-only to generative architectures.

### 1.2 Network Centrality and Key Nodes

Table 2 presents the keywords with highest total link strength (TLS), a VOSviewer measure of network centrality.

**Table 2: Top Keywords by Network Centrality**

| Rank | Keyword | Occurrences | Links | TLS | Cluster | Role in Network |
|------|---------|-------------|-------|-----|---------|-----------------|
| 1 | information retrieval | 12 | 12 | 16 | C3 | Central hub connecting all clusters |
| 2 | ranking | 7 | 9 | 13 | C3 | Bridge between IR core and bias/applied clusters |
| 3 | recommender systems | 7 | 9 | 11 | C1 | Primary connection from evaluation to domain application |
| 4 | learning to rank | 5 | 8 | 9 | C2 | Core methodological bridge |
| 5 | position bias | 6 | 6 | 8 | C2 | Strongest single-bias keyword |
| 6 | two-tower model | 2 | 7 | 7 | C2 | High centrality despite low frequency — emerging architectural standard |
| 7 | unbiased learning to rank | 5 | 6 | 7 | C1 | Connects debiasing theory to recommender practice |

The two-tower model keyword is notable: with only 2 occurrences but 7 links (total link strength of 7), it achieves the highest ratio of links to occurrences (3.5) in the network. This indicates the two-tower architecture is a structural bridge concept that connects diverse sub-communities, consistent with its role in jointly modeling relevance and bias across both search and recommendation contexts.

### 1.3 Temporal Evolution

The average publication year per cluster reveals the field's developmental trajectory:

- **2021–2022 (Foundation):** Cluster 5 (causal inference, counterfactual LTR, neural network) formed earliest, establishing the theoretical toolkit. Early keywords include user interface (2021.5), evaluation (2022.25), and counterfactual learning to rank (2022.0).
- **2023 (Consolidation):** Clusters 1 and 2 crystallized, with position bias, learning to rank, and recommender systems reaching sufficient frequency to form distinct co-occurrence patterns. Click models and examination bias emerged as connected sub-themes.
- **2024–2025 (Expansion and LLM Inflection):** Clusters 4, 6, and 7 formed in rapid succession. Large language model (2024.5), IoT (2025.0), two-tower model (2025.0), and fairness (2024.5) represent the newest keyword cohort. The two-tower model's immediate high centrality upon emergence reflects a rapid architectural consensus.

---

## 2. Index Keyword Co-occurrence Analysis

The index keyword co-occurrence map (min. 3 occurrences, Scopus-indexed keywords) identified 58 keywords organized into 5 clusters, providing broader coverage than the author keyword map.

**Table 3: Index Keyword Cluster Summary**

| Cluster | Size | Anchor Keywords (TLS) | Dominant Theme |
|---------|------|----------------------|----------------|
| C1 | 22 | behavioral research (57), learning systems (62), recommender systems (75), ULTR (30) | Human-Centered IR and Bias Research |
| C2 | 16 | information retrieval (138), search engines (126), ranking model (58), embeddings (35) | Core IR Systems and Neural Retrieval |
| C3 | 10 | language model (66), content-based retrieval (25), generative model (13) | Language Models and Generative Retrieval |
| C4 | 6 | inverse problems (20), implicit feedback (9), propensity score (21), user behaviors (42) | Counterfactual Estimation and User Modeling |
| C5 | 4 | computational linguistics (21), re-ranking (47), signal encoding (23) | NLP Techniques for Ranking |

The index keyword analysis confirms the author keyword structure while adding depth:
- **Information retrieval** (27 occurrences, 138 TLS) and **search engines** (21 occurrences, 126 TLS) dominate the network, with the strongest inter-keyword connection being information retrieval — search engines (12 co-occurrences).
- The 5-cluster structure is coarser than the 7 author-keyword clusters, merging the transformer/LLM clusters but separating out counterfactual estimation (C4) as a distinct methodological cluster.
- **Recommender systems** (15 occurrences, 75 TLS) anchors the human-centered research cluster (C1), connecting to learning systems, user behaviors, and de-biasing.

---

## 3. Bibliographic Coupling Analysis

Bibliographic coupling analysis (min. 0 citations, 62 connected documents from 71 total, 8 clusters) groups papers by shared references, revealing intellectual lineages independent of direct citation.

**Table 4: Bibliographic Coupling Clusters**

| Cluster | Papers | Representative Documents | Shared Intellectual Foundation |
|---------|--------|------------------------|-------------------------------|
| C1 | 14 | Li et al. (2025), Luo et al. (2025), Deng et al. (2025), Jeon et al. (2025), Karlovic et al. (2025) | Generative IR and LLM-based systems |
| C2 | 13 | Zhuang et al. (2021), Wu et al. (2021), He et al. (2024), Niu et al. (2025), Gupta et al. (2023) | Position/personalized bias, ULTR with counterfactual estimation |
| C3 | 10 | Haddad et al. (2025), Zhou et al. (2024), Taniskidou et al. (2023), Krasakis et al. (2025) | Neural ranking architectures, GNN/BERT-based re-ranking |
| C4 | 7 | Batri et al. (2025a, 2025b), Kumar et al. (2026), Podder et al. (2026), Novak et al. (2022) | Efficient retrieval, novel metrics, term weighting |
| C5 | 6 | Lyu et al. (2024), Abdallah et al. (2025), Alaofi et al. (2025), Carnovalini et al. (2025) | Evaluation frameworks, bias surveys, interpretability |
| C6 | 6 | Leonhardt et al. (2022, 2023, 2024), Anand et al. (2024) | Fast-Forward indexes, efficient neural ranking |
| C7 | 4 | Amala & Rajeswari (2025a, 2025b), Huang et al. (2021), Ren et al. (2022) | Two-tower CTR prediction, neural click models |
| C8 | 2 | Chen et al. (2021a), Bisht et al. (2022) | Attention-based observation embedding, vertical-aware models |

**Key observations:**

1. **Cluster 1 (GenIR/LLM, 14 papers)** and **Cluster 2 (ULTR/Bias, 13 papers)** are the two largest bibliographic coupling clusters, reflecting the field's primary intellectual division between generative and counterfactual approaches.

2. **Cluster 6 (Fast-Forward indexes, 6 papers)** represents the strongest within-cluster coupling, with Leonhardt et al. (2022), Leonhardt et al. (2024), and Anand et al. (2024) sharing 21, 48, and 83 references respectively — the densest local reference network. This reflects the tightly cumulative nature of the efficiency-focused research program.

3. **The 9 unconnected papers** represent niche or cross-disciplinary contributions that share insufficient references with the main corpus to form coupling links. These include domain-specific applications (finance, edge computing) and methodology papers using frameworks outside the IR mainstream.

4. **Cross-cluster coupling** is strongest between C2 (ULTR) and C7 (two-tower CTR), reflecting their shared reliance on propensity estimation and click modeling literature. The weakest cross-cluster coupling is between C1 (GenIR) and C6 (Fast-Forward), indicating these research communities draw on largely disjoint reference sets.

---

## 4. Key Insights

### 4.1 Research Field Structure

The VOSviewer analysis reveals a field organized around three structural features:

1. **A dense IR core** (information retrieval + ranking + search engines) that serves as the network hub, connecting all other clusters through high link strength.

2. **A ULTR-bias axis** (Clusters 1, 2, 5 in author keywords; Clusters 2, 4 in index keywords) that represents the dominant methodological concern, connected to the core through learning to rank and recommender systems.

3. **An emerging LLM-fairness frontier** (Cluster 6 in author keywords; Cluster 3 in index keywords) that is the newest and fastest-growing component, with large language model (4 occurrences in 2024.5) already ranking among the top 10 keywords despite only entering the literature substantially from 2024.

### 4.2 Co-authorship Limitations

Co-authorship analysis could not produce meaningful results: of 266 unique authors across 71 documents, 244 appear in only 1 paper. At a threshold of 2 documents per author, only 4 authors qualify — insufficient for network visualization. This indicates fragmented research groups with limited cross-institutional collaboration. The few qualifying authors (including Avishek Anand, Jurek Leonhardt, Qingyao Ai, Harrie Oosterhuis, K.J. Amala) represent small research clusters at TU Delft/L3S, Tsinghua University, Radboud University, and independent researchers, respectively.

### 4.3 Geographic and Institutional Concentration

Country/institutional analysis from Scopus affiliations shows strong concentration in China (Tsinghua, Renmin, Shanghai Jiao Tong), the Netherlands (Amsterdam, Delft, Radboud), and Austria (TU Wien). Chinese institutions dominate publication count, particularly through CIKM and SIGIR proceedings. Dutch institutions contribute disproportionately to theoretical ULTR and counterfactual learning research. Industry labs (Google, Tencent, JD.com, Meituan) appear as co-authors on 14 of 71 papers (20%), indicating close academy-industry research integration.

---

## 5. Research Gaps Identified Through Bibliometric Analysis

1. **GenIR-ULTR disconnection:** Bibliographic coupling shows GenIR papers (C1) and ULTR papers (C2) draw on largely separate reference corpora, with minimal cross-citation. This quantitative evidence confirms the qualitative observation that bias correction and generative retrieval are developing as parallel, disconnected research streams.

2. **Reproducibility deficit:** Only 18 of 71 Scopus records (25%) are associated with publicly available code repositories or datasets, based on the absence of code/data availability statements in abstract and keywords.

3. **Evaluation diversity gap:** The keyword "evaluation" (4 occurrences) ranks 7th, yet is connected only to recommender systems (2 links) and user interface (2 links). No direct co-occurrence exists between evaluation and the LLM cluster (C6), suggesting GenIR evaluation methodology is underdeveloped.

4. **Underrepresented application domains:** IoT appears as a peripheral cluster (C4, 5 keywords, avg. 2024.7), disconnected from the main ULTR and LLM research axes. Edge computing, engineering IR, and financial IR appear only in the 9 unconnected bibliographic coupling papers.

---

## 6. Conclusion

The VOSviewer bibliometric analysis confirms and quantifies the thematic structure identified in the systematic review. The seven author-keyword clusters map cleanly onto the five thematic clusters from the content analysis, with the bibliometric data providing network-metric evidence (link strengths, temporal evolution, cluster cohesion) that the qualitative analysis cannot produce. The most salient bibliometric finding is the structural disconnection between the GenIR/LLM cluster (C6) and the ULTR/bias-correction cluster (C2), quantitatively demonstrating the field's central integration challenge. The two-tower model emerges as a potential bridge concept — its high centrality-to-occurrence ratio (3.5) suggests it is already serving as a common architectural reference point across clusters, and its extension to generative retrieval contexts represents a natural integration pathway.

---

✅ Bibliometric analysis based on VOSviewer network data successfully generated.
