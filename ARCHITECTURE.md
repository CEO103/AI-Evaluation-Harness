# Architecture Overview

## Design Goal

The primary goal of this project is to build a modular AI evaluation harness that separates model execution from evaluation logic. The system is designed to measure output quality across multiple task types while remaining extensible and easy to maintain.

The focus is on evaluation infrastructure rather than model accuracy.

---

## High-Level Pipeline

tests.jsonl
→ Loader
→ Model Runner
→ Evaluator
→ Reporter
→ report.json + Console Output

---

## Module Breakdown

### 1. loader.py

Responsible for:
- Reading JSONL test files
- Parsing each line into structured test objects
- Handling malformed JSON safely

This isolates dataset handling from evaluation logic.

---

### 2. model.py

Implements a deterministic rule-based mock model.

Purpose:
- Provide reproducible outputs
- Avoid external dependencies
- Allow easy replacement with a real LLM API

The evaluation layer does not depend on how the model is implemented.

---

### 3. metrics.py

Contains task-specific evaluation logic:

- classification → exact match on label and urgency
- json_extraction → lightweight schema validation
- qa → fuzzy similarity scoring

Each metric is implemented independently to allow future extension.

---

### 4. evaluator.py

Acts as the orchestration layer.

Responsibilities:
- Invoke model
- Route to appropriate metric
- Determine pass/fail
- Capture failure reason
- Handle invalid schemas gracefully

This is the core evaluation engine.

---

### 5. reporter.py

Responsible for:
- Aggregating test results
- Computing summary statistics
- Generating task-level breakdown
- Writing structured JSON report
- Printing concise console summary

Reporting is intentionally separated from evaluation to maintain clean architecture.

---

## Design Principles

- Separation of concerns
- Deterministic evaluation
- Clear failure reasoning
- Minimal dependencies
- Extensibility

---

## Extensibility

The system can be extended by:

- Adding new task types
- Replacing the mock model with a real LLM
- Adding regression comparison between runs
- Adding additional metrics
- Integrating logging or CI pipelines

The architecture supports these changes without modifying core evaluation flow.
