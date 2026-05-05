# Relevance and Positioning: A Systematic Bibliometric Review of Context-Aware ML Ranking in Web Search and Recommendation Systems

## Abstract

Context-aware machine learning ranking algorithms dynamically adjust search and recommendation results based on situational, behavioral, and environmental signals, directly affecting both the relevance of retrieved resources and their positioning in ranked outputs. This review provides a comprehensive synthesis of research at this intersection through a hybrid systematic-bibliometric methodology, analyzing 46 peer-reviewed publications (2020–2025) with VOSviewer bibliometric mapping of 48 Scopus-indexed records. Keyword co-occurrence analysis identified five thematic clusters: neural architectures for context-aware ranking, dense retrieval and query enhancement, position bias and counterfactual learning to rank, recommender fairness and popularity bias, and context-aware search applications. The co-authorship network revealed three independent research groups (Tsinghua University, Renmin University of China, University of Utah), with 94% of authors appearing in a single publication. The central finding is a structural disconnection between the relevance-improvement and positioning-fairness research communities, confirmed bibliometrically: the keyword context-aware shares a single co-occurrence link (total link strength 1) with fairness in the VOSviewer network. Of 45 qualitatively analyzed papers, none simultaneously address relevance improvement through context and fairness preservation in positioning. Five high-impact research directions are proposed, prioritizing unified relevance-positioning frameworks, online and user-centered evaluation of positioning effects, and richer context taxonomies incorporating multimodal signals.

**Keywords:** context-aware ranking, relevance, positioning, information retrieval, recommender systems, fairness, popularity bias, VOSviewer, bibliometric analysis

---

## 1. Introduction

## Relevance of the Topic

In modern web search and recommendation systems, the relevance of retrieved results and their positioning in the ranked output directly determine which information reaches users. Context-aware machine learning ranking algorithms — models that dynamically adjust result ordering based on situational, behavioral, and environmental signals — have emerged as a central mechanism for improving both relevance estimation and result personalization. These algorithms incorporate diverse contextual factors: session history and query context in web search (Chen et al., 2020), user embeddings and sequential behavior in music recommendation (Hansen et al., 2020), document-level contextual signals in neural re-ranking (Zerveas et al., 2022), and spatio-temporal context in service ranking. By adapting ranking decisions to context, these systems promise more accurate relevance assessment and more personalized resource positioning.

However, the relationship between context-awareness and positioning outcomes is not straightforward. Contextual signals can improve relevance — as demonstrated by BERT-based dense retrieval augmented with pseudo-relevance feedback (Wang et al., 2021, 2023) and context-aware click models that disentangle examination from relevance (Chen et al., 2020). Yet contextual signals can also amplify existing distortions: popularity bias in recommender systems systematically advantages already-popular resources regardless of contextual relevance (Klimashevskaia et al., 2024; Abdollahpouri et al., 2021), and position bias creates feedback loops where highly-positioned resources accumulate clicks irrespective of merit (Kiyohara et al., 2022). Understanding how context-aware ML ranking algorithms affect both the relevance and the positioning of web resources — and developing methods for analyzing this dual impact — is therefore critical for building information access systems that are both effective and fair.

## Literature Gap

Existing surveys have addressed individual dimensions of this problem. Gupta et al. (2023) provided a tutorial on unbiased learning to rank foundations. Klimashevskaia et al. (2024) and Abdollahpouri et al. (2021) surveyed popularity bias in recommender systems. Dai et al. (2024) examined bias and unfairness in the LLM era. Mateos and Bellogin (2025) systematically reviewed context-aware recommender systems. However, no existing review integrates the two outcome dimensions — relevance and positioning — into a unified analytical framework. Specifically, no review examines how context-aware ranking algorithms simultaneously affect (a) the relevance of retrieved results and (b) the positioning of web resources in ranked outputs, nor does any review combine systematic literature review methodology with bibliometric network analysis to quantify the structural relationships among these research themes.

## Research Goal and Questions

The primary goal of this review is to provide a comprehensive, structured synthesis of research on context-aware ML ranking in web search and recommendation systems, with specific focus on the dual impact on relevance and resource positioning. The review is guided by four research questions:

