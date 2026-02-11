# eval.py
import argparse
from loader import load_tests
from evaluator import evaluate_test
from reporter import generate_report


def main():
    parser = argparse.ArgumentParser(description="AI Evaluation Harness")

    parser.add_argument("run", help="Run evaluation")
    parser.add_argument("--tests", required=True, help="Path to tests.jsonl")
    parser.add_argument("--output", required=True, help="Path to output report.json")

    args = parser.parse_args()

    tests = load_tests(args.tests)

    results = []
    for test in tests:
        result = evaluate_test(test)
        results.append(result)

    generate_report(results, args.output)


if __name__ == "__main__":
    main()
