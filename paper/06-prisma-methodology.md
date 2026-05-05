# PRISMA Methodology and Search Strategy

**Review Type:** Hybrid Systematic + Bibliometric Review
**Standards:** PRISMA 2020

---

## 1. PRISMA Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        IDENTIFICATION                           │
│                                                                 │
│  Records identified from Scopus (n = 318)                       │
│  Search query: context-aware + ranking + relevance +            │
│    web search / recommender systems                             │
│  Date of search: May 2025                                       │
│                                                                 │
│  Records removed BEFORE screening:                              │
│  • Not retrieved / inaccessible (n = 0)                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                           SCREENING                             │
│                                                                 │
│  Records screened by title/abstract (n = 318)                   │
│                                                                 │
│  Records excluded (n = 182):                                    │
│  • Outside topic scope — not IR/ranking/recommender (n = 147)   │
│  • Outside 2020–2025 window (n = 4)                             │
│  • No DOI available (n = 1)                                     │
│  • Off-topic after content review (n = 30)                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                          ELIGIBILITY                            │
│                                                                 │
│  Full-text articles assessed for eligibility (n = 136)          │
│                                                                 │
│  Articles excluded (n = 44):                                    │
│  • Zero citations in Scopus (n = 44)                            │
│  • Full text unavailable (n = 0)                                │
│  • Non-English (n = 0)                                          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                           INCLUDED                              │
│                                                                 │
│  Studies included in bibliometric analysis (n = 48)             │
│  • All 48 confirmed in Scopus with complete metadata            │
│                                                                 │
│  Studies included in qualitative synthesis (n = 46)             │
│  • 46 full-text papers analyzed via literature matrix           │
│  • 2 excluded: off-topic on full-text review                    │
│  • 3 additional: full text available but outside scope          │
│                                                                 │
│  • Context-aware ranking / neural IR studies (n = 18)           │
│  • Recommender system bias and fairness studies (n = 12)        │
│  • Click models and counterfactual LTR studies (n = 8)          │
│  • Evaluation and cross-cutting studies (n = 8)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Search Strategy

### 2.1 Research Questions

1. **RQ1**: What are the main thematic clusters in context-aware machine learning ranking research for web search and recommendation systems (2020–2025)?
2. **RQ2**: What methodologies dominate — neural ranking architectures, bias correction frameworks, or context modeling approaches?
3. **RQ3**: How does context-aware ML ranking affect the relevance and positioning of web resources?
4. **RQ4**: What are the key research gaps at the intersection of context-awareness, ranking fairness, and result positioning?

### 2.2 Database and Search Query

A comprehensive search was conducted in Scopus in May 2025 using the following Boolean query:

```
TITLE-ABS-KEY (
  ( "context-aware ranking" OR "context-aware retrieval"
    OR "contextual ranking" OR "context-aware recommendation"
    OR "context-aware" AND "learning to rank"
    OR "contextual" AND "neural ranking"
    OR "context*" AND "re-ranking"
    OR "context*" AND "ranking model" )
  AND
  ( "web search" OR "search engine" OR "information retrieval"
    OR "recommender system" OR "recommendation system"
    OR "web resource" OR "document retrieval" )
  AND
  ( "relevance" OR "position" OR "ranking quality"
    OR "ndcg" OR "map" OR "mrr" )
)
AND PUBYEAR > 2019 AND PUBYEAR < 2026
```

The query targets the intersection of three conceptual dimensions: (a) context-aware or contextual ranking mechanisms, (b) web search and recommender system applications, and (c) relevance and positioning outcomes. The temporal filter (2020–2025) captures the period of most active research following the BERT-era transformation of neural IR.

### 2.3 Inclusion and Exclusion Criteria

| Criterion | Inclusion | Exclusion |
|-----------|----------|-----------|
| Topic | Studies addressing context-aware ranking, contextual retrieval, context-aware recommendation, or contextual neural ranking for web search or recommender systems | Studies where "context-aware" refers to non-IR domains (computer vision, NLP without retrieval, edge computing without ranking) |
| Publication type | Peer-reviewed journal articles, conference papers, reviews | Preprints without subsequent publication, editorials |
| Time frame | 2020–2025 | Before 2020 or after 2025 |
| Language | English | Non-English |
| Quality | At least 1 Scopus citation | Zero citations (excluded at eligibility stage) |

---

## 3. Study Selection Process

The initial Scopus search returned 318 records. All 318 underwent title and abstract screening, during which 182 records were excluded: 147 were outside the IR/ranking/recommender topic scope (capturing papers where "context-aware" referred to video processing, medical applications, construction engineering, or other non-IR domains), 4 were outside the 2020–2025 temporal window, 1 lacked a DOI, and 30 were identified as off-topic after deeper content review.

The remaining 136 papers underwent full eligibility assessment. Applying the citation threshold criterion (minimum 1 Scopus citation), 44 zero-citation papers were excluded. This threshold was applied to ensure the review synthesizes research with demonstrated academic impact, consistent with the bibliometric component's requirement for meaningful citation-based indicators.

Forty-eight papers were confirmed in Scopus with complete bibliographic metadata and exported for VOSviewer analysis. Of these, 46 full-text papers were obtained and included in the qualitative synthesis (literature matrix and thematic analysis). Two papers were excluded at this stage as off-topic on full-text review (university rankings methodology, linguistic usage analysis).

The bibliometric analysis component (keyword co-occurrence, co-authorship, bibliographic coupling) draws from the 48 Scopus-confirmed records. The qualitative synthesis (thematic clustering, literature matrix) draws from the 46 full-text papers. The discrepancy of 2 papers reflects Scopus records retained for bibliometric completeness whose content was determined to be outside the review's topical scope.

---

## 4. Data Extraction and Analysis Tools

Bibliometric analysis was conducted using VOSviewer 1.6.20, producing four map types: (1) author keyword co-occurrence (min. 2 occurrences, 21 keywords, 5 clusters), (2) index keyword co-occurrence (min. 3 occurrences, 36 keywords, 4 clusters), (3) co-authorship (min. 2 documents, 11 authors, 3 research groups), and (4) bibliographic coupling (min. 1 shared reference, 39 connected documents, 5 clusters).

For the qualitative synthesis, full-text papers in markdown format were systematically read and data extracted into a standardized Literature Analysis Matrix capturing: bibliographic information, research aim, methodology, participants/data, main findings, reported limitations, and author keywords. Thematic clustering was performed through iterative content analysis cross-validated against VOSviewer cluster assignments.

---

## 5. Quality Assurance

Methodological quality followed PRISMA 2020 guidelines. The citation threshold (≥1 Scopus citation) served as a bibliometric quality filter. AI-assisted tools were used for text extraction and initial screening; all AI-generated outputs were verified against source documents.

---

✅ PRISMA methodology successfully generated.
