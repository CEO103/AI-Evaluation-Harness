# metrics.py
import string
from difflib import SequenceMatcher


#for classification metrics
def classification_metrics(expected: dict, actual: dict) -> dict:
    label_match = expected.get("label") == actual.get("label")
    urgency_match = expected.get("urgency") == actual.get("urgency")

    return {
        "label_match": label_match,
        "urgency_match": urgency_match,
        "exact_match": label_match and urgency_match
    }


#for json extraction metrics
def json_schema_validation(actual: dict) -> dict:
    if not isinstance(actual, dict):
        return {"schema_valid": False, "reason": "Output is not a dictionary"}

    if "items" not in actual:
        return {"schema_valid": False, "reason": "Missing key: items"}

    if not isinstance(actual["items"], list):
        return {"schema_valid": False, "reason": "items must be a list"}

    for item in actual["items"]:
        if not isinstance(item, dict):
            return {"schema_valid": False, "reason": "Item must be a dictionary"}
        if "name" not in item or "qty" not in item:
            return {"schema_valid": False, "reason": "Missing name or qty in item"}
        if not isinstance(item["qty"], int):
            return {"schema_valid": False, "reason": "qty must be integer"}

    return {"schema_valid": True}


# for QA metrics
def normalize(text: str) -> str:
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))


def qa_similarity(expected: str, actual: str) -> float:
    expected_n = normalize(expected)
    actual_n = normalize(actual)
    return SequenceMatcher(None, expected_n, actual_n).ratio()
