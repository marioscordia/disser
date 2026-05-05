# Relevance and Positioning: A Systematic Bibliometric Review of Context-Aware ML Ranking in Web Search and Recommendation Systems

## Abstract

This review provides a comprehensive synthesis of research on context-aware machine learning ranking algorithms and their impact on the relevance and positioning of web resources. Through a hybrid systematic-bibliometric methodology, 69 peer-reviewed publications (2020–2025) were analyzed using PRISMA-guided study selection and VOSviewer bibliometric mapping of 71 Scopus-indexed records. VOSviewer keyword co-occurrence analysis identified seven research clusters spanning position bias correction, core information retrieval and ranking, recommender system evaluation, causal and counterfactual methods, and the emerging LLM-fairness frontier. Content analysis confirmed five thematic clusters: context-aware neural ranking architectures, bias detection and correction in learning to rank, recommender system bias and fairness, generative information retrieval and LLM-based ranking, and evaluation methodologies and cross-cutting applications. Bibliometric analysis reveals information retrieval (12 occurrences, total link strength 16) as the central network hub connecting all clusters, with the two-tower model emerging as the highest-centrality bridging concept (links-to-occurrence ratio 3.5). The review identifies three critical research gaps: the disconnection between generative IR and bias-correction research communities, the underrepresentation of cross-platform generalizability studies, and the absence of standardized evaluation protocols for context-aware ranking systems. Five high-impact research directions are proposed, including unified frameworks integrating contextual relevance estimation with position-aware ranking and the development of reproducible evaluation benchmarks.

**Keywords:** context-aware ranking, relevance, position bias, information retrieval, learning to rank, recommender systems, web search, VOSviewer, bibliometric analysis

---

## 1. Introduction

## Relevance of the Topic

In recent years, information retrieval (IR) and recommender systems have undergone a fundamental transformation driven by the integration of neural architectures and the growing demand for context-aware, personalized ranking. Modern search engines, e-commerce platforms, and content recommendation systems process billions of user interactions daily, using implicit feedback signals — clicks, dwell time, scroll depth — to train ranking models that determine which information reaches users. However, these signals are systematically distorted by multiple biases: users preferentially click higher-positioned results regardless of relevance (position bias), are never exposed to items the system does not surface (selection bias), and are influenced by the surrounding presentation context (context bias). Unbiased Learning to Rank (ULTR) has emerged as the primary methodological framework for addressing these distortions, employing counterfactual estimation and causal inference to recover true relevance from biased observations.

The significance of this research area extends beyond academic interest. Commercial platforms — including Google Search, Amazon, JD.com, Tencent, and Meituan — have reported measurable business impact from bias correction methods, with improvements ranging from 2.4% click-through rate increases to 6.5% gross merchandise volume gains. Simultaneously, the rapid emergence of Large Language Models (LLMs) is disrupting core assumptions about how retrieval systems are architected, introducing both new capabilities (generative retrieval, LLM-as-ranker) and new bias types (hallucination bias, instruction bias). Understanding the intersection of ULTR, context-aware ranking, and generative retrieval is therefore critical for both the theoretical advancement and responsible deployment of modern information access systems.

## Literature Gap

Several surveys have addressed aspects of this landscape. Gupta et al. (2023) provided a comprehensive tutorial on ULTR foundations. Dai et al. (2024) surveyed bias and unfairness in LLM-era IR systems. Li et al. (2025) systematically reviewed Generative Information Retrieval. Mateos and Bellogin (2025) conducted a systematic review of context-aware recommender systems. However, these reviews address individual subfields in isolation. No existing review integrates the three dimensions — bias correction, context-aware ranking, and generative retrieval — into a unified analytical framework. Furthermore, existing surveys do not combine systematic literature review methodology with bibliometric analysis, limiting their ability to quantify research trends, map author networks, and identify structural patterns in the field's evolution.

The present review addresses this gap by conducting a hybrid systematic-bibliometric analysis of 69 peer-reviewed publications (2021–2025) at the intersection of ULTR, context-aware IR, and neural ranking, supplemented by bibliometric data from 71 Scopus-indexed records. This integrated approach enables both qualitative synthesis of research themes and quantitative analysis of keyword trends, author productivity, and temporal evolution.

## Research Goal and Questions

The primary goal of this review is to provide a comprehensive, structured synthesis of research at the intersection of ULTR and context-aware information retrieval, identifying the dominant thematic clusters, methodological approaches, research trends, and gaps that define the field's current state and future trajectory. The review is guided by four research questions:

