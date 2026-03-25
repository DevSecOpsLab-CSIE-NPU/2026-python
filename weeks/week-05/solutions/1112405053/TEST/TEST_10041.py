from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR.parent / "10041_AI.py"
RESULT_FILE = BASE_DIR / "RESULT_10041.txt"

# 依需求固定測試五次
TEST_CASES = [0, 1, 5, 42, 255]


def run_one_case(number: int) -> tuple[str, str, bool, str]:
	expected = bin(number)[2:]

	completed = subprocess.run(
		["python", str(TARGET_SCRIPT)],
		input=f"{number}\n",
		text=True,
		capture_output=True,
		check=False,
	)

	actual = completed.stdout.strip()
	is_pass = completed.returncode == 0 and actual == expected
	error_text = completed.stderr.strip()
	return expected, actual, is_pass, error_text


def main() -> None:
	lines: list[str] = []
	lines.append("=" * 60)
	lines.append(f"10041 測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	lines.append(f"目標程式: {TARGET_SCRIPT}")
	lines.append("=" * 60)

	pass_count = 0
	for index, number in enumerate(TEST_CASES, start=1):
		expected, actual, is_pass, error_text = run_one_case(number)
		status = "PASS" if is_pass else "FAIL"
		if is_pass:
			pass_count += 1

		lines.append(f"[第 {index} 次]")
		lines.append(f"輸入: {number}")
		lines.append(f"預期: {expected}")
		lines.append(f"實際: {actual}")
		lines.append(f"結果: {status}")
		if error_text:
			lines.append(f"stderr: {error_text}")
		lines.append("-" * 60)

	lines.append(f"總結: {pass_count}/{len(TEST_CASES)} 通過")

	result_text = "\n".join(lines) + "\n"
	RESULT_FILE.write_text(result_text, encoding="utf-8")

	print(result_text)
	print(f"測試結果已寫入: {RESULT_FILE}")


if __name__ == "__main__":
	main()
