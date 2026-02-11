# model.py
import re


def run_model(task: str, input_text: str):
    """
    Mock model implementation.
    Returns:
      - dict for classification/json_extraction
      - string for qa
    """

    if task == "classification":
        text = input_text.lower()

        if "crash" in text or "error" in text:
            return {"label": "bug_report", "urgency": "high"}
        elif "payment" in text or "billing" in text:
            return {"label": "billing_issue", "urgency": "medium"}
        else:
            return {"label": "general_query", "urgency": "low"}

    elif task == "json_extraction":
        # Example: "Order 2 pizzas and 1 coke"
        items = []
        matches = re.findall(r"(\d+)\s(\w+)", input_text.lower())

        for qty, name in matches:
            items.append({
                "name": name.rstrip("s"),
                "qty": int(qty)
            })

        return {"items": items}

    elif task == "qa":
        # For mock purposes, return input text
        return input_text

    else:
        raise ValueError(f"Unsupported task type: {task}")