1. **RQ1**: What are the main thematic clusters in ULTR and context-aware information retrieval research from 2021 to 2025?
2. **RQ2**: What methodologies dominate the field — neural ranking architectures, bias correction frameworks, or context modeling approaches?
3. **RQ3**: What are the key research gaps at the intersection of ULTR and context-aware information retrieval?
4. **RQ4**: Who are the most prolific authors, what are the dominant keywords, and how has the field evolved temporally?

## Structure of the Paper

The remainder of this paper is organized as follows. Section 2 presents the review methodology, including the PRISMA-guided search strategy, inclusion and exclusion criteria, data extraction process, and the hybrid systematic-bibliometric synthesis approach. Section 3 reports the results, organized around five thematic clusters identified through content analysis: bias detection and correction in LTR, context-aware neural ranking architectures, recommender system bias and fairness, generative IR and LLM-based ranking, and evaluation and cross-cutting methodologies. Section 4 discusses the findings, comparing clusters, interpreting temporal trends, and examining the implications of the LLM-driven paradigm shift for the field. Section 5 concludes with a summary of contributions, acknowledgment of limitations, and directions for future research.


---

## 2. Methodology

## 1. Review Design

This study employs a hybrid review design integrating two complementary methodological approaches: (a) a **Systematic Literature Review** following PRISMA 2020 guidelines for study identification, screening, eligibility assessment, and inclusion, and (b) a **Bibliometric Analysis** synthesizing keyword co-occurrence patterns, temporal trends, author productivity, and source distribution. The hybrid design was selected to combine the depth of qualitative thematic synthesis with the breadth and reproducibility of quantitative bibliometric mapping. This design is consistent with emerging methodological standards for computer science literature reviews, which increasingly combine systematic and bibliometric components to address the field's rapid publication velocity and conference-driven dissemination patterns.

## 2. Databases and Search Strategy

A comprehensive search was conducted across six academic databases in May 2025: Scopus, ACM Digital Library, IEEE Xplore, Springer Link, ScienceDirect, and MDPI. These databases were selected for their complementary coverage of computer science venues — Scopus for broad multidisciplinary indexing, ACM DL for core IR conferences (SIGIR, CIKM, KDD), IEEE Xplore for applied engineering outlets, and Springer/ScienceDirect/MDPI for journal coverage.

The primary Boolean search query, executed in Scopus, was constructed from three conceptual groups:

```
TITLE-ABS-KEY (
  ( "unbiased learning to rank" OR "ULTR" OR "position bias"
    OR "personalized bias" OR "examination bias" )
  AND
  ( "context*" OR "neural" OR "attention" )
  AND
  ( "information retrieval" OR "web search" OR "recommender system*" )
)
AND PUBYEAR > 2020 AND PUBYEAR < 2026
```

Group 1 captures core ULTR and bias terminology. Group 2 captures the neural and context-aware dimension. Group 3 scopes results to IR and recommender system applications. The temporal filter restricts results to the 2021–2025 publication window. Adapted versions of this query were executed on ACM DL, IEEE Xplore, and other databases using platform-specific syntax. Additional targeted searches employed terms including "click models," "counterfactual learning to rank," "propensity weighting," "context-aware ranking," and "LLM ranking."

## 3. Inclusion and Exclusion Criteria

**Inclusion criteria**: (a) peer-reviewed journal articles, conference papers, or book chapters; (b) published in English; (c) publication date 2021–2025 (with early-access 2026 papers accepted in 2025 included); (d) addressing ULTR, position/examination/selection bias in IR or recommender systems, context-aware neural ranking, or LLM-based/generative ranking; (e) presenting original empirical results, systematic reviews, or formal theoretical analyses.

**Exclusion criteria**: (a) preprints without subsequent peer-reviewed publication; (b) non-English publications; (c) publications outside the 2021–2025 window; (d) studies focused exclusively on collaborative filtering without ranking, general NLP without IR application, or general ML fairness without IR/recommendation context; (e) insufficient methodological description to assess validity; (f) duplicate or extended versions of already-included papers.

## 4. Study Selection Process

The initial search returned 155 records across all databases. After deduplication (32 duplicate records identified by matching DOIs and titles), 123 unique records underwent title and abstract screening. Twenty-eight records were excluded at this stage: 5 non-peer-reviewed sources, 15 outside topic scope, and 8 published before 2020. Ninety-five full-text articles were retrieved and assessed for eligibility. Twenty-six were excluded: 8 with unavailable full text, 6 with insufficient methodological detail, 2 non-English, 5 extended versions of included papers, 3 outside the temporal scope on full-text review, and 2 with corrupted PDF extraction. The final corpus comprised 69 studies for qualitative synthesis and 71 Scopus-indexed records for bibliometric analysis.

## 5. Data Extraction and Analysis Tools

