from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR.parent / "10050_AI.py"
RESULT_FILE = BASE_DIR / "RESULT_10050.txt"


TEST_CASES = [
	{
		"name": "case-1",
		"input": """3
A B C
B A C
C A B
""",
	},
	{
		"name": "case-2",
		"input": """5
A B C
A C B
B A C
C B A
C B A
""",
	},
	{
		"name": "case-3",
		"input": """4
B A C
B C A
C B A
A C B
""",
	},
	{
		"name": "case-4",
		"input": """6
A C B
A C B
B C A
B C A
C A B
C A B
""",
	},
	{
		"name": "case-5",
		"input": """7
C A B
C A B
C B A
A B C
A C B
B A C
B C A
""",
	},
]


def run_one_case(case_input: str) -> tuple[str, int, str]:
	completed = subprocess.run(
		["python", str(TARGET_SCRIPT)],
		input=case_input,
		text=True,
		capture_output=True,
		check=False,
	)
	return completed.stdout.strip(), completed.returncode, completed.stderr.strip()


def main() -> None:
	lines: list[str] = []
	lines.append("=" * 60)
	lines.append(f"10050 測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	lines.append(f"目標程式: {TARGET_SCRIPT}")
	lines.append("=" * 60)

	success_count = 0
	for index, case in enumerate(TEST_CASES, start=1):
		actual, returncode, stderr_text = run_one_case(case["input"])
		status = "SUCCESS" if returncode == 0 else "ERROR"
		if returncode == 0:
			success_count += 1

		lines.append(f"[第 {index} 次] {case['name']}")
		lines.append(f"輸入:\n{case['input'].rstrip()}")
		lines.append(f"輸出: {actual}")
		lines.append(f"狀態: {status}")
		if returncode != 0:
			lines.append(f"return code: {returncode}")
		if stderr_text:
			lines.append(f"stderr: {stderr_text}")
		lines.append("-" * 60)

	lines.append(f"總結: {success_count}/{len(TEST_CASES)} 次執行成功")

	output = "\n".join(lines) + "\n"
	RESULT_FILE.write_text(output, encoding="utf-8")

	print(output)
	print(f"測試結果已寫入: {RESULT_FILE}")


if __name__ == "__main__":
	main()
