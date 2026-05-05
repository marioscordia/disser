# Methodology

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