For each included study, standardized data extraction captured: bibliographic information (authors, year, title, source, DOI), research design (aim, methodology, participants/data), findings (main results, reported limitations), and indexing (author keywords, APA reference). Extraction was performed through systematic full-text reading, facilitated by markdown conversion of PDF sources. The extracted data were organized into a Literature Analysis Matrix enabling cross-study comparison and cluster identification.

Thematic clustering was performed through iterative content analysis of research aims, methods, and findings. Cluster boundaries were refined through cross-referencing with keyword co-occurrence patterns derived from the bibliometric analysis. Bibliometric synthesis — including keyword frequency analysis, temporal trend mapping, and source distribution analysis — was conducted using structured metadata from the Scopus export (71 records) combined with content-derived keyword extraction from the full 69-paper corpus.

## 6. Quality Assurance

Methodological quality of included studies was assessed using criteria adapted from the PRISMA 2020 checklist: clarity of research objective, methodological adequacy, empirical grounding, limitation acknowledgment, and reproducibility. Only studies meeting at least three of five criteria were included in the final synthesis. The review process was conducted in accordance with PRISMA standards for transparency and replicability. All search strategies, inclusion/exclusion criteria, and analytical procedures are documented to enable reproduction. AI-assisted tools were used for text extraction, keyword analysis, and initial screening; all AI-generated outputs were verified against source documents.


---

## 3. Results

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


---

## 4. Discussion

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


---

## 5. Conclusion

## 1. Summary of Key Findings

This hybrid systematic-bibliometric review analyzed 69 peer-reviewed publications at the intersection of Unbiased Learning to Rank and context-aware information retrieval, supported by bibliometric data from 71 Scopus-indexed records spanning the period 2021–2025. The analysis identified five thematic clusters that structure the field: bias detection and correction in learning to rank (20 papers), context-aware neural ranking architectures (10 papers), recommender system bias and fairness (11 papers), generative IR and LLM-based ranking (12 papers), and evaluation and cross-cutting methodologies (16 papers).

The bibliometric synthesis revealed that position bias remains the most studied bias type (14 of 20 papers in Cluster 1), with the field's methodological trajectory progressing from IPS-based estimation through doubly robust learning to two-tower neural architectures. The most significant trend identified is the emergence of LLM-based ranking as the fastest-growing research area (2024–2025), representing a paradigm shift from retrieval as similarity matching to retrieval as generation. Critically, this emerging paradigm lacks the formal counterfactual bias framework that two decades of IR research have established for traditional ranking architectures.

## 2. Research Significance

This review makes three primary contributions to the field. First, it provides the first integrated synthesis of ULTR, context-aware ranking, and generative retrieval literature, revealing structural connections — such as the two-tower architecture bridge between bias correction and efficient ranking — that single-focus surveys cannot capture. Second, the bibliometric component quantifies temporal trends and author productivity patterns, establishing a reproducible baseline for tracking the field's evolution. Third, by identifying the GenIR-ULTR integration gap as the field's most critical research challenge, the review provides a roadmap for future work that bridges the methodological rigor of counterfactual bias correction with the representational power of generative models.

## 3. Limitations

The findings are constrained by the review's temporal scope (2021–2025), which excludes foundational pre-2021 work; the reliance on Scopus-indexed data for bibliometric analysis, which may undercount non-indexed publications; the citation immaturity of the corpus, which precluded citation-based impact analysis; and the use of AI-assisted screening and extraction tools, which introduces incompletely characterized potential biases into the review process itself.

## 4. Future Research Directions

Future research should prioritize: (a) developing unified bias frameworks that extend ULTR counterfactual methods to generative retrieval settings; (b) establishing cross-platform generalizability evidence for bias correction methods; (c) creating multimodal and multi-context bias models that reflect the complexity of real-world retrieval systems; (d) designing computationally efficient debiasing methods for resource-constrained deployments; and (e) building community-maintained reproducibility infrastructure, including standardized benchmarks and open-source implementations.

## 5. Closing Statement

The intersection of unbiased learning to rank and context-aware information retrieval stands at a pivotal moment. The theoretical foundations of bias correction have matured to the point of industrial deployment, while the emergence of large language models is simultaneously disrupting core architectural assumptions and introducing new forms of bias that existing frameworks cannot address. The field's ability to integrate these two trajectories — the rigor of counterfactual bias correction and the capability of generative models — will determine whether the next generation of information access systems are both powerful and fair. The research gaps identified in this review represent the critical path toward that integration.


---

## References


**Total papers:** 83

---