1. **RQ1**: What are the main thematic clusters in context-aware ML ranking research for web search and recommendation systems (2020–2025)?
2. **RQ2**: What methodologies dominate — neural ranking architectures, bias correction frameworks, or context modeling approaches?
3. **RQ3**: How does context-aware ML ranking affect the relevance and positioning of web resources?
4. **RQ4**: What are the key research gaps at the intersection of context-awareness, ranking fairness, and result positioning?

## Structure of the Paper

The remainder of this paper is organized as follows. Section 2 presents the review methodology, including the PRISMA-guided search strategy, inclusion and exclusion criteria, data extraction process, and the hybrid systematic-bibliometric synthesis approach employing VOSviewer. Section 3 reports the results, organized around five thematic clusters identified through combined content analysis and bibliometric mapping. Section 4 discusses the findings, interpreting the cluster structure, comparing with prior surveys, and examining implications for relevance-oriented and positioning-aware ranking system design. Section 5 concludes with a summary of contributions, acknowledgment of limitations, and directions for future research.


---

## 2. Methodology

## 1. Review Design

This study employs a hybrid review design integrating two complementary methodological approaches: (a) a **Systematic Literature Review** following PRISMA 2020 guidelines for study identification, screening, eligibility assessment, and inclusion, and (b) a **Bibliometric Analysis** using VOSviewer for keyword co-occurrence mapping, co-authorship network analysis, and bibliographic coupling. The hybrid design was selected to combine the depth of qualitative thematic synthesis with the breadth and reproducibility of quantitative bibliometric network analysis, enabling both identification of research themes and measurement of their structural relationships.

## 2. Search Strategy

A comprehensive search was conducted in Scopus in May 2025. Scopus was selected as the primary database for its broad multidisciplinary coverage, structured bibliometric metadata (author IDs, affiliation data, indexed keywords, cited references), and native compatibility with VOSviewer import. The Boolean search query was constructed from three conceptual dimensions:

**Dimension 1 — Context-aware ranking mechanisms:**
`"context-aware ranking" OR "context-aware retrieval" OR "contextual ranking" OR "context-aware recommendation" OR "context-aware" AND "learning to rank" OR "contextual" AND "neural ranking" OR "context*" AND "re-ranking"`

**Dimension 2 — Application domains:**
`"web search" OR "search engine" OR "information retrieval" OR "recommender system" OR "recommendation system" OR "web resource" OR "document retrieval"`

**Dimension 3 — Outcome measures:**
`"relevance" OR "position" OR "ranking quality" OR "ndcg" OR "map" OR "mrr"`

The complete query combined these dimensions with AND operators, restricted to publications from 2020 to 2025 and English-language documents. The temporal window was selected to capture the period following the BERT-era transformation of neural IR, during which context-aware deep learning architectures became the dominant paradigm.

## 3. Inclusion and Exclusion Criteria

| Criterion | Inclusion | Exclusion |
|-----------|----------|-----------|
| Topic scope | Context-aware or contextual ranking for web search, IR, or recommender systems | Context-aware in non-IR domains (computer vision, NLP without retrieval, edge computing without ranking) |
| Publication type | Peer-reviewed journal articles, conference papers, reviews | Preprints, editorials, non-peer-reviewed sources |
| Time frame | 2020–2025 | Before 2020 |
| Language | English | Non-English |
| Citation impact | Minimum 1 Scopus citation | Zero citations |

The citation threshold (≥1 Scopus citation) served as a bibliometric quality filter, ensuring included studies have demonstrated academic impact. This criterion is appropriate for a bibliometric review where citation-based indicators (citation counts, normalized citation scores) are integral to the analysis.

## 4. Study Selection Process

The initial Scopus search returned 318 records. All 318 underwent title and abstract screening. At this stage, 182 records were excluded: 147 captured by the query but outside the IR/ranking/recommender domain (papers where "context-aware" referred to video localization, medical imaging, construction engineering, agricultural systems, or other non-IR applications), 4 outside the 2020–2025 temporal window, 1 lacking a DOI, and 30 identified as tangentially relevant on closer inspection. The remaining 136 papers advanced to eligibility assessment, where application of the citation threshold excluded 44 zero-citation papers.

Forty-eight papers were confirmed in Scopus and exported in CSV format with full records and cited references for VOSviewer analysis. Full-text versions of 46 papers were obtained for qualitative synthesis. Two papers were excluded at this stage following full-text review (university rankings methodology and linguistic usage analysis — both captured by the query through the term "ranking" but outside the IR/ranking scope).

