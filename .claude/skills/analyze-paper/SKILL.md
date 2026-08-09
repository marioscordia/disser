---
name: analyze-paper
description: Extract structured data from a single paper for the literature analysis matrix. Reads the prepared markdown file and returns a filled matrix row. Use when populating matrix_literature.csv row by row.
arguments: [paper_number]
argument-hint: "[paper number 1–50]"
---

You are extracting structured data from research paper #$0 for the dissertation literature analysis matrix.

**Project path**: `/Users/marioscordia/Desktop/disser/`

## Steps

1. Read `sourcelist.csv` row #$0 to get: Authors, Title, Year, DOI, Short description (abstract)
2. Read `prepared/$0/$0.md` for the full paper text
3. Extract the following fields:

| Field | Extraction Guide |
|-------|-----------------|
| **Author(s)** | From CSV Authors column; format as "Surname A., Surname B." |
| **Year** | From CSV Year column |
| **Aim** | What research problem does the paper address? 1–2 sentences from abstract/intro |
| **Method** | Specific model or algorithm used (e.g., "YOLOv5 + LSTM attention", "3D CNN with optical flow") |
| **Participants/Dataset** | Dataset name, number of videos/images, source (public/custom/school CCTV) |
| **Main Findings** | Best reported metric (accuracy/F1/mAP) and the key contribution. 1–2 sentences |
| **Key Limitations** | Explicitly stated or clearly implied limitations. 1–2 sentences |
| **Keywords** | 3–5 meaningful terms from title+abstract (NOT Scopus codes) |
| **APA Reference** | Match by DOI in `references.txt` and paste the full APA citation |

## Output Format

Return a single filled CSV row, then the same data as a readable table:

**CSV row** (comma-separated, quoted fields):
```
"Author(s)","Year","Aim","Method","Participants/Dataset","Main Findings","Key Limitations","Keywords","APA Reference"
```

**Readable table**:
| Field | Value |
|-------|-------|
| Author(s) | ... |
| Year | ... |
| Aim | ... |
| Method | ... |
| Participants/Dataset | ... |
| Main Findings | ... |
| Key Limitations | ... |
| Keywords | ... |
| APA Reference | ... |

If a field cannot be determined from either source, write `Not specified`.