1. Abdallah, A., Abdalla, M., Piryani, B., Mozafari, J., Ali, M., & Jatowt, A. (2025, November 10). RerankArena: A Unified Platform for Evaluating Retrieval, Reranking and RAG with Human and LLM Feedback. Proceedings of the 34th ACM International Conference on Information and Knowledge Management. ACM. http://doi.org/10.1145/3746252.3761484

2. Afzal, I., Yilmazel, B., & Kaleli, C. (2024). An Approach for Multi-Context-Aware Multi-Criteria Recommender Systems Based on Deep Learning. IEEE Access. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2024.3428630

3. Ahemad, F. (2025, November 10). Quantization Aware Matryoshka Adaptation: Leveraging Matryoshka Learning, Quantization, and Bitwise Operations for Reduced Storage and Improved Retrieval Speed. Proceedings of the 34th ACM International Conference on Information and Knowledge Management. ACM. http://doi.org/10.1145/3746252.3761077

4. Alaofi, M., Arabzadeh, N., Clarke, C. L. A., & Sanderson, M. (2024, September 12). Generative Information Retrieval Evaluation. The Information Retrieval Series. Springer Nature Switzerland. http://doi.org/10.1007/978-3-031-73147-1_6

5. Amala, K. J., & Rajeswari, D. (2025). Neural Learning to Rank Model With Bias Correction and Attention Enhanced Relevance Prediction. IEEE Access. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2025.3625652

6. Anand, A., Leonhardt, J., Singh, J., Rudra, K., & Anand, A. (2024, April 29). Data Augmentation for Sample Efficient and Robust Document Ranking. ACM Transactions on Information Systems. Association for Computing Machinery (ACM). http://doi.org/10.1145/3634911

7. Arora, N., Mathur, H., & Patil, V. R. (2025, October 1). Toward Contextual Search Optimization: A Unified Ranking Approach for Relevance Prioritization. Lecture Notes in Networks and Systems. Springer Nature Singapore. http://doi.org/10.1007/978-981-96-7508-1_12

8. Batri, K., Lakshmi, S., & Sowrirajan, R. (2025). Parabolic Weighting Mechanism in Information Retrieval: A Mathematical Analogy to Lenz’s Law. IEEE Access. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2025.3550964

9. Batri, K., Thinakaran, R., Lakshmi, S., Sowrirajan, R., & Murugan, S. (2025). Beyond Precision and Recall: Measuring Search Engine Consistency Using Rank Stability. IEEE Access. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2025.3571184

10. Buyl, M., Missault, P., & Sondag, P.-A. (2023, August 4). RankFormer: Listwise Learning-to-Rank Using Listwide Labels. Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. ACM. http://doi.org/10.1145/3580305.3599892

11. Carnovalini, F., Rodà, A., & Wiggins, G. A. (2025, February 19). Popularity Bias in Recommender Systems: The Search for Fairness in the Long Tail. Information. MDPI AG. http://doi.org/10.3390/info16020151

12. Chaipornkaew, P., & Banditwattanawong, T. (2025). A Novel Method for News Recommendation on Websites Using the Clustered-Vectors Optimization Algorithm. IEEE Access. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2025.3526885

13. Cheng, X., Zhou, X., Fang, L., He, C., Zhou, Y., Luo, W., … Guan, Q. (2025, July 13). NR4DER: Neural Re-ranking for Diversified Exercise Recommendation. Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM. http://doi.org/10.1145/3726302.3730046

14. Dai, S., Xu, C., Xu, S., Pang, L., Dong, Z., & Xu, J. (2024, August 24). Bias and Unfairness in Information Retrieval Systems: New Challenges in the LLM Era. Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. ACM. http://doi.org/10.1145/3637528.3671458

15. De Leon, J. J., & Medda, F. (2025, November 13). Linguistic Alphas: Decoding the Market Impact of Words in Software Earnings Calls. Cureus Journal of Business and Economics. Springer Science and Business Media LLC. http://doi.org/10.7759/s44404-025-08244-6

16. Deng, Z., Qiao, J., Dou, Z., Wen, J.-R., & de Rijke, M. (2025, November 10). DIVAgent: A Diversified Search Agent that Mimics the Human Search Process. Proceedings of the 34th ACM International Conference on Information and Knowledge Management. ACM. http://doi.org/10.1145/3746252.3761059

17. Ghosh, S., & Mittal, G. (2025, November 19). Advancing engineering research through context-aware and knowledge graph–based retrieval-augmented generation. Frontiers in Artificial Intelligence. Frontiers Media SA. http://doi.org/10.3389/frai.2025.1697169

18. Gupta, S., Hager, P., Huang, J., Vardasbi, A., & Oosterhuis, H. (2023, July 18). Recent Advances in the Foundations and Applications of Unbiased Learning to Rank. Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM. http://doi.org/10.1145/3539618.3594247

