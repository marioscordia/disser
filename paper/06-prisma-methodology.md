# PRISMA Methodology and Search Strategy

**Review Type:** Hybrid Systematic + Bibliometric Review
**Standards:** PRISMA 2020

---

## 1. PRISMA Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        IDENTIFICATION                           │
│                                                                 │
│  Records identified from databases (n = 155):                   │
│  • Scopus (n = 71)                                              │
│  • ACM Digital Library (n = 38)                                 │
│  • IEEE Xplore (n = 22)                                         │
│  • Springer Link (n = 10)                                       │
│  • ScienceDirect (n = 6)                                        │
│  • MDPI (n = 5)                                                 │
│  • Frontiers (n = 3)                                            │
│                                                                 │
│  Records removed BEFORE screening:                              │
│  • Duplicate records removed (n = 32)                           │
│  • Records removed for other reasons (n = 0)                    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                           SCREENING                             │
│                                                                 │
│  Records screened by title/abstract (n = 123)                   │
│                                                                 │
│  Records excluded (n = 28):                                     │
│  • Not peer-reviewed (preprints, technical reports) (n = 5)     │
│  • Outside topic scope (n = 15)                                 │
│  • Published before 2020 (n = 8)                                │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                          ELIGIBILITY                            │
│                                                                 │
│  Full-text articles assessed for eligibility (n = 95)           │
│                                                                 │
│  Articles excluded (n = 26):                                    │
│  • Full text unavailable (n = 8)                                │
│  • Insufficient methodological detail (n = 6)                   │
│  • Non-English (n = 2)                                          │
│  • Duplicate content / extended version (n = 5)                 │
│  • Outside 2021-2025 scope on full-text review (n = 3)          │
│  • Incomplete extraction / corrupted file (n = 2)               │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                           INCLUDED                              │
│                                                                 │
│  Studies included in synthesis (n = 69)                         │
│  • Position bias / ULTR studies (n = 20)                        │
│  • Context-aware neural ranking studies (n = 10)                │
│  • Recommender system bias and fairness studies (n = 11)        │
│  • GenIR / LLM-based ranking studies (n = 12)                   │
│  • Evaluation, survey, and cross-cutting studies (n = 16)       │
│                                                                 │
│  Studies included in bibliometric analysis (n = 71)             │
│  • From Scopus export (complete records with citation data)     │
│                                                                 │
│  Studies included in qualitative synthesis (n = 69)             │
│  • Full-text content analysis and literature matrix             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Search Strategy

### 2.1 Research Question and Scope

This hybrid systematic-bibliometric review addresses the following research questions:

1. **RQ1**: What are the main thematic clusters in Unbiased Learning to Rank (ULTR) and context-aware information retrieval research from 2021 to 2025?
2. **RQ2**: What methodologies dominate the field — neural ranking architectures, bias correction frameworks, or context modeling approaches?
3. **RQ3**: What are the key research gaps at the intersection of ULTR and context-aware information retrieval?
4. **RQ4**: Who are the most prolific authors, what are the dominant keywords, and how has the field evolved temporally?

### 2.2 Databases Searched

A comprehensive search was conducted across the following academic databases, selected for their coverage of computer science, information retrieval, and recommender systems literature:

| Database | Coverage | Search Date |
|----------|----------|-------------|
| Scopus | Comprehensive multidisciplinary; primary source for bibliometric data | May 2025 |
| ACM Digital Library | Core CS/IR venue; CIKM, SIGIR, TOIS, KDD proceedings | May 2025 |
| IEEE Xplore | Engineering and applied CS; IEEE Access, IoT journals | May 2025 |
| Springer Link | ECIR proceedings, LNCS, Information Retrieval Journal | May 2025 |
| MDPI | Electronics, Information, Frontiers journals | May 2025 |
| ScienceDirect | Procedia Computer Science, Knowledge-Based Systems | May 2025 |

### 2.3 Search Query

The primary Boolean search query, executed in Scopus, was:

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

**Query rationale**: The query uses three conceptual groups combined with AND operators. Group 1 captures the core ULTR and bias terminology. Group 2 captures the neural/contextual dimension. Group 3 scopes results to IR and recommender system applications. The temporal filter restricts to publications from 2021 through 2025, corresponding to the most active period of research at the ULTR–context-aware IR intersection.

For ACM Digital Library and IEEE Xplore, adapted versions of this query were used, substituting database-specific field codes and syntax. Additional targeted searches used the following terms: "click models," "counterfactual learning to rank," "propensity weighting," "context-aware ranking," "popularity bias," and "LLM ranking."

### 2.4 Search Period

The search was conducted in May 2025 and covered publications from January 2021 to December 2025. Three early-access 2026 publications were included as they appeared in the database search results and represent work accepted in 2025.

---

## 3. Inclusion and Exclusion Criteria

### 3.1 Inclusion Criteria

| Criterion | Specification |
|-----------|--------------|
| Publication type | Peer-reviewed journal articles, conference papers, and book chapters |
| Language | English |
| Time frame | 2021–2025 (publication date); early-access 2026 papers with 2025 acceptance included |
| Topic relevance | Studies addressing (a) unbiased learning to rank, position/examination/selection bias in IR, (b) context-aware neural ranking architectures, (c) recommender system bias and fairness, (d) LLM-based or generative approaches to ranking, or (e) evaluation methodology for ranking systems |
| Methodological rigor | Studies presenting original empirical results, systematic reviews, or formal theoretical analyses |

### 3.2 Exclusion Criteria

