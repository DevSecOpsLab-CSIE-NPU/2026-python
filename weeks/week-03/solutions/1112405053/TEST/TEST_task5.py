from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
TARGET_FILE = BASE_DIR / "task5_AI.py"
LOG_FILE = Path(__file__).resolve().parent / "task5_test_records.log"


TEST_CASES = [
    {
        "name": "sample_case",
        "input": """3
3
1 3 2
4
4 3 2 1
2
2 1
""",
        "expected": """Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps.""",
    },
    {
        "name": "already_sorted",
        "input": """1
5
1 2 3 4 5
""",
        "expected": "Optimal train swapping takes 0 swaps.",
    },
    {
        "name": "single_car",
        "input": """1
1
1
""",
        "expected": "Optimal train swapping takes 0 swaps.",
    },
    {
        "name": "mixed_order",
        "input": """2
5
5 1 2 4 3
3
2 3 1
""",
        "expected": """Optimal train swapping takes 5 swaps.
Optimal train swapping takes 2 swaps.""",
    },
]


def normalize_output(text: str) -> str:
    return text.replace("\r\n", "\n").strip()


def run_case(case_input: str) -> tuple[int, str, str, str]:
    completed = subprocess.run(
        [sys.executable, str(TARGET_FILE)],
        input=case_input,
        text=True,
        capture_output=True,
        check=False,
    )

    stdout = normalize_output(completed.stdout)
    stderr = completed.stderr.strip()
    if stderr:
        combined_output = f"{stdout}\n[stderr]\n{stderr}".strip()
    else:
        combined_output = stdout

    return completed.returncode, stdout, stderr, combined_output


def append_log(lines: list[str]) -> None:
    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write("\n".join(lines))
        file.write("\n\n")


def main() -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_lines = [f"=== task5_AI.py test run at {timestamp} ==="]
    passed_count = 0

    for case in TEST_CASES:
        expected = normalize_output(case["expected"])
        returncode, stdout, stderr, combined_output = run_case(case["input"])
        passed = returncode == 0 and not stderr and stdout == expected
        status = "PASS" if passed else "FAIL"

        if passed:
            passed_count += 1

        log_lines.append(f"[{status}] {case['name']}")
        log_lines.append("input:")
        log_lines.append(case["input"].rstrip())
        log_lines.append("expected:")
        log_lines.append(expected)
        log_lines.append("actual:")
        log_lines.append(combined_output)
        log_lines.append("-" * 40)

    summary = f"Summary: {passed_count}/{len(TEST_CASES)} passed"
    log_lines.append(summary)
    append_log(log_lines)

    print(summary)
    print(f"Test log saved to: {LOG_FILE}")

    if passed_count != len(TEST_CASES):
        raise SystemExit(1)


if __name__ == "__main__":
    main()