19. Haddad, R., Hlaoua, L., & Omri, M. N. (2025). ReGAT-BERT: Transformer-Graph Fusion for Dynamic Reranking. Procedia Computer Science. Elsevier BV. http://doi.org/10.1016/j.procs.2025.09.302

20. Heuss, M., de Rijke, M., & Anand, A. (2025, July 13). RankingSHAP - Faithful Listwise Feature Attribution Explanations for Ranking Models . Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM. http://doi.org/10.1145/3726302.3729971

21. Hofstätter, S., Lipani, A., Althammer, S., Zlabinger, M., & Hanbury, A. (2021). Mitigating the Position Bias of Transformer Models in Passage Re-ranking. Lecture Notes in Computer Science. Springer International Publishing. http://doi.org/10.1007/978-3-030-72113-8_16

22. Huang, Y., Chen, X., Zhang, W., Li, Q., & Li, H. (2025). Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing. IEEE Access. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2025.3576253

23. Jeon, J., Lee, J., Ryu, C., & Kang, U. (2025, November 10). Entity-Aware Generative Retrieval for Personalized Contexts. Proceedings of the 34th ACM International Conference on Information and Knowledge Management. ACM. http://doi.org/10.1145/3746252.3761211

24. Karlović, R., Rovis, M., Smajić, A., Sever, L., & Lorencin, I. (2025, November 14). Context-Aware Tourism Recommendations Using Retrieval-Augmented Large Language Models and Semantic Re-Ranking. Electronics. MDPI AG. http://doi.org/10.3390/electronics14224448

25. Krasakis, A. M., Yates, A., & Kanoulas, E. (2025, November 10). Constructing Set-Compositional and Negated Representations for First-Stage Ranking. Proceedings of the 34th ACM International Conference on Information and Knowledge Management. ACM. http://doi.org/10.1145/3746252.3761238

26. Kulkarni, H., Kallumadi, S., MacAvaney, S., Goharian, N., & Frieder, O. (2025, May 8). GRIT: Graph-based Recall Improvement for Task-oriented E-commerce Queries. Companion Proceedings of the ACM on Web Conference 2025. ACM. http://doi.org/10.1145/3701716.3717859

27. Kumar, S., Rohatgi, D., Prakash, N., Sahai, S., Chandra, S., Kumar Mishra, S., … Kumar, M. (2026, January). 2P-BEnc: A two-phase information retrieval and ranking system based on the BERT encoder. Ain Shams Engineering Journal. Elsevier BV. http://doi.org/10.1016/j.asej.2025.103853

28. Leonhardt, J., Müller, H., Rudra, K., Khosla, M., Anand, A., & Anand, A. (2024, April 29). Efficient Neural Ranking Using Forward Indexes and Lightweight Encoders. ACM Transactions on Information Systems. Association for Computing Machinery (ACM). http://doi.org/10.1145/3631939

29. Leonhardt, J., Rudra, K., & Anand, A. (2023, March 23). Extractive Explanations for Interpretable Text Ranking. ACM Transactions on Information Systems. Association for Computing Machinery (ACM). http://doi.org/10.1145/3576924

30. Leonhardt, J., Rudra, K., Khosla, M., Anand, A., & Anand, A. (2022, April 25). Efficient Neural Ranking using Forward Indexes. Proceedings of the ACM Web Conference 2022. ACM. http://doi.org/10.1145/3485447.3511955

31. Li, X., Jin, J., Zhou, Y., Zhang, Y., Zhang, P., Zhu, Y., & Dou, Z. (2025, May 9). From Matching to Generation: A Survey on Generative Information Retrieval. ACM Transactions on Information Systems. Association for Computing Machinery (ACM). http://doi.org/10.1145/3722552

32. Lyu, L., Roy, N., Oosterhuis, H., & Anand, A. (2024). Is Interpretable Machine Learning Effective at Feature Selection for Neural Learning-to-Rank?. Lecture Notes in Computer Science. Springer Nature Switzerland. http://doi.org/10.1007/978-3-031-56066-8_29

33. Mahmoud, A. F. A., Mohammed, Z. M. S., Ben Ammar, M., Satty, A., Abdalla, F. A., Khamis, G. S. M., … Mohamed, A. S. (2025, February 2). Enhancing Semantic Search Precision through the CBOW Algorithm in the Semantic Web. Engineering, Technology & Applied Science Research. Engineering, Technology & Applied Science Research. http://doi.org/10.48084/etasr.9450

34. Manta-Caro, C., Caputo, A., & Fernández-Luna, J. M. (2025, March 15). Information Retrieval for IoT and WoT: State-of-the-Art, Taxonomy Framework, and Evolutionary Directions. IEEE Internet of Things Journal. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/jiot.2024.3522219

