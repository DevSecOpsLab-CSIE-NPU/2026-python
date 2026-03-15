from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
TARGET_FILE = BASE_DIR / "task1_AI.py"
LOG_FILE = Path(__file__).resolve().parent / "task1_test_records.log"


def expected_sequence(start: int) -> str:
	values = []
	current = start

	while True:
		values.append(str(current))
		if current == 1:
			break
		if current % 2 == 1:
			current = 3 * current + 1
		else:
			current //= 2

	return "\n".join(values)


def run_case(case_input: int) -> tuple[bool, str, str]:
	completed = subprocess.run(
		[sys.executable, str(TARGET_FILE)],
		input=f"{case_input}\n",
		text=True,
		capture_output=True,
		check=False,
	)

	actual_output = completed.stdout.strip()
	expected_output = expected_sequence(case_input)
	passed = completed.returncode == 0 and actual_output == expected_output

	if completed.stderr:
		actual_output = f"{actual_output}\n[stderr]\n{completed.stderr.strip()}".strip()

	return passed, expected_output, actual_output


def append_log(lines: list[str]) -> None:
	with LOG_FILE.open("a", encoding="utf-8") as file:
		file.write("\n".join(lines))
		file.write("\n\n")


def main() -> None:
	test_cases = [1, 2, 3, 6, 7, 27]
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	log_lines = [f"=== task1_AI.py test run at {timestamp} ==="]
	passed_count = 0

	for case_input in test_cases:
		passed, expected_output, actual_output = run_case(case_input)
		status = "PASS" if passed else "FAIL"
		if passed:
			passed_count += 1

		log_lines.append(f"[{status}] input = {case_input}")
		log_lines.append("expected:")
		log_lines.append(expected_output)
		log_lines.append("actual:")
		log_lines.append(actual_output)
		log_lines.append("-" * 40)

	summary = f"Summary: {passed_count}/{len(test_cases)} passed"
	log_lines.append(summary)
	append_log(log_lines)

	print(summary)
	print(f"Test log saved to: {LOG_FILE}")

	if passed_count != len(test_cases):
		raise SystemExit(1)


if __name__ == "__main__":
	main()
