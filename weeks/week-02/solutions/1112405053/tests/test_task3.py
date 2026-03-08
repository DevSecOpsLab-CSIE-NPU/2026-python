from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import unittest


ROOT_DIR = Path(__file__).resolve().parents[1]
TARGET_FILE = ROOT_DIR / "task3-Log Summary.py"


@dataclass
class CaseReport:
	name: str
	input_data: str
	expected_output: list[str]
	actual_output: list[str]
	passed: bool
	test_function: str
	fix_note: str


def run_task3_with_input(input_text: str) -> list[str]:
	proc = subprocess.run(
		[sys.executable, str(TARGET_FILE)],
		input=input_text,
		text=True,
		capture_output=True,
		check=False,
	)

	stdout_lines = [line.rstrip() for line in proc.stdout.splitlines()]
	stderr_lines = [line.rstrip() for line in proc.stderr.splitlines() if line.strip()]

	if proc.returncode != 0:
		return stdout_lines + [f"<RETURN_CODE {proc.returncode}>"] + stderr_lines

	return stdout_lines


def _run_case(case_name: str) -> CaseReport:
	if case_name == "normal":
		input_data = """8
alice login
bob view
alice view
chris login
bob login
bob view
alice logout
bob logout
"""
		expected_output = [
			"bob 4",
			"alice 3",
			"chris 1",
			"top_action: login 3",
		]
		actual_output = run_task3_with_input(input_data)
		return CaseReport(
			name="1. 一般情況（正常輸入）",
			input_data=input_data.strip(),
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task3.py::TestTask3LogSummary::test_normal_input",
			fix_note="需同時統計 user 次數與 action 次數，避免只做其中一個統計導致輸出缺漏。",
		)

	if case_name == "boundary":
		input_data = "0\n"
		expected_output = []
		actual_output = run_task3_with_input(input_data)
		return CaseReport(
			name="2. 邊界情況（最小輸入 m=0）",
			input_data=input_data.strip(),
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task3.py::TestTask3LogSummary::test_boundary_minimal_input",
			fix_note="m=0 時不應輸出 top_action，必須先判斷 action_count 是否為空。",
		)

	if case_name == "duplicate_tie":
		input_data = """4
bob login
alice view
bob logout
alice login
"""
		expected_output = [
			"alice 2",
			"bob 2",
			"top_action: login 2",
		]
		actual_output = run_task3_with_input(input_data)
		return CaseReport(
			name="3. 重複值/同分排序情況",
			input_data=input_data.strip(),
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task3.py::TestTask3LogSummary::test_tie_break_by_user_name",
			fix_note="當 user 次數相同時要用名稱字母序排序，不能沿用輸入順序。",
		)

	if case_name == "counterexample":
		input_data = """6
amy login
amy view
bob login
bob login
cara view
cara view
"""
		expected_output = [
			"amy 2",
			"bob 2",
			"cara 2",
			"top_action: login 3",
		]
		actual_output = run_task3_with_input(input_data)
		return CaseReport(
			name="4. 反例（容易寫錯）",
			input_data=input_data.strip(),
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task3.py::TestTask3LogSummary::test_counterexample_top_action_not_top_user",
			fix_note="top_action 必須由 action_count 計算，不能誤用 user 排名第一名對應的 action。",
		)

	if case_name == "high_error_detection":
		input_data = """12
zack download
amy login
zack login
bob login
amy upload
bob download
amy login
cara download
cara login
cara logout
bob login
zack logout
"""
		expected_output = [
			"amy 3",
			"bob 3",
			"cara 3",
			"zack 3",
			"top_action: login 6",
		]
		actual_output = run_task3_with_input(input_data)
		return CaseReport(
			name="5. 高錯誤檢出情況（多人同次數 + action 混合）",
			input_data=input_data.strip(),
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task3.py::TestTask3LogSummary::test_high_error_detection_case",
			fix_note="這組同時驗證 user 同分字母序與 action 全域統計，最容易抓出排序鍵或統計目標寫錯。",
		)

	raise ValueError(f"未知案例: {case_name}")


def print_case_report(case: CaseReport) -> None:
	status = "PASS" if case.passed else "FAIL"
	print(f"\n{case.name}")
	print(f"輸入: {case.input_data}")
	print(f"預期輸出: {case.expected_output}")
	print(f"實際輸出: {case.actual_output}")
	print(f"是否通過: {status}")
	print(f"對應測試函式: {case.test_function}")
	print(f"關鍵修改點: {case.fix_note}")


def run_all_case_reports() -> bool:
	case_order = ["normal", "boundary", "duplicate_tie", "counterexample", "high_error_detection"]
	all_passed = True
	for case_name in case_order:
		case = _run_case(case_name)
		print_case_report(case)
		if not case.passed:
			all_passed = False
	return all_passed


class TestTask3LogSummary(unittest.TestCase):
	def test_normal_input(self):
		case = _run_case("normal")
		self.assertTrue(case.passed)

	def test_boundary_minimal_input(self):
		case = _run_case("boundary")
		self.assertTrue(case.passed)

	def test_tie_break_by_user_name(self):
		case = _run_case("duplicate_tie")
		self.assertTrue(case.passed)

	def test_counterexample_top_action_not_top_user(self):
		case = _run_case("counterexample")
		self.assertTrue(case.passed)

	def test_high_error_detection_case(self):
		case = _run_case("high_error_detection")
		self.assertTrue(case.passed)


def run_suite_once() -> bool:
	case_report_ok = run_all_case_reports()
	print("\n--- unittest 驗證 ---")
	suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTask3LogSummary)
	result = unittest.TextTestRunner(verbosity=2).run(suite)
	return case_report_ok and result.wasSuccessful()


if __name__ == "__main__":
	total_runs = 5
	passed_runs = 0

	for i in range(1, total_runs + 1):
		print(f"\n========== 第 {i}/{total_runs} 次測試 ==========")
		ok = run_suite_once()
		if ok:
			passed_runs += 1

	print("\n========== 測試總結 ==========")
	print(f"通過次數: {passed_runs}/{total_runs}")

	if passed_runs != total_runs:
		sys.exit(1)
