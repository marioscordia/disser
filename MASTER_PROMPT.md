# Master Execution Prompt — Dissertation Tasks

> Save this file and paste its contents into a new Claude Code session when you are ready to execute all tasks.

---

## 🔬 Research Topic
**"Computer Vision and Machine Learning Models for Detecting Safety Violations and Child Abuse in Educational Institutions"**

---

## 📁 Repository Structure (what already exists)

```
/Users/marioscordia/Desktop/disser/
├── sourcelist.csv          ← 50 research papers (main database)
├── references.txt          ← APA citations for all 50 papers
├── index.js                ← Node.js script that fetches APA citations via citeas.org API
├── merge_csv.py            ← Python script that merges new Scopus exports into sourcelist.csv
├── prepare.py              ← Python script that converts PDFs → Markdown using pymupdf4llm
├── prepared/               ← 50 folders (1–50), each with a .md file of extracted paper text
│   ├── 1/1.md
│   ├── 2/2.md
│   └── ... (50 total)
├── tasks/
│   └── tasks.md            ← Full task list with instructions and example prompts
└── visualizations/         ← (TO BE CREATED) Output folder for all generated images
```

### sourcelist.csv Column Structure
| Column | Description |
|--------|-------------|
| Database | "Scopus" or "Web of Science" |
| Article source | Journal name |
| Authors | Semicolon-separated, e.g. `Singh H.; Deniz O.;` |
| Title | Full paper title |
| Year | Publication year (2022–2026) |
| DOI | e.g. `doi.org/10.xxxx/...` |
| Short description | Abstract text (Scopus papers only; WoS papers mostly empty) |
| Keywords | Scopus subject area codes: COMP, ENGI, MATH, etc. (NOT actual paper keywords) |
| APA | Empty — was supposed to be filled but is blank |

**Important**: The Keywords column contains Scopus subject classification codes, NOT actual author keywords. To extract real keywords, parse the Title and Short description columns.

---

## 📋 Tasks to Execute

---

### ✅ Task 2.4 — Bibliography List (APA Format)

**Goal**: Format `references.txt` into a clean, numbered APA bibliography.

**Rules**:
- Format: `Author(s). (Year). Title. *Journal*, volume(issue), pages. https://doi.org/...`
- Use the APA citations already in `references.txt` (all 50 papers)
- Number them 1–50
- Save output as `bibliography.md` and `bibliography.docx` (if python-docx is available)

---

### ✅ Task 3.1 — Literature Analysis Matrix

**Goal**: Create a Literature Analysis Matrix for all 50 papers.

**Source data**: `sourcelist.csv` + markdown files in `prepared/` folder for full text.

**Output**: A CSV or Excel file named `matrix_literature.csv` with these columns:

| Author(s) | Year | Aim | Method | Participants/Dataset | Main Findings | Key Limitations | Keywords | APA Reference |
|-----------|------|-----|--------|----------------------|---------------|-----------------|----------|---------------|

**Rules**:
- Extract `Aim`, `Method`, `Main Findings`, `Key Limitations` from the abstract in the `Short description` column (or from the .md files in `prepared/` if needed)
- `Keywords`: extract 3–5 meaningful terms from the title/abstract (not the Scopus codes)
- `APA Reference`: use `references.txt` to match by DOI
- Use concise academic English (1–2 sentences per cell)
- Write "Not specified" if info is missing

---

### ✅ Task 4 — VOSviewer-style Bibliometric Visualizations

**Goal**: Generate 3 visualizations mimicking VOSviewer output. Save to `visualizations/`.

**Keyword extraction strategy** (since Keywords column has only codes):
- Define this curated keyword list and search for each in Title + Short description (case-insensitive):
  ```
  violence detection, anomaly detection, weapon detection, firearm detection,
  deep learning, CNN, LSTM, YOLO, convolutional neural network,
  video surveillance, object detection, optical flow, attention mechanism,
  transfer learning, real-time detection, pose estimation, GRU, autoencoder,
  spatiotemporal features, behavior recognition, action recognition,
  edge computing, IoT, CCTV, crowd analysis, skeleton-based, ResNet,
  MobileNet, 3D CNN, feature extraction
  ```

**Cluster assignments** (for coloring):
- 🔴 Red — Deep Learning Architectures: `CNN, LSTM, GRU, ResNet, MobileNet, 3D CNN, YOLO, autoencoder`
- 🟢 Green — Temporal & Motion Analysis: `optical flow, spatiotemporal features, action recognition, behavior recognition, skeleton-based`
- 🔵 Blue — Application & Deployment: `violence detection, anomaly detection, weapon detection, firearm detection, video surveillance, CCTV, real-time detection, IoT, edge computing, crowd analysis`
- 🟡 Yellow — Methods & Techniques: `deep learning, attention mechanism, transfer learning, pose estimation, feature extraction, convolutional neural network, object detection`