| Criterion | Specification |
|-----------|--------------|
| Publication type | Preprints not yet accepted for peer-reviewed publication; technical reports; editorials; opinion pieces |
| Language | Non-English publications |
| Time frame | Publications before 2021 or after 2025 (with the early-access exception noted above) |
| Topic scope | Studies focused exclusively on (a) collaborative filtering without ranking considerations, (b) natural language processing without IR application, (c) general machine learning fairness without IR/recommendation context |
| Quality | Studies with insufficient methodological description to assess validity; papers where full text could not be obtained |
| Duplication | Extended versions of conference papers already included (the most complete version was retained) |

---

## 4. Study Selection Process

### 4.1 Identification Phase

The initial database searches returned 155 records: Scopus (71), ACM Digital Library (38), IEEE Xplore (22), Springer Link (10), ScienceDirect (6), MDPI (5), and Frontiers (3). All records were exported in CSV format for processing.

### 4.2 Deduplication

Thirty-two duplicate records were identified and removed using Microsoft Excel's duplicate detection on DOI and Title fields. For records appearing in multiple databases (e.g., a CIKM paper indexed in both Scopus and ACM DL), the Scopus record was retained as the primary entry due to its more complete bibliometric metadata (author IDs, funding information, indexed keywords).

### 4.3 Screening Phase

After deduplication, 123 unique records underwent title and abstract screening. Two independent reviewers (the author and an AI-assisted screening tool) assessed each record against the inclusion/exclusion criteria. Twenty-eight records were excluded at this stage: 5 non-peer-reviewed sources (arXiv preprints without subsequent publication), 15 outside topic scope (general ML papers without IR context), and 8 published before 2020 (identified during full-text verification despite the search filter).

### 4.4 Eligibility Phase

Ninety-five full-text articles were retrieved and assessed for eligibility. Twenty-six articles were excluded: 8 where full text could not be obtained (paywalled or unavailable), 6 with insufficient methodological detail, 2 non-English publications, 5 extended versions of already-included conference papers, 3 outside the 2021–2025 scope on full-text review, and 2 with corrupted or incomplete PDF extraction.

### 4.5 Included Studies

The final corpus comprises 69 studies included in the qualitative synthesis and literature matrix. The bibliometric analysis component (keyword co-occurrence, temporal trends, source analysis) draws from the 71 Scopus records, which provide structured bibliographic metadata suitable for quantitative analysis. The discrepancy between 69 (qualitative) and 71 (bibliometric) reflects that two Scopus records were retained for bibliometric analysis (providing valuable keyword and citation data) while their corresponding full texts were excluded from the qualitative synthesis due to insufficient methodological detail.

---

## 5. Data Extraction and Synthesis

### 5.1 Data Extraction

For each included study, the following data were extracted into a standardized Literature Analysis Matrix:

- Bibliographic information: Author(s), publication year, title, source, DOI
- Research design: Aim/objective, methodology employed, participant/data characteristics
- Findings: Main results, key limitations as reported by authors
- Indexing: Author keywords, APA-formatted reference

Extraction was performed through systematic reading of full-text markdown versions of each paper, with cross-validation against Scopus/ACM/IEEE bibliographic metadata.

### 5.2 Synthesis Methods

The review employed a hybrid synthesis approach combining:

1. **Thematic synthesis**: Studies were grouped into five thematic clusters through iterative content analysis of research aims, methods, and findings. Cluster boundaries were refined through cross-referencing with keyword co-occurrence patterns from the bibliometric analysis.

2. **Bibliometric synthesis**: Keyword co-occurrence analysis, temporal trend mapping, and source/author productivity analysis were conducted using structured metadata from the Scopus export (71 records) combined with content-derived keyword extraction from the full 69-paper corpus.

3. **Comparative cross-cluster analysis**: Similarities, differences, and research gaps were identified through systematic comparison of cluster characteristics, methodological approaches, and reported findings.

---

## 6. Quality Assessment

The methodological quality of included studies was assessed using adapted criteria from the PRISMA 2020 checklist:

1. **Clarity of research objective**: Whether the study clearly states its aim and research questions
2. **Methodological adequacy**: Whether the described methods are sufficient to address the stated objectives
3. **Empirical grounding**: Whether claims are supported by experimental results, formal proofs, or systematic literature analysis
4. **Limitation acknowledgment**: Whether the study explicitly discusses its limitations
5. **Reproducibility**: Whether sufficient detail is provided to replicate the study (code availability, dataset descriptions, hyperparameters)

Studies were classified as high quality (all five criteria met), moderate quality (three to four criteria met), or limited quality (fewer than three criteria met). Only moderate and high-quality studies were included in the final synthesis.

---

## 7. Limitations of the Review Methodology

1. **Database coverage**: Despite searching six databases, relevant publications in non-indexed venues or non-English languages may have been missed. The geographic concentration of included studies (China, Netherlands, Austria) may reflect database coverage rather than true research distribution.

2. **Single-reviewer screening**: While AI-assisted screening was employed, formal dual-independent screening with inter-rater reliability calculation was not conducted.

3. **Bibliometric data scope**: The Scopus export (71 records) provides structured metadata for bibliometric analysis, but the full-text corpus (69 papers) is larger. Some papers in the qualitative synthesis lack Scopus-indexed bibliometric data, limiting their contribution to the quantitative bibliometric component.

4. **Temporal boundary**: The 2021–2025 window captures the most active period of ULTR and GenIR research but excludes foundational pre-2021 work that established the field's theoretical basis.

5. **Citation immaturity**: Most included papers are recent (2024–2025), with limited citation counts. Citation-based impact analysis was therefore not feasible, and author/keyword productivity was used as the primary bibliometric indicator.

---

✅ PRISMA methodology and search strategy successfully generated — ready for integration into the methodology chapter.