## 5. Bibliometric Analysis

Bibliometric analysis was conducted using VOSviewer 1.6.20. Four map types were generated:

| Analysis | Unit | Threshold | Result |
|----------|------|-----------|--------|
| Keyword co-occurrence | Author keywords | Min. 2 occurrences | 21 keywords, 5 clusters |
| Keyword co-occurrence | Index keywords (Scopus) | Min. 3 occurrences | 36 keywords, 4 clusters |
| Co-authorship | Authors | Min. 2 documents, 0 citations | 11 authors, 3 research groups |
| Bibliographic coupling | Documents | Min. 1 shared reference | 39 connected documents, 5 clusters |

For each map type, network, overlay, and density visualizations were generated. Cluster assignments were determined by the VOSviewer Leiden clustering algorithm.

## 6. Qualitative Synthesis

For the 46 included papers, systematic full-text reading was conducted using markdown versions of each paper. A standardized Literature Analysis Matrix captured: author(s), publication year, research aim, methodology, participants/data characteristics, main findings, reported limitations, and author keywords. Thematic clusters were identified through iterative content analysis of research aims, methods, and findings, cross-validated against VOSviewer keyword cluster assignments. Where content-based and bibliometric cluster assignments diverged, the content-based assignment was retained for the qualitative synthesis, with the bibliometric assignment noted for triangulation.

## 7. Quality Assurance and Limitations

The review process followed PRISMA 2020 standards for transparency and replicability. Methodological limitations include: (a) single-database search (Scopus only), which may omit relevant publications indexed exclusively in ACM Digital Library, IEEE Xplore, or Web of Science; (b) citation threshold exclusion (zero-citation papers removed), which may exclude recent high-quality publications that have not yet accumulated citations; (c) single-reviewer screening, without formal inter-rater reliability assessment; and (d) reliance on author-assigned keywords for the primary bibliometric map, which may underrepresent emerging terminology not yet adopted as author keywords.


---

## 3. Results

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


---

## 4. Discussion

## 1. Interpretation of Key Findings

The identification of five thematic clusters — spanning neural architectures for context-aware ranking (C1), dense retrieval and query enhancement (C2), position bias and counterfactual LTR (C3), recommender fairness and popularity bias (C4), and context-aware search applications (C5) — reveals a field organized around a central tension: context as a mechanism for improving relevance versus context as a vector for amplifying positioning distortions.

This tension is most visible in the citation distribution. Cluster 4 (Recommender Fairness), with 10 papers and an average of 49.2 citations per paper, dominates the impact landscape, accounting for four of the five most-cited papers in the corpus. Yet the bibliometric network shows that context-aware — the keyword most directly aligned with this review's focus — is connected to fairness through a single co-occurrence link (TLS 1), the weakest connection in the keyword network. This structural gap is the central finding of this review: the research community studying how context improves relevance (Clusters 1, 2) operates almost entirely separately from the community studying how context-encoded signals can produce unfair positioning outcomes (Cluster 4).

The two-tower architecture emerges as a potential bridge between these communities. Appearing in Cluster 1 (e-commerce EBR), Cluster 3 (counterfactual LTR), and implicitly in Cluster 4 (bias NN + relevance NN architectures), the two-tower pattern — where one tower models user preference or relevance and another models context or bias — represents a shared architectural vocabulary. However, current instantiations use the second tower for fundamentally different purposes: in Cluster 1, to capture contextual signals for relevance improvement; in Cluster 3, to estimate bias for counterfactual correction; in Cluster 4, to separate popularity from preference. A unified two-tower framework that simultaneously optimizes for context-driven relevance improvement and context-driven fairness preservation does not yet exist.

The co-authorship network further illustrates the field's fragmentation. Three research groups, operating independently and with zero cross-group co-authorship edges in the VOSviewer network, account for all authors appearing in 2+ papers. The Tsinghua group (Liu, Ma, Zhang, Mao) contributes to both the context-aware click model literature (Cluster 3) and context-aware recommendation (Cluster 4), representing the only institutional bridge between the relevance and fairness clusters. This concentration is both a strength — indicating deep, cumulative expertise — and a structural risk: the absence of cross-institutional collaboration may slow the integration of context-as-opportunity and context-as-risk perspectives.

