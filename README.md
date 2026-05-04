# Dissertation Research Tools

This repository contains various scripts and data files to automate the tedious parts of gathering, tracking, and parsing research literature for a dissertation.

## Key Features & Scripts

### 1. Literature Database Management (`merge_csv.py`)
A Python script that merges new research exports (e.g., `second-export.csv` from Scopus) into the primary tracking database (`ranked list of resources - sourcelist.csv`). 
- **Deduplication:** Ensures existing DOIs or titles are not duplicated.
- **Auto-Citation:** Automatically fetches the APA citation for new records using the `citeas.org` API before appending them.

### 2. PDF to Markdown Parsing (`prepare.py`)
A Python script that converts academic PDFs into Markdown format, making them easier to query or feed into LLMs.
- **Input:** Place PDFs in the `all/` directory.
- **Output:** Generates a folder for each PDF in the `prepared/` directory containing the extracted `.md` text and an `images/` subfolder for associated images. It reads directly from the `all/` directory without copying the PDF.
- **Requires:** `pymupdf4llm`

### 3. Bulk Citation Fetcher (`index.js`)
A Node.js utility script for bulk-fetching APA citations from a hardcoded list of DOIs using the `citeas.org` API.
- Results are saved to a `references.txt` file.

## Setup & Usage

**Prerequisites:**
- Python 3.x
- Node.js
- `pip install pymupdf4llm`

**Running the Tools:**
- Merge new CSV exports: `python merge_csv.py`
- Prepare PDFs: `python prepare.py`
- Fetch citations from JS array: `node index.js`
