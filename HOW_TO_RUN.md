# How To Run

## Requirements

- Python 3.9+
- No external paid APIs required

---

## Step 1: Prepare Dataset

Ensure test cases are in JSON Lines format (one JSON object per line).

Example:

{
  "id": "TC001",
  "task": "classification",
  "input": "The app crashes on login screen",
  "expected": {
    "label": "bug_report",
    "urgency": "high"
  }
}

---

## Step 2: Run Evaluation

```bash
python eval.py run --tests tests.jsonl --output report.json