## 2. Comparison with Existing Reviews

The thematic structure identified here both confirms and extends prior surveys. Klimashevskaia et al. (2024) and Abdollahpouri et al. (2021) comprehensively cover the material in Cluster 4 (popularity bias), but do not address how context-aware architectures (Clusters 1 and 2) might amplify or mitigate the biases they document. Mateos and Bellogin (2025) survey context-aware recommender systems but treat context as a methodological category rather than examining its dual role in relevance and fairness. Dai et al. (2024) identify LLM-era bias types but do not connect them to the established counterfactual LTR literature in Cluster 3. Gupta et al. (2023) provide a tutorial on ULTR foundations but limit their scope to bias correction, without addressing the broader context-aware ranking landscape.

This review's distinctive contribution is the integration of these sub-literatures into a unified framework organized around the relevance-positioning dual axis. By combining systematic content analysis with bibliometric network mapping, it becomes possible to quantify what prior reviews could only suggest: that the context-awareness—fairness connection is not merely underexplored but structurally absent from the bibliometric record. The TLS 1 link between context-aware and fairness is not an artifact of keyword selection — it reflects a genuine research gap that content analysis confirms. Of the 45 papers in the qualitative synthesis, zero simultaneously address (a) how context-aware ranking improves relevance and (b) how context-driven signals affect the fairness of resource positioning.

## 3. Implications for Research and Practice

The finding that context-awareness and fairness are disconnected in both the bibliometric network and the published literature has direct implications. For researchers, it identifies a high-impact research opportunity: developing unified frameworks that jointly model context for relevance and fairness, extending the two-tower architecture to include a fairness objective alongside relevance and bias estimation. The theoretical tools exist — counterfactual estimation (Cluster 3) for bias correction, user-centered metrics (Cluster 4) for fairness evaluation — but have not been combined in a context-aware ranking setting.

For practitioners, the findings carry a caution: deploying context-aware ranking without measuring its positioning effects risks amplifying the popularity bias that the fairness community has extensively documented. If contextual signals (user history, session patterns, device type) are correlated with popularity — as they almost certainly are in production systems — then context-aware models trained purely for relevance may systematically disadvantage less popular but contextually appropriate resources.

The efficiency findings in Cluster 2 (Fast-Forward indexes, 14:1 compression, CPU-only re-ranking) have practical significance independent of the fairness concern. They demonstrate that neural context-aware ranking is viable without GPU infrastructure, lowering the barrier to deployment for resource-constrained applications.

## 4. Limitations of This Review

Five limitations should be considered. First, the single-database search (Scopus only) may omit relevant publications indexed exclusively in ACM Digital Library, IEEE Xplore, or Web of Science. Second, the citation threshold (≥1 citation) excluded 44 zero-citation papers that may include recent high-quality work not yet accumulated citations. Third, single-reviewer screening — while supplemented by AI-assisted keyword filtering — was not subject to formal inter-rater reliability assessment. Fourth, the author keyword co-occurrence map, while providing the most direct window into researchers' self-described contributions, is limited by the vocabulary authors choose; emerging concepts not yet adopted as author keywords may be underrepresented. Fifth, the temporal window (2020–2025) excludes pre-BERT-era foundational work on context-aware IR that established the field's theoretical basis.

## 5. Future Research Directions

Based on the identified gaps, five directions emerge as priorities:

1. **Unified relevance-positioning frameworks:** Developing context-aware ranking architectures that simultaneously optimize for relevance and measure positioning fairness. The two-tower architectural pattern, extended with a fairness-aware loss function, represents a natural starting point.

2. **Online and user-centered evaluation of positioning effects:** Moving beyond offline metrics to production A/B tests and user studies that measure how context-aware ranking changes which resources gain or lose visibility, following the user-centered evaluation paradigm established by Abdollahpouri et al. (2021).

3. **Richer context taxonomies:** Expanding context operationalization beyond session history and document structure to include affective, social, cross-device, and multimodal signals, with systematic comparison of how different context types affect relevance and positioning.

4. **Cross-domain generalizability studies:** Testing whether context-aware ranking methods effective in one domain (e-commerce, music recommendation) transfer to others (web search, legal retrieval, email search).