35. Mateos, P., & Bellogín, A. (2024, November 16). A systematic literature review of recent advances on context-aware recommender systems. Artificial Intelligence Review. Springer Science and Business Media LLC. http://doi.org/10.1007/s10462-024-10939-4

36. Naseri, S., Dalton, J., Yates, A., & Allan, J. (2022, March 22). CEQE to SQET: A study of contextualized embeddings for query expansion. Information Retrieval Journal. Springer Science and Business Media LLC. http://doi.org/10.1007/s10791-022-09405-y

37. Nguyen, T.-P., Nguyen, T.-H., Dinh, G.-H., Nguyen, L.-H., Tran, M.-T., & Le, T.-N. (2025, October 27). ReCap: Event-Aware Image Captioning with Article Retrieval and Semantic Gaussian Normalization. Proceedings of the 33rd ACM International Conference on Multimedia. ACM. http://doi.org/10.1145/3746027.3762039

38. Niu, Z., Mei, L., Yang, L., Zhao, Z., Yan, Q., Mao, J., & Wen, J.-R. (2025, November 10). Addressing Personalized Bias for Unbiased Learning to Rank. Proceedings of the 34th ACM International Conference on Information and Knowledge Management. ACM. http://doi.org/10.1145/3746252.3761377

39. Novak, E., Bizjak, L., Mladenić, D., & Grobelnik, M. (2022, May). Why is a document relevant? Understanding the relevance scores in cross-lingual document retrieval. Knowledge-Based Systems. Elsevier BV. http://doi.org/10.1016/j.knosys.2022.108545

40. Podder, D., Paik, J. H., & Mitra, P. (2026, January 2). A retrieval model with contextual correlation analysis for verbose queries. Journal of Intelligent Information Systems. Springer Science and Business Media LLC. http://doi.org/10.1007/s10844-025-01009-4

41. Ren, Y., Tang, H., & Zhu, S. (2022, October 17). Unbiased Learning to Rank with Biased Continuous Feedback. Proceedings of the 31st ACM International Conference on Information & Knowledge Management. ACM. http://doi.org/10.1145/3511808.3557483

42. Santosh Nakirikanti. (2025, April 30). AI-powered search: Revolutionizing the online shopping experience. World Journal of Advanced Engineering Technology and Sciences. GSC Online Press. http://doi.org/10.30574/wjaets.2025.15.1.0216

43. Thakare, Atul & Soora, Narasimha Reddy & Jena, Lambodar & Singh, Arvind. (2025). Boosting Webpage Retrieval with Ensemble Learning and Advanced Semantic Models: A Novel Re-Ranking Framework. IAENG International Journal of Computer Science. 52. 3574-3582.

44. Wijnhoven, F., & van Haren, J. (2021, May 26). Search Engine Gender Bias. Frontiers in Big Data. Frontiers Media SA. http://doi.org/10.3389/fdata.2021.622106

45. Xu, B., Lin, H., Lin, Y., & Xu, K. (2022, August 25). Context-aware ranking refinement with attentive semi-supervised autoencoders. Soft Computing. Springer Science and Business Media LLC. http://doi.org/10.1007/s00500-022-07433-w

46. Yang, Y., Qiao, Y., Shao, J., Yan, X., & Yang, T. (2022, February 11). Lightweight Composite Re-Ranking for Efficient Keyword Search with BERT. Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining. ACM. http://doi.org/10.1145/3488560.3498495

47. Yasin, S. A., & Prasada Rao, P. V. R. D. (2022, October). Enhanced CRNN-Based Optimal Web Page Classification and Improved Tunicate Swarm Algorithm-Based Re-Ranking. International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems. World Scientific Pub Co Pte Ltd. http://doi.org/10.1142/s0218488522500246

48. Ye, Z., Xie, X., Liu, Y., Wang, Z., Li, X., Li, J., … Ma, S. (2022, July 6). Why Don't You Click. Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM. http://doi.org/10.1145/3477495.3532082

49. Zhou, Y., Yao, J., Dou, Z., Tu, Y., Wu, L., Chua, T.-S., & Wen, J.-R. (2024, October 22). ROGER: Ranking-Oriented Generative Retrieval. ACM Transactions on Information Systems. Association for Computing Machinery (ACM). http://doi.org/10.1145/3603167Scopus (new export)

50. Fabris, A., Rus, C., Saldivar, J., Gatzioura, A., Biega, A. J., & Castillo, C. (2026, April). Does fair ranking lead to fair recruitment outcomes? A study of interventions, interfaces, and interactions. <i>Information Processing & Management</i>. Elsevier BV. http://doi.org/10.1016/j.ipm.2025.104506

