---
name: deep-research
description: Deep analysis mode for extracting insights from the 50 research papers. Reads full paper text from prepared/ folder, synthesizes findings, identifies patterns, and answers specific research questions about the literature. Use when the user wants to understand what specific papers say about a method, dataset, or finding.
arguments: [query]
argument-hint: "[research question or topic to investigate]"
---

You are performing a deep research analysis across 50 reviewed papers in the project at `/Users/marioscordia/Desktop/disser/`.

**Research Topic**: "Computer Vision and Machine Learning Models for Detecting Safety Violations and Child Abuse in Educational Institutions"

## Your Task
The user wants to investigate: **$ARGUMENTS**

## Data Access
- **Paper metadata**: `sourcelist.csv` (Title, Authors, Year, Abstract in "Short description" column)
- **Full paper text**: `prepared/{n}/{n}.md` for papers 1–50
- **Citations**: `references.txt`

## Research Protocol

### Step 1: Identify Relevant Papers
Search `sourcelist.csv` for papers whose Title or Short description relate to the query.
List them with their paper number (row index + 1).

### Step 2: Deep Read
For the top 5–10 most relevant papers, read the corresponding `prepared/{n}/{n}.md` files.
Extract:
- Exact method/model used
- Dataset name, size, and source
- Reported accuracy / F1 / mAP / AUC
- Key innovations described by the authors
- Explicitly stated limitations

### Step 3: Synthesise
Identify:
- **Consensus**: what most papers agree on
- **Disagreements**: conflicting findings or approaches
- **Gaps**: what is not addressed by any paper
- **Best performers**: which methods/datasets achieve highest reported metrics

## Output Format

```markdown
## Deep Research: [your query]

### Papers Analysed
| # | Authors | Year | Title (short) | Relevance |
|---|---------|------|---------------|-----------|

### Key Findings

#### [Theme 1]
[Paragraph synthesising evidence from 2–4 papers with inline citations]

#### [Theme 2]
...

### Consensus View
[1–2 sentences on what the field generally agrees on]

### Open Questions / Gaps
- [gap 1]
- [gap 2]

### Recommended Papers for Further Reading
[Top 3 most informative papers on this topic]
```

Write in academic English. Back all claims with paper numbers or [Author, Year].
