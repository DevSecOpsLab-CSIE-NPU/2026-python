from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
TARGET_FILE = BASE_DIR / "task3_AI.py"
LOG_FILE = Path(__file__).resolve().parent / "task3_test_records.log"


TEST_CASES = [
	{
		"name": "sample_case",
		"input": '"To be or not to be," quoth the Bard, "that\nis the question".\nThe programming\ncontestant replied: "I must disagree.\nTo `C\' or not to `C\', that is The Question!"\n',
		"expected": "``To be or not to be,'' quoth the Bard, ``that\nis the question''.\nThe programming\ncontestant replied: ``I must disagree.\nTo `C' or not to `C', that is The Question!''\n",
	},
	{
		"name": "no_quotes",
		"input": "Plain text only.\nNo replacement needed.\n",
		"expected": "Plain text only.\nNo replacement needed.\n",
	},
	{
		"name": "single_pair",
		"input": 'She said, "hello".\n',
		"expected": "She said, ``hello''.\n",
	},
	{
		"name": "multiple_pairs_same_line",
		"input": '"A" "B" "C"\n',
		"expected": "``A'' ``B'' ``C''\n",
	},
]


def run_case(case_input: str) -> tuple[int, str, str, str]:
	completed = subprocess.run(
		[sys.executable, str(TARGET_FILE)],
		input=case_input,
		text=True,
		capture_output=True,
		check=False,
	)

	stdout = completed.stdout.replace("\r\n", "\n")
	stderr = completed.stderr.strip()
	if stderr:
		combined_output = f"{stdout}[stderr]\n{stderr}"
	else:
		combined_output = stdout

	return completed.returncode, stdout, stderr, combined_output


def append_log(lines: list[str]) -> None:
	with LOG_FILE.open("a", encoding="utf-8") as file:
		file.write("\n".join(lines))
		file.write("\n\n")


def main() -> None:
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	log_lines = [f"=== task3_AI.py test run at {timestamp} ==="]
	passed_count = 0

	for case in TEST_CASES:
		returncode, stdout, stderr, combined_output = run_case(case["input"])
		passed = returncode == 0 and not stderr and stdout == case["expected"]
		status = "PASS" if passed else "FAIL"

		if passed:
			passed_count += 1

		log_lines.append(f"[{status}] {case['name']}")
		log_lines.append("input:")
		log_lines.append(case["input"].rstrip("\n"))
		log_lines.append("expected:")
		log_lines.append(case["expected"].rstrip("\n"))
		log_lines.append("actual:")
		log_lines.append(combined_output.rstrip("\n"))
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