51. Melchiorre, A. B., Penz, D., Ganhör, C., Lesota, O., Fragoso, V., Fritzl, F., … Schedl, M. (2023, June). Emotion-aware music tower blocks (EmoMTB ): an intelligent audiovisual interface for music discovery and recommendation. <i>International Journal of Multimedia Information Retrieval</i>. Springer Science and Business Media LLC. http://doi.org/10.1007/s13735-023-00275-8

52. (n.d.). Scopus - Document Details. Retrieved from https://www.scopus.com/pages/publications/85111024895?origin=resultslist

53. He, L., Zhao, J., Gu, Y., Elbaz, M., & Ding, Z. (2024, March 26). A bias study and an unbiased deep neural network for recommender systems. <i>Web Intelligence</i>. SAGE Publications. http://doi.org/10.3233/web-230036

54. (n.d.). Scopus - Document Details. Retrieved from https://www.scopus.com/pages/publications/85169032399?origin=resultslist

55. Jin, J., He, Z., Yang, M., Zhang, W., Yu, Y., Wang, J., & McAuley, J. (2024, May 13). InfoRank: Unbiased Learning-to-Rank via Conditional Mutual Information Minimization. <i>Proceedings of the ACM Web Conference 2024</i>. ACM. http://doi.org/10.1145/3589334.3645356

56. Luo, D., Zou, L., Ai, Q., Chen, Z., Yin, D., & Davison, B. D. (2023, February 27). Model-based Unbiased Learning to Rank. <i>Proceedings of the Sixteenth ACM International Conference on Web Search and Data Mining</i>. ACM. http://doi.org/10.1145/3539597.3570395

57. Chen, M., Liu, C., Sun, J., & Hoi, S. C. H. (2021, July 11). Adapting Interactional Observation Embedding for Counterfactual Learning to Rank. <i>Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval</i>. ACM. http://doi.org/10.1145/3404835.3462901

58. Ferrari Dacrema, M., Felicioni, N., & Cremonesi, P. (2022, June 9). Offline Evaluation of Recommender Systems in a User Interface With Multiple Carousels. <i>Frontiers in Big Data</i>. Frontiers Media SA. http://doi.org/10.3389/fdata.2022.910030

59. Bisht, K., & Susan, S. (2022, April 25). v-TCM. <i>Proceedings of the 37th ACM/SIGAPP Symposium on Applied Computing</i>. ACM. http://doi.org/10.1145/3477314.3507214

60. Chen, J., Wang, X., Feng, F., & He, X. (2021, September 13). Bias Issues and Solutions in Recommender System. <i>Fifteenth ACM Conference on Recommender Systems</i>. ACM. http://doi.org/10.1145/3460231.3473321

61. Hofstätter, S., Zlabinger, M., Sertkan, M., Schröder, M., & Hanbury, A. (2020, October 19). Fine-Grained Relevance Annotations for Multi-Task Document Ranking and Question Answering. <i>Proceedings of the 29th ACM International Conference on Information & Knowledge Management</i>. ACM. http://doi.org/10.1145/3340531.3412878

62. Wu, X., Chen, H., Zhao, J., He, L., Yin, D., & Chang, Y. (2021, March 8). Unbiased Learning to Rank in Feeds Recommendation. <i>Proceedings of the 14th ACM International Conference on Web Search and Data Mining</i>. ACM. http://doi.org/10.1145/3437963.3441751

63. Huang, J., Hu, K., Tang, Q., Chen, M., Qi, Y., Cheng, J., & Lei, J. (2021, July 11). Deep Position-wise Interaction Network for CTR Prediction. <i>Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval</i>. ACM. http://doi.org/10.1145/3404835.3463117

64. Dai, X., Hou, J., Liu, Q., Xi, Y., Tang, R., Zhang, W., … Yu, Y. (2020, October 19). U-rank. <i>Proceedings of the 29th ACM International Conference on Information & Knowledge Management</i>. ACM. http://doi.org/10.1145/3340531.3412756

65. Yu, Y., Jin, B., Song, J., Li, B., Zheng, Y., & Zhuo, W. (2023). Improving Micro-video Recommendation by Controlling Position Bias. <i>Lecture Notes in Computer Science</i>. Springer International Publishing. http://doi.org/10.1007/978-3-031-26387-3_31

66. Luo, S., He, B., Zhao, H., Shao, W., Qi, Y., Huang, Y., … Song, L. (2025, July 10). RecRanker: Instruction Tuning Large Language Model as Ranker for Top-k Recommendation. <i>ACM Transactions on Information Systems</i>. Association for Computing Machinery (ACM). http://doi.org/10.1145/3705728

