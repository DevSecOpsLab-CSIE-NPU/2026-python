from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path


TOTAL_RUNS = 5


TEST_CASES = [
	{
		"name": "basic_rotation",
		"input": "ABC\nDE\n",
		"expected": "DA\nEB\n C",
	},
	{
		"name": "single_line",
		"input": "HELLO\n",
		"expected": "H\nE\nL\nL\nO",
	},
	{
		"name": "space_sensitive",
		"input": "A \nB\n",
		"expected": "BA\n  ",
	},
]


def normalize_final_newline(text: str) -> str:
	if text.endswith("\n"):
		return text[:-1]
	return text


def run_one_case(script_path: Path, case_input: str) -> subprocess.CompletedProcess[str]:
	return subprocess.run(
		[sys.executable, str(script_path)],
		input=case_input,
		text=True,
		capture_output=True,
		check=False,
	)


def main() -> None:
	current_dir = Path(__file__).resolve().parent
	script_path = current_dir.parent / "Q490_ME.py"
	result_path = current_dir / "RESULT_Q490.txt"

	if not script_path.exists():
		raise FileNotFoundError(f"找不到被測試檔案: {script_path}")

	lines: list[str] = []
	lines.append(f"測試時間: {datetime.now().isoformat(timespec='seconds')}")
	lines.append(f"被測試檔案: {script_path}")
	lines.append(f"總執行次數: {TOTAL_RUNS}")
	lines.append("=" * 60)

	for run_index in range(1, TOTAL_RUNS + 1):
		run_passed = True
		lines.append(f"[Run {run_index}]")

		for case in TEST_CASES:
			proc = run_one_case(script_path, case["input"])
			expected_normalized = normalize_final_newline(case["expected"])
			actual_normalized = normalize_final_newline(proc.stdout)

			case_passed = proc.returncode == 0 and actual_normalized == expected_normalized
			if not case_passed:
				run_passed = False

			lines.append(
				f"- {case['name']}: {'PASS' if case_passed else 'FAIL'} (returncode={proc.returncode})"
			)

			if not case_passed:
				lines.append(f"  expected(normalized): {repr(expected_normalized)}")
				lines.append(f"  actual(normalized)  : {repr(actual_normalized)}")
				lines.append(f"  expected(raw): {repr(case['expected'])}")
				lines.append(f"  actual(raw)  : {repr(proc.stdout)}")
				if proc.stderr:
					lines.append(f"  stderr  : {repr(proc.stderr)}")

		lines.append(f"Run {run_index} 結果: {'PASS' if run_passed else 'FAIL'}")
		lines.append("-" * 60)

	result_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
	print(f"測試完成，結果已寫入: {result_path}")


if __name__ == "__main__":
	main()
