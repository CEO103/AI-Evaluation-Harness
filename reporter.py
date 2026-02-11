# reporter.py
import json
from collections import defaultdict


def generate_report(results: list, output_path: str):
    total = len(results)
    passed = sum(r["passed"] for r in results)
    failed = total - passed
    pass_rate = passed / total if total > 0 else 0

    by_task = defaultdict(list)
    failures = []

    for result in results:
        by_task[result["task"]].append(result)
        if not result["passed"]:
            failures.append(result)

    breakdown = {}
    for task, items in by_task.items():
        task_total = len(items)
        task_passed = sum(i["passed"] for i in items)

        breakdown[task] = {
            "total": task_total,
            "pass_rate": task_passed / task_total if task_total > 0 else 0
        }

    report = {
        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": round(pass_rate, 3)
        },
        "by_task": breakdown,
        "failures": failures
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Console output
    print(f"\nTotal: {total} | Passed: {passed} | Failed: {failed} | Pass rate: {pass_rate:.0%}")

    if breakdown:
        worst_task = min(breakdown.items(), key=lambda x: x[1]["pass_rate"])
        print(f"Worst task: {worst_task[0]} ({worst_task[1]['pass_rate']:.0%})")

    if failures:
        print("\nTop Failures:")
        for failure in failures[:5]:
            print(f"- {failure['id']}: {failure['reason']}")