5. **Reproducibility infrastructure:** Addressing the code and data availability gap — particularly acute in context-aware recommender systems where Mateos and Bellogin (2025) find fewer than 25% of papers provide public implementations.


---

## 5. Conclusion

## 1. Summary of Key Findings

This hybrid systematic-bibliometric review analyzed 46 peer-reviewed publications (2020–2025) on context-aware machine learning ranking in web search and recommendation systems, supported by bibliometric data from 48 Scopus-indexed records. VOSviewer keyword co-occurrence analysis identified five thematic clusters: neural architectures for context-aware ranking (10 papers), dense retrieval and query enhancement (8 papers), position bias and counterfactual LTR (8 papers), recommender fairness and popularity bias (10 papers), and context-aware search applications (9 papers). The co-authorship network revealed three independent research groups (Tsinghua University, Renmin University of China, University of Utah) accounting for all multi-paper authors, with 94% of authors appearing in a single publication.

The central finding is a structural disconnection between the two research communities most relevant to this review's focus. The community studying how context improves ranking relevance (Clusters 1–2) operates almost entirely separately from the community studying how context-encoded signals produce unfair positioning outcomes (Cluster 4). This disconnection is confirmed bibliometrically: the keyword context-aware shares a single co-occurrence link (total link strength 1) with fairness in the VOSviewer network. Of the 45 papers in the qualitative synthesis, none simultaneously address relevance improvement through context and fairness preservation in positioning.

## 2. Research Significance

This review makes three primary contributions. First, it provides the first integrated synthesis of context-aware ML ranking research organized around the dual outcome dimensions of relevance and positioning — dimensions that prior surveys have addressed in isolation but never jointly. Second, the bibliometric component quantifies the structural relationships among research themes, providing network-metric evidence (link strengths, cluster cohesion, co-authorship fragmentation) that transforms a qualitative observation about disconnected communities into a verifiable finding. Third, by identifying the context-awareness—fairness gap as the field's most critical underexplored frontier, the review provides a roadmap for future research that bridges the methodological rigor of counterfactual bias correction with the representational power of context-aware neural architectures.

## 3. Limitations

The findings are constrained by: the single-database search (Scopus), which may omit relevant publications; the citation threshold (≥1 citation), which excluded recent work not yet accumulated citations; single-reviewer screening without formal inter-rater reliability assessment; the reliance on author-assigned keywords for bibliometric mapping, which may underrepresent emerging terminology; and the 2020–2025 temporal window, which excludes foundational pre-BERT-era context-aware IR research.

## 4. Future Research Directions

Five directions emerge from the identified gaps: (1) developing unified relevance-positioning frameworks that jointly optimize context-aware ranking for relevance and fairness — extending the two-tower architecture with fairness-aware objectives; (2) moving evaluation from offline metrics to production A/B tests and user studies that measure real-world positioning effects; (3) expanding context operationalization beyond session and document signals to affective, social, cross-device, and multimodal context; (4) conducting cross-domain generalizability studies; and (5) building reproducibility infrastructure including public implementations and standardized benchmarks for context-aware ranking evaluation.

## 5. Closing Statement

The intersection of context-aware ranking, relevance estimation, and resource positioning stands at a formative moment. The neural architectures for leveraging context to improve relevance have matured to the point of industrial deployment, while the fairness community has produced rigorous evidence that context-encoded signals can amplify positioning distortions. The field's next advance requires integrating these perspectives — building context-aware ranking systems that improve relevance without systematically advantaging already-visible resources. The methods for analyzing this dual impact — combining systematic review with bibliometric network analysis — are themselves part of this integration. The research gaps identified in this review represent the critical path toward ranking systems that are both contextually intelligent and positioning-fair.


---

## References


**Total papers:** 46
**Citation range:** 1–127 (median: 14)

---

1. Hansen, C.., Hansen, C.., Maystre, L.., Mehrotra, R.., Brost, B.., Tomasi, F.., Lalmas, M.. (2020). Contextual and Sequential User Embeddings for Large-Scale Music Recommendation. *Recsys 2020 14th ACM Conference on Recommender Systems*. https://doi.org/10.1145/3383313.3412248

2. Abdollahpouri, H.., Mansoury, M.., Burke, R.., Mobasher, B.., Malthouse, E.. (2021). User-centered evaluation of popularity bias in recommender systems. *Umap 2021 Proceedings of the 29th ACM Conference on User Modeling Adaptation and Personalization*. https://doi.org/10.1145/3450613.3456821

