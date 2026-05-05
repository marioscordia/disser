# Methodology

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
