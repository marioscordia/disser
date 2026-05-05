# Discussion

## 1. Interpretation of Key Findings

The identification of five distinct thematic clusters reveals a field organized around a central tension: the methodological rigor of bias correction versus the architectural disruption of generative models. Cluster 1 (Bias Correction) and Cluster 4 (GenIR/LLM) represent opposite poles of this tension, with Clusters 2, 3, and 5 occupying intermediate positions that connect these poles through shared concerns with architecture, fairness, and evaluation.

The dominance of position bias as the most studied bias type — appearing in 14 of 20 papers in Cluster 1 — reflects both its practical importance and its relative tractability. Position is observable, controllable in experiments, and amenable to mathematical formalization through examination probability models. Selection bias (Ovaisi et al., 2020) and personalized bias (Niu et al., 2025) represent the frontier of bias research, requiring more complex models that account for what users never see and how different users exhibit different examination patterns. The progression from IPS to doubly robust to two-tower architectures mirrors the development of causal inference methods in epidemiology and econometrics, suggesting that the ULTR field is following a mature methodological trajectory.

The emergence of Cluster 4 (GenIR/LLM) as the fastest-growing research area — concentrated in 2024–2025 — parallels broader AI community trends but carries specific implications for the IR field. The finding that LLMs introduce new bias types (Dai et al., 2024) while simultaneously lacking the formal counterfactual framework developed for traditional IR biases represents a critical gap. The field risks bifurcating into two disconnected research communities: one refining increasingly sophisticated ULTR methods for traditional ranking architectures, and another building LLM-based systems without the bias-awareness that two decades of IR research have established as essential.

## 2. Comparison with Previous Work

The thematic structure identified in this review both confirms and extends prior surveys. Gupta et al. (2023) focused exclusively on ULTR methods, covering the material in Cluster 1 but not addressing the architectural (Cluster 2), fairness (Cluster 3), or generative (Cluster 4) dimensions that this review shows are increasingly central to the field. Li et al. (2025) surveyed GenIR comprehensively but treated bias as a peripheral concern rather than a central analytical dimension. Dai et al. (2024) identified LLM-era bias types but did not connect these to the established ULTR literature. Mateos and Bellogin (2025) covered context-aware recommender systems but limited their scope to recommendation, excluding core IR ranking architectures.

The present review's contribution is the integration of these previously disconnected sub-literatures into a unified framework. By showing that two-tower architectures bridge bias correction (Cluster 1) and efficient ranking (Cluster 2), that fairness concerns (Cluster 3) apply equally to traditional and generative systems, and that the evaluation infrastructure (Cluster 5) lags behind architectural innovation, this review provides a map of the field that existing single-focus surveys cannot offer.

The geographic and institutional concentration observed — Tsinghua University, Renmin University of China, TU Delft, University of Amsterdam — is consistent with bibliometric studies of IR more broadly. However, the strong representation of industry research labs (Google, JD.com, Tencent, Meituan) is notable. In more mature fields, industry contributions are often concentrated in applied venues; in ULTR and context-aware IR, industry papers appear in top-tier academic venues (SIGIR, CIKM, KDD), contributing to both theory and practice. This pattern indicates a field where the gap between academic research and industrial deployment is unusually narrow.

## 3. Theoretical and Practical Implications

The finding that permutation invariance is necessary for AutoULTR convergence (Fang et al., 2020) has implications beyond the original context. As generative retrieval models produce ranked outputs without explicit scoring functions, the conditions under which such models are theoretically guaranteed to converge to unbiased rankings remain unexplored. Extending permutation invariance analysis to generative retrieval architectures represents a high-impact theoretical direction.

The practical finding that combined propensity models (position × context bias) consistently outperform single-bias approaches (Wu et al., 2021) suggests that industrial ranking systems should move beyond position-only debiasing. However, the computational cost of two-tower architectures — identified as a limitation in multiple studies — may limit adoption in resource-constrained deployments, including IoT and edge computing scenarios (Huang et al., 2025).

The multi-carousel evaluation results (Felicioni et al., 2021; Ferrari Dacrema et al., 2022) have direct implications for recommender system development. The demonstration that algorithm rankings change depending on whether evaluation uses single-list or carousel metrics means that offline evaluation protocols, which almost universally assume single-list presentation, may be systematically misleading for modern multi-carousel interfaces.

## 4. Limitations of This Review

Several limitations should be considered when interpreting the findings. First, the review's temporal scope (2021–2025) captures the most active period of ULTR and GenIR research but excludes foundational pre-2021 work. The theoretical frameworks of IPS-based ULTR, the original position-based click models, and the early neural IR architectures were established before this window, and understanding them is necessary for full appreciation of the field's evolution.

Second, the bibliometric component relies on Scopus-indexed data (71 records). While Scopus provides the most comprehensive structured metadata for computer science, some relevant publications — particularly in newer or regional venues — may not be Scopus-indexed. The qualitative synthesis compensates for this by including non-Scopus papers, but the bibliometric analysis (keyword frequency, author productivity) is necessarily constrained to Scopus-covered publications.

Third, the screening process, while following PRISMA guidelines, involved AI-assisted tools for initial title/abstract screening and keyword extraction. While all AI outputs were verified against source documents, the use of AI in the review process itself introduces potential biases that are incompletely characterized.

Fourth, the citation immaturity of the corpus — most papers were published in 2024–2025 and have accumulated few citations — precluded citation-based impact analysis, which is traditionally a core component of bibliometric reviews. Author and keyword productivity were used as alternative bibliometric indicators.

## 5. Future Research Directions

The analysis identifies five high-impact research directions:

1. **Unified bias frameworks for GenIR**: Extending ULTR counterfactual methods to generative retrieval settings where documents are not retrieved but generated. This requires formalizing how position bias, selection bias, and other click-based distortions manifest when an LLM produces output directly, and developing corresponding propensity estimation and debiasing techniques.

2. **Cross-platform generalizability**: The majority of bias correction methods are validated on single platforms. Multi-platform studies with shared evaluation protocols are needed to establish which methods are broadly applicable versus platform-specific.

3. **Multimodal and multi-context bias**: Current bias models operate predominantly on text-based ranking with a narrow set of context types (time, location, device). Real-world systems increasingly incorporate images, structured data, and rich contextual signals (affective state, social context, longitudinal behavior), for which no formal bias frameworks exist.

4. **Computationally efficient debiasing for resource-constrained deployments**: Two-tower architectures and doubly robust estimation provide strong bias correction but at significant computational cost. Lightweight debiasing methods compatible with edge computing and real-time ranking constraints remain underexplored.

5. **Reproducibility infrastructure**: The field lacks standardized benchmark protocols, shared evaluation datasets, and open-source implementations. Establishing community-maintained benchmarks, similar to BEIR for neural retrieval, would accelerate progress and enable rigorous comparison across research groups.