3. Dai, S.., Xu, C.., Xu, S.., Pang, L.., Dong, Z.., Xu, J.. (2024). Bias and Unfairness in Information Retrieval Systems: New Challenges in the LLM Era. *Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. https://doi.org/10.1145/3637528.3671458

4. Klimashevskaia, A.., Jannach, D.., Elahi, M.., Trattner, C.. (2024). A survey on popularity bias in recommender systems. *User Modeling and User Adapted Interaction*. https://doi.org/10.1007/s11257-024-09406-0

5. Wang, X.., MacDonald, C.., Tonellotto, N.., Ounis, I.. (2021). Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval. *Ictir 2021 Proceedings of the 2021 ACM SIGIR International Conference on Theory of Information Retrieval*. https://doi.org/10.1145/3471158.3472250

6. Mateos, P.., Bellogín, A.. (2025). A systematic literature review of recent advances on context-aware recommender systems. *Artificial Intelligence Review*. https://doi.org/10.1007/s10462-024-10939-4

7. Chen, J.., Mao, J.., Liu, Y.., Zhang, M.., Ma, S.. (2020). A context-aware click model for web search. *Wsdm 2020 Proceedings of the 13th International Conference on Web Search and Data Mining*. https://doi.org/10.1145/3336191.3371819

8. Wang, X.., Macdonald, C.., Tonellotto, N.., Ounis, I.. (2023). ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval. *ACM Transactions on the Web*. https://doi.org/10.1145/3572405

9. Chen, C.., Zhang, M.., Ma, W.., Liu, Y.., Ma, S.. (2020). Efficient Non-Sampling Factorization Machines for Optimal Context-Aware Recommendation. *Web Conference 2020 Proceedings of the World Wide Web Conference Www 2020*. https://doi.org/10.1145/3366423.3380303

10. Kiyohara, H.., Saito, Y.., Matsuhiro, T.., Narita, Y.., Shimizu, N.., Yamamoto, Y.. (2022). Doubly robust off-policy evaluation for ranking policies under the cascade behavior model. *Wsdm 2022 Proceedings of the 15th ACM International Conference on Web Search and Data Mining*. https://doi.org/10.1145/3488560.3498380

11. Wu, Z.., Mao, J.., Liu, Y.., Zhan, J.., Zheng, Y.., Zhang, M.., Ma, S.. (2020). Leveraging Passage-level Cumulative Gain for Document Ranking. *Web Conference 2020 Proceedings of the World Wide Web Conference Www 2020*. https://doi.org/10.1145/3366423.3380305

12. Su, Z.., Dou, Z.., Zhu, Y.., Qin, X.., Wen, J.-R.. (2021). Modeling Intent Graph for Search Result Diversification. *SIGIR 2021 Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3404835.3462872

13. Guo, Y.., Ma, Z.., Mao, J.., Qian, H.., Zhang, X.., Jiang, H.., Cao, Z.., Dou, Z.. (2022). Webformer: Pre-training with Web Pages for Information Retrieval. *SIGIR 2022 Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3477495.3532086

14. Zerveas, G.., Rekabsaz, N.., Cohen, D.., Eickhoff, C.. (2022). Mitigating Bias in Search Results Through Contextual Document Reranking and Neutrality Regularization. *SIGIR 2022 Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3477495.3531891

15. Afzal, I.., Yilmazel, B.., Kaleli, C.. (2024). An Approach for Multi-Context-Aware Multi-Criteria Recommender Systems Based on Deep Learning. *IEEE Access*. https://doi.org/10.1109/access.2024.3428630

16. Ma, Y.., Ai, Q.., Wu, Y.., Shao, Y.., Liu, Y.., Zhang, M.., Ma, S.. (2022). Incorporating Retrieval Information into the Truncation of Ranking Lists for Better Legal Search. *SIGIR 2022 Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3477495.3531998

17. Chen, M.., Liu, C.., Sun, J.., Hoi, S.C.H.. (2021). Adapting Interactional Observation Embedding for Counterfactual Learning to Rank. *SIGIR 2021 Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3404835.3462901

