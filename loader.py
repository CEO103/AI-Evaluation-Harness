# loader.py
import json
from typing import List, Dict

def load_tests(file_path: str) -> List[Dict]:
    tests = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            try:
                tests.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                print(f"Invalid JSON at line {line_number}")
    return tests
