---
name: academic-paper
description: Write a dissertation section (introduction, methodology, results, discussion, or conclusion) in Scopus Q1/Q2 academic English style. Use when the user asks to write or draft any section of the review article.
arguments: [section]
argument-hint: "[section: introduction|methodology|results|discussion|conclusion]"
---

You are writing a section of a peer-reviewed systematic review article for a Scopus Q1/Q2 journal. The research topic is:

**"Computer Vision and Machine Learning Models for Detecting Safety Violations and Child Abuse in Educational Institutions"**

## Context
- 50 papers reviewed (2022–2026), sourced from Scopus and Web of Science
- Bibliometric tools used: VOSviewer (keyword co-occurrence), CiteSpace (burst analysis), PRISMA (selection flowchart)
- Methods in the literature: YOLO, CNN+LSTM, 3D CNN, attention mechanisms, optical flow, ResNet, MobileNet, GRU, autoencoders
- Datasets: school/campus CCTV footage, publicly available violence/anomaly detection datasets
- Key themes: real-time detection, edge deployment, privacy, dataset scarcity

## Section to Write
The user wants the **$0** section.

## Style Rules
- Academic English only; formal register, no contractions
- Cite sources as [Author, Year] inline (use authors from sourcelist.csv / references.txt)
- Use hedging language where appropriate: "suggests", "indicates", "highlights", "demonstrates"
- Results section: facts only, verbs like "shows", "presents", "identifies", "lists"
- Discussion section: interpretation, compare methods, address limitations and future directions
- No bullet lists in the body text — use flowing paragraphs
- Every claim about the literature must be backed by a citation
- Do not mention AI tools or automated generation

## Word Count Targets
| Section | Target |
|---------|--------|
| introduction | 500–600 words |
| methodology | ~300 words |
| results | 800–1000 words |
| discussion | 600–800 words |
| conclusion | 300–400 words |

## Required Structure Per Section

**introduction**: (1) relevance of topic, (2) brief overview citing 5–7 papers, (3) gap identification, (4) research aim and questions, (5) article structure

**methodology**: review type → databases → search query → time range → inclusion/exclusion criteria → tools (VOSviewer, CiteSpace, PRISMA) → data extraction variables

**results**: subsections 10.1 Publication Trends, 10.2 Keyword Co-occurrence, 10.3 Thematic Clusters, 10.4 Top Authors and Journals, 10.5 Citation Burst Analysis, 10.6 Literature Matrix Summary

**discussion**: interpret results, compare with prior reviews, highlight effective methods, discuss limitations (datasets, real-world deployment, privacy), future directions (multimodal fusion, explainability, edge/lightweight models)

**conclusion**: summarize review, key findings, practical significance, review limitations, future research (3–4 sentences), strong closing statement

Write the section now. Output the section as clean Markdown with proper headings.
