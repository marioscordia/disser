---
name: academic-pipeline
description: Execute all pending dissertation generation tasks in the correct order. Produces visualizations, matrix, bibliography, top-10 tables, and article sections. Use when the user wants to run the full pipeline or a specific task by number.
arguments: [task]
argument-hint: "[task: all | 2.4 | 3.1 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12]"
---

You are executing dissertation generation tasks for the project at `/Users/marioscordia/Desktop/disser/`.

**Research Topic**: "Computer Vision and Machine Learning Models for Detecting Safety Violations and Child Abuse in Educational Institutions"

## Task Registry

| Task | Output | Description |
|------|--------|-------------|
| 2.4 | `bibliography.md` | Numbered APA bibliography from references.txt |
| 3.1 | `matrix_literature.csv` | Literature analysis matrix (50 papers) |
| 4 | `visualizations/vosviewer_*.png` (3 files) | VOSviewer-style keyword visualizations |
| 5 | `visualizations/citespace_*.png` (4 files) | CiteSpace-style bibliometric visualizations |
| 6 | `visualizations/prisma_diagram.png` | PRISMA 2020 flowchart |
| 7 | `top10_authors.csv`, `top10_keywords.csv` | Top 10 author and keyword tables |
| 8 | `section_introduction.md` | Introduction section (~500–600 words) |
| 9 | `section_methodology.md` | Methodology section (~300 words) |
| 10 | `section_results.md` | Results section (~800–1000 words) |
| 11 | `section_discussion.md` | Discussion section (~600–800 words) |
| 12 | `section_conclusion.md` | Conclusion section (~300–400 words) |

## Execution Rules

**If task argument is `all` or not provided**: execute tasks in this exact order: 4 → 5 → 6 → 3.1 → 7 → 2.4 → 8 → 9 → 10 → 11 → 12

**If a specific task number is given**: execute only that task.

## Key Data Sources
- `sourcelist.csv` — 50 papers: columns Database, Article source, Authors, Title, Year, DOI, Short description, Keywords (= Scopus codes, NOT real keywords), APA (empty)
- `references.txt` — 50 APA citations, one per blank-line-separated block
- `prepared/1/1.md` through `prepared/50/50.md` — full paper text in Markdown

## Critical Implementation Notes

### Keyword Extraction (Tasks 3.1, 4, 5, 7)
The Keywords column contains only Scopus subject codes (COMP, ENGI, etc.) — NOT real keywords.
Extract real keywords by searching Title + Short description for these terms (case-insensitive):
```
violence detection, anomaly detection, weapon detection, firearm detection,
deep learning, CNN, LSTM, YOLO, convolutional neural network,
video surveillance, object detection, optical flow, attention mechanism,
transfer learning, real-time detection, pose estimation, GRU, autoencoder,
spatiotemporal features, behavior recognition, action recognition,
edge computing, IoT, CCTV, crowd analysis, skeleton-based, ResNet,
MobileNet, 3D CNN, feature extraction
```

### Cluster Colors (Tasks 4, 5, 7)
- Red `#e74c3c`: CNN, LSTM, GRU, ResNet, MobileNet, 3D CNN, YOLO, autoencoder
- Green `#2ecc71`: optical flow, spatiotemporal features, action recognition, behavior recognition, skeleton-based
- Blue `#3498db`: violence detection, anomaly detection, weapon detection, firearm detection, video surveillance, CCTV, real-time detection, IoT, edge computing, crowd analysis
- Yellow `#f1c40f`: deep learning, attention mechanism, transfer learning, pose estimation, feature extraction, convolutional neural network, object detection

### Visualizations (Tasks 4, 5, 6)
Write/run `generate_visualizations.py` from `/Users/marioscordia/Desktop/disser/`.
Required packages: `pip install pandas matplotlib networkx numpy scipy`
Use `seed=42` for all spring_layout calls so layouts are reproducible.

### PRISMA Numbers (Task 6)
- Identification: Scopus=312, WoS=187, Google Scholar=94 → Total=593
- Duplicates removed: 142 → 451 screened
- Excluded at screening: 287 → 164 assessed for eligibility
- Excluded at eligibility: 114 (not ML/CV=38, not education/surveillance=31, pre-2020=22, no full text=15, abstract only=8)
- Included: 50

## Begin Execution

The user requested task: **$0**

Start now. For code-based tasks (4, 5, 6), write the Python script and run it. For writing tasks (8–12), use the `/academic-paper` skill guidelines. Confirm completion of each task before moving to the next.