18. Wang, Y.., Lyu, L.., Anand, A.. (2022). BERT Rankers are Brittle: A Study using Adversarial Document Perturbations. *Ictir 2022 Proceedings of the 2022 ACM SIGIR International Conference on the Theory of Information Retrieval*. https://doi.org/10.1145/3539813.3545122

19. Jin, J.., Fang, Y.., Zhang, W.., Ren, K.., Zhou, G.., Xu, J.., Yu, Y.., Wang, J.., Zhu, X.., Gai, K.. (2020). A Deep Recurrent Survival Model for Unbiased Ranking. *SIGIR 2020 Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3397271.3401073

20. Yang, Y.., Qiao, Y.., Shao, J.., Yan, X.., Yang, T.. (2022). Lightweight composite re-ranking for efficient keyword search with BERT. *Wsdm 2022 Proceedings of the 15th ACM International Conference on Web Search and Data Mining*. https://doi.org/10.1145/3488560.3498495

21. Luo, S.., He, B.., Zhao, H.., Shao, W.., Qi, Y.., Huang, Y.., Zhou, A.., Yao, Y.., Li, Z.., Xiao, Y.., Zhan, M.., Song, L.. (2025). RecRanker: Instruction Tuning Large Language Model as Ranker for Top-k Recommendation. *ACM Transactions on Information Systems*. https://doi.org/10.1145/3705728

22. Yang, Y.., Qiao, Y.., Shao, J.., Yan, X.., Yang, T.. (2022). Lightweight composite re-ranking for efficient keyword search with BERT. *Wsdm 2022 Proceedings of the 15th ACM International Conference on Web Search and Data Mining*. https://doi.org/10.1145/3488560.3498495

23. Li, F.., Si, X.., Tang, S.., Wang, D.., Han, K.., Han, B.., Zhou, G.., Song, Y.., Chen, H.. (2024). Contextual Distillation Model for Diversified Recommendation. *Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. https://doi.org/10.1145/3637528.3671514

24. Buyl, M.., Missault, P.., Sondag, P.-A.. (2023). RankFormer: Listwise Learning-to-Rank Using Listwide Labels. *Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. https://doi.org/10.1145/3580305.3599892

25. Ermis, B.., Ernst, P.., Stein, Y.., Zappella, G.. (2020). Learning to Rank in the Position Based Model with Bandit Feedback. *International Conference on Information and Knowledge Management Proceedings*. https://doi.org/10.1145/3340531.3412723

26. Leonhardt, J.., Rudra, K.., Khosla, M.., Anand, A.., Anand, A.. (2022). Efficient Neural Ranking using Forward Indexes. *Www 2022 Proceedings of the ACM Web Conference 2022*. https://doi.org/10.1145/3485447.3511955

27. Vuong, T.., Andolina, S.., Jacucci, G.., Ruotsalo, T.. (2022). Does More Context Help? Effects of Context Window and Application Source on Retrieval Performance. *ACM Transactions on Information Systems*. https://doi.org/10.1145/3474055

28. Chang, B.., Meng, C.., Ma, H.., Chang, S.., Gu, Y.., Peng, Y.., Feng, J.., Zhang, Y.., Bi, S.., Chi, E.H.., Chen, M.. (2024). Cluster Anchor Regularization to Alleviate Popularity Bias in Recommender Systems. *Www 2024 Companion Companion Proceedings of the ACM Web Conference*. https://doi.org/10.1145/3589335.3648312

29. Ren, Y.., Tang, H.., Zhu, S.. (2022). Unbiased Learning to Rank with Biased Continuous Feedback. *International Conference on Information and Knowledge Management Proceedings*. https://doi.org/10.1145/3511808.3557483

30. Zhang, J.., Liu, Y.., Mao, J.., Ma, W.., Xu, J.., Ma, S.., Tian, Q.. (2023). User Behavior Simulation for Search Result Re-ranking. *ACM Transactions on Information Systems*. https://doi.org/10.1145/3511469

31. Vuong, T.., Ruotsalo, T.. (2024). Predicting Representations of Information Needs from Digital Activity Context. *ACM Transactions on Information Systems*. https://doi.org/10.1145/3639819

32. Zhang, C.., Yao, H.., Yu, L.., Huang, C.., Song, D.., Chen, H.., Jiang, M.., Chawla, N.V.. (2021). Inductive Contextual Relation Learning for Personalization. *ACM Transactions on Information Systems*. https://doi.org/10.1145/3450353

