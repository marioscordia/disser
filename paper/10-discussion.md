# Discussion

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
