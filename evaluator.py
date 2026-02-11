# evaluator.py
from model import run_model
from metrics import (
    classification_metrics,
    json_schema_validation,
    qa_similarity,
)

SIMILARITY_THRESHOLD = 0.8


def evaluate_test(test: dict) -> dict:
    task = test.get("task")
    input_text = test.get("input")
    expected = test.get("expected")

    try:
        actual = run_model(task, input_text)
    except Exception as e:
        return {
            "id": test.get("id"),
            "task": task,
            "input": input_text,
            "expected": expected,
            "actual": None,
            "metrics": {},
            "passed": False,
            "reason": f"Model execution failed: {str(e)}",
        }

    passed = False
    metrics = {}
    reason = None

    # for classification 
    if task == "classification":
        if not isinstance(expected, dict):
            return {
                "id": test.get("id"),
                "task": task,
                "input": input_text,
                "expected": expected,
                "actual": actual,
                "metrics": {},
                "passed": False,
                "reason": "Expected must be dict for classification",
            }

        metrics = classification_metrics(expected, actual)
        passed = metrics["exact_match"]

        if not passed:
            reason = "Classification mismatch"

    # for JSON extraction

    elif task == "json_extraction":
        metrics = json_schema_validation(actual)
        passed = metrics["schema_valid"]

        if not passed:
            reason = metrics.get("reason")

    #for QA
    
    elif task == "qa":

        # Handle dict-style expected automatically
        if isinstance(expected, dict):
            
            if "answer" in expected:
                expected = expected["answer"]
            else:
                return {
                    "id": test.get("id"),
                    "task": task,
                    "input": input_text,
                    "expected": expected,
                    "actual": actual,
                    "metrics": {},
                    "passed": False,
                    "reason": "QA expected must be string or contain 'answer' key",
                }

        if not isinstance(expected, str):
            return {
                "id": test.get("id"),
                "task": task,
                "input": input_text,
                "expected": expected,
                "actual": actual,
                "metrics": {},
                "passed": False,
                "reason": "QA expected must be string",
            }

        score = qa_similarity(expected, actual)
        metrics = {"similarity": round(score, 3)}
        passed = score >= SIMILARITY_THRESHOLD

        if not passed:
            reason = f"Low similarity score: {score:.3f}"

    #for unknown task
    else:
        reason = f"Unsupported task type: {task}"

    return {
        "id": test.get("id"),
        "task": task,
        "input": input_text,
        "expected": expected,
        "actual": actual,
        "metrics": metrics,
        "passed": passed,
        "reason": reason,
    }
