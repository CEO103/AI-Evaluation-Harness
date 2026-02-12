# AI Evaluation Harness

This project implements a lightweight AI evaluation framework designed to measure model output quality across multiple AI task types.

The goal is to demonstrate how evaluation  infrastructure can be structured, modularized, and extended for real-world AI systems.

---

## Supported Task Types

### 1. Classification
Evaluates structured output with:
- label (string)
- urgency (string)

Uses exact match comparison.

### 2. JSON Extraction
Validates structured JSON output extracted from text.
Includes lightweight schema validation:
- required keys
- type checks
- structure validation

### 3. Question Answering (QA)
Evaluates answer strings using:
- case-insensitive comparison
- punctuation normalization
- fuzzy similarity scoring (0–1)

---

## CLI Usage

Run evaluation:

```bash
python eval.py run --tests tests.jsonl --output report.json