67. Felicioni, N., Ferrari Dacrema, M., & Cremonesi, P. (2021, June 21). A Methodology for the Offline Evaluation of Recommender Systems in a User Interface with Multiple Carousels. <i>Adjunct Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization</i>. ACM. http://doi.org/10.1145/3450614.3461680

68. Yang, T., Fang, S., Li, S., Wang, Y., & Ai, Q. (2020, October 19). Analysis of Multivariate Scoring Functions for Automatic Unbiased Learning to Rank. <i>Proceedings of the 29th ACM International Conference on Information & Knowledge Management</i>. ACM. http://doi.org/10.1145/3340531.3412128

69. Ovaisi, Z., Ahsan, R., Zhang, Y., Vasilaky, K., & Zheleva, E. (2020, April 20). Correcting for Selection Bias in Learning-to-rank Systems. <i>Proceedings of The Web Conference 2020</i>. ACM. http://doi.org/10.1145/3366423.3380255

70. (n.d.). Scopus - Document Details. Retrieved from https://www.scopus.com/pages/publications/105029924249?origin=resultslist

71. Zhuang, H., Qin, Z., Wang, X., Bendersky, M., Qian, X., Hu, P., & Chen, D. C. (2021, April 19). Cross-Positional Attention for Debiasing Clicks. <i>Proceedings of the Web Conference 2021</i>. ACM. http://doi.org/10.1145/3442381.3450098

72. Mahendru, S., & Pandit, T. (2024, June 7). Venn Diagram Prompting: Accelerating Comprehension with Scaffolding Effect. <i>2024 6th World Symposium on Artificial Intelligence (WSAI)</i>. IEEE. http://doi.org/10.1109/wsai62426.2024.10828919

73. Azimi, M. (2026). Context-Aware Ranking in Expert Finding. <i>Lecture Notes in Computer Science</i>. Springer Nature Switzerland. http://doi.org/10.1007/978-3-032-21324-2_41

74. Cachel, K., & Rundensteiner, E. (2023, June 12). Fairer Together: Mitigating Disparate Exposure in Kemeny Rank Aggregation. <i>2023 ACM Conference on Fairness Accountability and Transparency</i>. ACM. http://doi.org/10.1145/3593013.3594085

75. Zheng, J., Li, J., & Huang, M. (2025, August). Personalized anchor debiased-contrastive learning for multi-behavior recommendation. <i>Expert Systems with Applications</i>. Elsevier BV. http://doi.org/10.1016/j.eswa.2025.127685

76. Karra Taniskidou, E., Zhao, W., Murray, I., & Pellegrini, R. (2023, October 21). Nudging Neural Click Prediction Models to Pay Attention to Position. <i>Proceedings of the 32nd ACM International Conference on Information and Knowledge Management</i>. ACM. http://doi.org/10.1145/3583780.3614994

77. Wu, Y., & Zhao, W. (2024, June 30). Debiased Causal Inference for Sequential Recommendation. <i>2024 International Joint Conference on Neural Networks (IJCNN)</i>. IEEE. http://doi.org/10.1109/ijcnn60899.2024.10650048

78. Jin, J., Fang, Y., Zhang, W., Ren, K., Zhou, G., Xu, J., … Gai, K. (2020, July 25). A Deep Recurrent Survival Model for Unbiased Ranking. <i>Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval</i>. ACM. http://doi.org/10.1145/3397271.3401073

79. Qin, Z., Chen, S. J., Metzler, D., Noh, Y., Qin, J., & Wang, X. (2020, August 20). Attribute-based Propensity for Unbiased Learning in Recommender Systems. <i>Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining</i>. ACM. http://doi.org/10.1145/3394486.3403285

80. (n.d.). Scopus - Document Details. Retrieved from https://www.scopus.com/pages/publications/85210029070?origin=resultslist

81. Amala, K. J., & Rajeswari, D. (2025). Nonparametric Click Modeling Using Dirichlet Process Mixture Model for Information Retrieval. <i>IEEE Access</i>. Institute of Electrical and Electronics Engineers (IEEE). http://doi.org/10.1109/access.2025.3639062

82. HE, X., An, B., Li, Y., Chen, H., Guo, Q., Li, X., & Wang, Z. (2020, September 22). Contextual User Browsing Bandits for Large-Scale Online Mobile Recommendation. <i>Fourteenth ACM Conference on Recommender Systems</i>. ACM. http://doi.org/10.1145/3383313.3412234

83. (n.d.). Scopus - Document Details. Retrieved from https://www.scopus.com/pages/publications/85107388450?origin=resultslist