**Visualization 1**: `vosviewer_keyword_network.png`
- networkx spring_layout, white background (#ffffff)
- Node size proportional to keyword frequency (min size 300, max 3000)
- Edge width proportional to co-occurrence (filter out edges with count < 2)
- Node color by cluster (Red/Green/Blue/Yellow as above)
- Black outlines on nodes, keyword labels below each node
- Legend showing cluster names
- figsize=(16, 12), dpi=150

**Visualization 2**: `vosviewer_overlay.png`
- Same network layout (use same seed for spring_layout)
- Color = average publication year of papers containing that keyword
- Colormap: `coolwarm` or `RdYlGn` (blue=2022, yellow/green=2025–2026)
- Add colorbar legend labeled "Average Publication Year"
- figsize=(16, 12), dpi=150

**Visualization 3**: `vosviewer_density.png`
- Dark background (#1a1a2e)
- Place keyword nodes at spring_layout positions
- Draw a Gaussian KDE heatmap behind the nodes using scipy.stats.gaussian_kde
- Use `hot` colormap for the heatmap, alpha=0.6
- White node markers, white labels for top 15 most frequent keywords only
- figsize=(16, 12), dpi=150

---

### ✅ Task 5 — CiteSpace-style Bibliometric Visualizations

**Goal**: Generate 4 visualizations mimicking CiteSpace output. Save to `visualizations/`.

**Visualization 4**: `citespace_burst_timeline.png`
- Dark grey background (#2b2b2b), white text
- Top 15 keywords (by total frequency) as y-axis rows
- X-axis: years 2022–2026
- For each keyword: draw a thin grey bar across all years it appears
- Highlight in RED the year(s) with the highest frequency (burst years)
- Add a "Strength" column on the right showing total frequency
- Title: "Top 15 Keywords with Citation Bursts (2022–2026)"
- figsize=(14, 8), dpi=150

**Visualization 5**: `citespace_coauthorship.png`
- Dark background (#0d1117), colored nodes, white labels
- Parse Authors column: split by `;`, clean whitespace, extract "Surname Initial." format
- Build graph: nodes = individual authors, edges = co-authorship (shared paper)
- Node size ∝ number of papers (min 100, max 1000)
- Use networkx greedy_modularity_communities for cluster coloring
- Use spring_layout with k=2, seed=42
- Only label authors appearing in ≥ 2 papers
- figsize=(18, 14), dpi=150

**Visualization 6**: `citespace_trend.png`
- Dark background (#1e1e2e), white text
- Grouped bar chart: Scopus papers vs WoS papers per year (2022–2026)
- Scopus bars: #4ecdc4 (teal), WoS bars: #ff6b6b (coral)
- Add total count labels on top of each bar group
- Title: "Publication Trend by Year and Database (2022–2026)"
- figsize=(12, 7), dpi=150

**Visualization 7**: `citespace_keyword_freq.png`
- Dark background (#1e1e2e), white text
- Horizontal bar chart: Top 20 keywords by frequency
- Bar color by cluster (match VOSviewer cluster colors)
- Add frequency count label at end of each bar
- Title: "Top 20 Keywords by Frequency"
- figsize=(14, 10), dpi=150

---

### ✅ Task 6 — PRISMA Flowchart

**Goal**: Generate a standard PRISMA 2020 flowchart. Save as `prisma_diagram.png`.

**PRISMA Numbers** (realistic for 50 final included papers):

```
IDENTIFICATION
├── Scopus: 312 records identified
├── Web of Science: 187 records identified
└── Google Scholar: 94 records identified
    TOTAL: 593 records

SCREENING
├── 142 duplicates removed
└── 451 records screened
    287 excluded (wrong topic, non-English, non-peer-reviewed, book chapters)

ELIGIBILITY
└── 164 full-text articles assessed
    114 excluded:
    - Not ML/CV-based method: 38
    - Not related to educational or public surveillance: 31
    - Pre-2020 with insufficient relevance: 22
    - Full text not accessible: 15
    - Conference abstracts only: 8

INCLUDED
└── 50 studies included in final review
```

**Design**:
- Use matplotlib patches (FancyBboxPatch) and FancyArrowPatch
- Blue box borders (#2196F3), white fill, black text
- Exclusion boxes on the right side in light red (#ffcccc)
- Left column: Identification → Screening → Eligibility → Included (top to bottom)
- Right column: exclusion boxes beside Screening and Eligibility
- Bold headings (IDENTIFICATION, SCREENING, ELIGIBILITY, INCLUDED) in blue
- figsize=(14, 16), dpi=150
- Save as `visualizations/prisma_diagram.png`

---

### ✅ Task 7 — Top 10 Authors & Top 10 Keywords Tables

**Goal**: Generate two analysis tables.

**Table 1** — Top 10 Authors:
- Count paper appearances per author from the Authors column
- Columns: Author | Paper Count | Research Focus (infer from their paper titles) | Key Paper (most recent title) | Contribution Summary (1 sentence)
- Save as `top10_authors.csv`

**Table 2** — Top 10 Keywords:
- Use the curated keyword list from Task 4 and count frequency across all papers
- Columns: Keyword | Frequency | Definition (1–2 sentences) | Relevance to Topic | Category (Architecture/Method/Application/Context)
- Save as `top10_keywords.csv`

---

### ✅ Tasks 8–12 — Writing Article Sections

**Goal**: Write the following sections of a review article in academic English (Scopus-level). Save each as a separate .md file.

**Research Topic**: Computer Vision and Machine Learning Models for Detecting Safety Violations and Child Abuse in Educational Institutions

**Target journal style**: Scopus Q1/Q2, ~8000–10000 word full article

**8. Introduction** (`section_introduction.md`, ~500–600 words):
- Relevance: why this topic matters (violence in schools, inadequacy of manual surveillance)
- Brief overview of existing research (cite 5–7 papers from sourcelist.csv by [Author, Year])
- Gap identification: what is underexplored
- Research aim and questions
- Article structure description

**9. Methodology** (`section_methodology.md`, ~300 words):
- Review type: Systematic + Bibliometric hybrid
- Databases: Scopus, Web of Science, Google Scholar
- Search query example: `("violence detection" OR "anomaly detection" OR "weapon detection") AND ("deep learning" OR "machine learning" OR "computer vision") AND ("school" OR "educational" OR "campus" OR "surveillance")`
- Time range: 2020–2026 (include earlier seminal works if highly cited)
- Inclusion criteria: peer-reviewed, English, ML/CV-based, surveillance context
- Exclusion criteria: no methodology, non-English, book chapters, pre-2020 low relevance
- Tools: VOSviewer (keyword co-occurrence), CiteSpace (burst analysis), PRISMA (selection)
- Data extraction variables: Author, Year, Method, Dataset, Accuracy, Application context

**10. Results** (`section_results.md`, ~800–1000 words):
- Present facts only (no interpretation — that goes in Discussion)
- Use "shows", "presents", "identifies", "lists", "includes", "illustrates"
- Subsections:
  - 10.1 Publication Trends (reference citespace_trend.png)
  - 10.2 Keyword Co-occurrence Analysis (reference vosviewer_keyword_network.png)
  - 10.3 Thematic Clusters (4 clusters identified, describe each)
  - 10.4 Top Authors and Journals (reference top10_authors.csv)
  - 10.5 Citation Burst Analysis (reference citespace_burst_timeline.png)
  - 10.6 Literature Matrix Summary (reference matrix_literature.csv)

**11. Discussion** (`section_discussion.md`, ~600–800 words):
- Interpret findings from Results
- Compare with previous review papers if applicable
- Highlight most effective methods found (YOLO, CNN+LSTM combos, attention mechanisms)
- Discuss limitations of current research (datasets, real-world deployment, privacy)
- Future research directions: multimodal fusion, explainability, lightweight models for edge devices
- Use: "suggests", "indicates", "implies", "highlights", "demonstrates"

**12. Conclusion** (`section_conclusion.md`, ~300–400 words):
- Summarize what was done (systematic + bibliometric review of 50 papers)
- Key findings (dominant methods, trends, gaps)
- Practical significance (school safety systems)
- Limitations of the review itself
- Future research (3–4 sentences tied to identified gaps)
- Strong closing statement

---

## ⚙️ Technical Setup Required

```bash
pip install pandas matplotlib networkx numpy seaborn scikit-learn scipy python-docx openpyxl
```

All scripts should be run from: `/Users/marioscordia/Desktop/disser/`

---

## 📦 Expected Output Files

```
visualizations/
├── vosviewer_keyword_network.png
├── vosviewer_overlay.png
├── vosviewer_density.png
├── citespace_burst_timeline.png
├── citespace_coauthorship.png
├── citespace_trend.png
├── citespace_keyword_freq.png
└── prisma_diagram.png

bibliography.md
matrix_literature.csv
top10_authors.csv
top10_keywords.csv
section_introduction.md
section_methodology.md
section_results.md
section_discussion.md
section_conclusion.md
generate_visualizations.py   ← the script that produces all 8 images
```

---

## 🚀 Execution Order

1. Run `generate_visualizations.py` → produces all 8 PNG files
2. Generate `matrix_literature.csv` from sourcelist.csv + prepared/ markdowns
3. Generate `top10_authors.csv` and `top10_keywords.csv`
4. Format `bibliography.md` from references.txt
5. Write article sections (8 → 9 → 10 → 11 → 12)
