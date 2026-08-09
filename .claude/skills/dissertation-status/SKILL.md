---
name: dissertation-status
description: Show the current completion status of all dissertation tasks by checking which output files exist. Use at the start of a session to see what has been done and what remains.
---

You are checking the status of all dissertation generation tasks.

**Project path**: `/Users/marioscordia/Desktop/disser/`

## Check These Files

Run a file existence check for each expected output and report the status.

### Expected Output Files

| Task | File | Status |
|------|------|--------|
| 2.4 | `bibliography.md` | ? |
| 3.1 | `matrix_literature.csv` | ? |
| 4a | `visualizations/vosviewer_keyword_network.png` | ? |
| 4b | `visualizations/vosviewer_overlay.png` | ? |
| 4c | `visualizations/vosviewer_density.png` | ? |
| 5a | `visualizations/citespace_burst_timeline.png` | ? |
| 5b | `visualizations/citespace_coauthorship.png` | ? |
| 5c | `visualizations/citespace_trend.png` | ? |
| 5d | `visualizations/citespace_keyword_freq.png` | ? |
| 6 | `visualizations/prisma_diagram.png` | ? |
| 7a | `top10_authors.csv` | ? |
| 7b | `top10_keywords.csv` | ? |
| 8 | `section_introduction.md` | ? |
| 9 | `section_methodology.md` | ? |
| 10 | `section_results.md` | ? |
| 11 | `section_discussion.md` | ? |
| 12 | `section_conclusion.md` | ? |
| — | `generate_visualizations.py` | ? |

## Instructions

1. Check existence of each file above using the Bash tool
2. Mark each as ✅ Done, ❌ Missing, or ⚠️ Exists but empty/small (<1KB)
3. Report the count: X/17 files complete
4. List the next recommended task to execute based on the execution order: Tasks 4+5+6 → 3.1 → 7 → 2.4 → 8 → 9 → 10 → 11 → 12

Output a clean status table, then a one-line recommendation for what to do next.
