# Assumptions

## 1. Dataset Format

- Input file is in JSON Lines (JSONL) format.
- Each line contains one complete test case.
- Each test case includes:
  - id
  - task
  - input
  - expected

Malformed JSON lines are skipped and reported gracefully.

---

## 2. Supported Task Types

The harness supports exactly three task types:

- classification
- json_extraction
- qa

Any unsupported task type results in a structured failure.

---

## 3. Model Behavior

- The model is rule-based and deterministic.
- Accuracy is not the objective of this assignment.
- Focus is on evaluation correctness and reporting.

---

## 4. Evaluation Logic

### Classification
- Exact match required for both label and urgency.

### JSON Extraction
- Output must be a dictionary.
- Must contain required keys.
- Basic type validation is enforced.
- Full JSON Schema validation is intentionally not implemented.

### QA
- Case-insensitive comparison.
- Punctuation ignored.
- Similarity score computed between 0 and 1.
- Pass threshold set to 0.8.

---

## 5. Reporting

- Pass rate is computed as passed / total.
- Task-level breakdown is calculated independently.
- All failures include expected, actual, metrics, and reason.

---

## 6. Scope Limitations

The following are intentionally out of scope:

- Real LLM integration
- Asynchronous execution
- Persistent storage
- Regression comparison across runs
- Advanced schema validation libraries

These can be added in future iterations.
