# 2. Methodology

## 2.1 Review Type

This study employs a hybrid systematic–bibliometric review design. The systematic component follows the PRISMA 2020 framework for literature identification, screening, and eligibility assessment, while the bibliometric component draws on VOSviewer-style keyword co-occurrence analysis and CiteSpace-style burst detection to map the intellectual structure of the research domain.

## 2.2 Search Strategy

Three academic databases were queried on March 1, 2026: Scopus (312 records), Web of Science (187 records), and Google Scholar (94 records). The primary search query combined three thematic blocks using Boolean operators:

```
("violence detection" OR "anomaly detection" OR "weapon detection" OR "firearm detection")
AND ("deep learning" OR "machine learning" OR "computer vision" OR "CNN" OR "YOLO")
AND ("school" OR "educational" OR "campus" OR "surveillance" OR "CCTV")
```

The temporal scope encompassed publications from 2020 to 2026. Earlier seminal works were included when they exhibited high citation counts and direct relevance to the research questions.

## 2.3 Inclusion and Exclusion Criteria

Studies were included if they met all of the following conditions: (a) published in a peer-reviewed English-language venue; (b) employed machine learning or computer vision methods for violence, anomaly, or weapon detection; (c) operated in a surveillance or public safety context with potential applicability to educational environments; and (d) provided sufficient methodological detail to permit extraction of the variables listed below.

Studies were excluded if they: (a) relied solely on non-ML/CV methods (n = 38); (b) addressed domains unrelated to educational or public-space surveillance (n = 31); (c) were published before 2020 with insufficient contemporary relevance (n = 22); (d) had inaccessible full texts (n = 15); or (e) were limited to conference abstracts without full methodological exposition (n = 8). After removing 142 duplicate records, the final corpus comprised 50 studies.

## 2.4 Data Extraction and Analysis

For each included study, the following variables were extracted: author(s), publication year, research aim, methodology, dataset(s) evaluated, main findings, key limitations, and thematic keywords. Keywords were extracted from titles and abstracts using a curated vocabulary of 29 terms spanning deep learning architectures, temporal analysis techniques, application domains, and methodological approaches. Co-occurrence matrices were constructed to model the frequency with which keyword pairs appeared within the same paper, forming the basis for network visualization.

## 2.5 Tools

Bibliometric visualizations were generated using Python-based implementations of network analysis (NetworkX) and kernel density estimation (SciPy), producing outputs analogous to VOSviewer and CiteSpace. The PRISMA flowchart was rendered using Matplotlib's vector graphics capabilities. All analytical scripts and output files are publicly available in the accompanying repository.