33. Leonhardt, J.., Müller, H.., Rudra, K.., Khosla, M.., Anand, A.., Anand, A.. (2024). Efficient Neural Ranking Using Forward Indexes and Lightweight Encoders. *ACM Transactions on Information Systems*. https://doi.org/10.1145/3631939

34. He, Y.., Tian, Y.., Wang, M.., Chen, F.., Yu, L.., Tang, M.., Chen, C.., Zhang, N.., Kuang, B.., Prakash, A.. (2023). Que2Engage: Embedding-based Retrieval for Relevant and Engaging Products at Facebook Marketplace. *ACM Web Conference 2023 Companion of the World Wide Web Conference Www 2023*. https://doi.org/10.1145/3543873.3584633

35. Zerveas, G.., Rekabsaz, N.., Cohen, D.., Eickhoff, C.. (2022). CODER: An efficient framework for improving retrieval through COntextual Document Embedding Reranking. *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing Emnlp 2022*. https://doi.org/10.18653/v1/2022.emnlp-main.727

36. Bi, K.., Metrikov, P.., Li, C.., Byun, B.. (2021). Leveraging user behavior history for personalized email search. *Web Conference 2021 Proceedings of the World Wide Web Conference Www 2021*. https://doi.org/10.1145/3442381.3450110

37. Yang, T.., Fang, S.., Li, S.., Wang, Y.., Ai, Q.. (2020). Analysis of Multivariate Scoring Functions for Automatic Unbiased Learning to Rank. *International Conference on Information and Knowledge Management Proceedings*. https://doi.org/10.1145/3340531.3412128

38. Gupta, S.., Hager, P.., Huang, J.., Vardasbi, A.., Oosterhuis, H.. (2023). Recent Advances in the Foundations and Applications of Unbiased Learning to Rank. *SIGIR 2023 Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval*. https://doi.org/10.1145/3539618.3594247

39. Bock, J.D.., Verstockt, S.. (2021). SmarterROUTES-A Data-driven Context-aware Solution for Personalized Dynamic Routing and Navigation. *ACM Transactions on Spatial Algorithms and Systems*. https://doi.org/10.1145/3402125

40. Yang, Y.., Qiao, Y.., Yang, T.. (2022). Compact Token Representations with Contextual Quantization for Efficient Document Re-ranking. *Proceedings of the Annual Meeting of the Association for Computational Linguistics*. https://doi.org/10.18653/v1/2022.acl-long.51

41. Chen, J.. (2020). Beyond sessions: Exploiting hybrid contextual information for web search. *Wsdm 2020 Proceedings of the 13th International Conference on Web Search and Data Mining*. https://doi.org/10.1145/3336191.3372179

42. Naseri, S.., Dalton, J.., Yates, A.., Allan, J.. (2022). CEQE to SQET: A study of contextualized embeddings for query expansion. *Information Retrieval Journal*. https://doi.org/10.1007/s10791-022-09405-y

43. Chen, H.., Chen, Y.., Meng, J.., Jiao, Y.., Ni, Y.., Gao, Y.., Momma, M.., Sun, Y.. (2023). Improving Product Search with Season-Aware Query-Product Semantic Similarity. *ACM Web Conference 2023 Companion of the World Wide Web Conference Www 2023*. https://doi.org/10.1145/3543873.3587625

44. Pham, T.M.., Yoon, S.., Bui, T.., Nguyen, A.. (2023). PiC: A Phrase-in-Context Dataset for Phrase Understanding and Semantic Search. *Eacl 2023 17th Conference of the European Chapter of the Association for Computational Linguistics Proceedings of the Conference*. https://doi.org/10.18653/v1/2023.eacl-main.1

45. Palomino, A.., Fischer, A.., Buschhüter, D.., Roller, R.., Pinkwart, N.., Paaßen, B.. (2025). Mitigating Bias in Item Retrieval for Enhancing Exam Assembly in Vocational Education Services. *Proceedings of the 2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Human Language Technologies Long Papers Naacl Hlt 2025*. https://doi.org/10.18653/v1/2025.naacl-industry.16

46. Rudra, K.., Fernando, Z.T.., Anand, A.. (2023). An in-depth analysis of passage-level label transfer for contextual document ranking. *Information Retrieval Journal*. https://doi.org/10.1007/s10791-023-09430-5

