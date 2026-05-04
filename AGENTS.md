# Agent Instructions for Dissertation Project

This document provides context and guidelines for AI coding agents working on this repository.

## Project Overview
This repository contains utility scripts and data files for automating the processing of research papers, generating citations, and maintaining a source list for a dissertation.

## Tech Stack & Dependencies
- **Python 3**: Used for CSV manipulation (`merge_csv.py`) and PDF processing (`prepare.py`).
  - Key library: `pymupdf4llm` (used in `prepare.py` for PDF to Markdown conversion).
- **Node.js**: Used for bulk citation fetching (`index.js`).
- **Data Formats**: CSV (`sourcelist.csv`), Plain Text (DOIs/citations), Markdown (extracted papers).

## Core Scripts and Workflows
1. **Adding New Literature (`merge_csv.py`)**
   - **Purpose**: Merges a new export CSV (e.g., `second-export.csv`) into the main database (`ranked list of resources - sourcelist.csv`).
   - **Behavior**: Checks for duplicate DOIs/Titles. For new items, it calls the `citeas.org` API to fetch APA citations, appends the new rows to the main CSV, and respects API rate limits (0.5s sleep).
2. **Bulk Citation Fetching (`index.js`)**
   - **Purpose**: Reads a hardcoded list of DOIs and fetches their APA citations via the `citeas.org` API, writing the output to `references.txt`.
3. **PDF to Markdown Extraction (`prepare.py`)**
   - **Purpose**: Scans the `all/` directory for PDF files. For each PDF, it creates a folder in `prepared/`, copies the PDF, and uses `pymupdf4llm` to extract the text into a `.md` file along with any images.

## AI Agent Guidelines
- **API Rate Limiting**: Whenever modifying or adding scripts that interact with `citeas.org` or similar APIs, ALWAYS include rate-limiting (e.g., `time.sleep(0.5)`) to prevent IP bans.
- **Data Integrity**: Be extremely careful when modifying `ranked list of resources - sourcelist.csv`. Always append or safely edit; avoid truncating or losing existing manual entries.
- **Paths**: Assume PDF inputs are in `all/` and outputs go to `prepared/`. 
- **Dependencies**: If you add new Python libraries, make sure to document them.
