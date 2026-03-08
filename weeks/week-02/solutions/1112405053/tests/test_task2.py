from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import unittest


ROOT_DIR = Path(__file__).resolve().parents[1]
TARGET_FILE = ROOT_DIR / "task2-Student Ranking.py"


def load_task2_module():
	spec = importlib.util.spec_from_file_location("task2_student_ranking", TARGET_FILE)
	if spec is None or spec.loader is None:
		raise ImportError(f"無法載入目標檔案: {TARGET_FILE}")

	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


task2 = load_task2_module()


@dataclass
class CaseReport:
	name: str
	input_data: Any
	expected_output: Any
	actual_output: Any
	passed: bool
	test_function: str
	fix_note: str


def _run_case(case_name: str) -> CaseReport:
	if case_name == "normal":
		input_data = [
			("Alice", 88, 20),
			("Bob", 95, 22),
			("Charlie", 88, 19),
			("David", 95, 21),
			("Eve", 88, 20),
		]
		expected_output = [
			("David", 95, 21),
			("Bob", 95, 22),
			("Charlie", 88, 19),
			("Alice", 88, 20),
			("Eve", 88, 20),
		]
		actual_output = task2.sort_students(input_data)
		return CaseReport(
			name="1. 一般情況（正常輸入）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task2.py::TestTask2StudentRanking::test_normal_input",
			fix_note="排序鍵必須是 score 降冪、age 升冪、name 升冪，任一順序顛倒都會導致排名錯誤。",
		)

	if case_name == "boundary":
		input_data = []
		expected_output = []
		actual_output = task2.sort_students(input_data)
		return CaseReport(
			name="2. 邊界情況（空輸入）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task2.py::TestTask2StudentRanking::test_boundary_empty_input",
			fix_note="空列表應直接回傳空結果，避免對空資料做索引或切片造成例外。",
		)

	if case_name == "duplicate_tie":
		input_data = [
			("Liam", 90, 20),
			("Emma", 90, 20),
			("Noah", 90, 20),
			("Ava", 90, 20),
		]
		expected_output = [
			("Ava", 90, 20),
			("Emma", 90, 20),
			("Liam", 90, 20),
			("Noah", 90, 20),
		]
		actual_output = task2.sort_students(input_data)
		return CaseReport(
			name="3. 重複值/同分排序情況",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task2.py::TestTask2StudentRanking::test_tie_break_by_name",
			fix_note="當分數與年齡都相同時需以姓名字母序作為最後 tie-break，否則結果會不穩定。",
		)

	if case_name == "counterexample":
		input_data = [
			("Zoe", "100", "19"),
			("Amy", "95", "18"),
			("Ben", "100", "20"),
		]
		expected_output = [
			("Zoe", "100", "19"),
			("Ben", "100", "20"),
			("Amy", "95", "18"),
		]
		actual_output = task2.sort_students(input_data)
		return CaseReport(
			name="4. 反例（容易寫錯）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task2.py::TestTask2StudentRanking::test_counterexample_numeric_string_input",
			fix_note="分數與年齡若以字串輸入，排序前需轉成整數，否則會發生字典序比較錯誤。",
		)

	if case_name == "high_error_detection":
		input_data = [
			("Mia", 100, 21),
			("Leo", 100, 20),
			("Aiden", 100, 20),
			("Nora", 99, 18),
			("Owen", 99, 18),
			("Ivy", 99, 19),
			("Eli", 100, 20),
		]
		expected_output = [
			("Aiden", 100, 20),
			("Eli", 100, 20),
			("Leo", 100, 20),
			("Mia", 100, 21),
			("Nora", 99, 18),
			("Owen", 99, 18),
			("Ivy", 99, 19),
		]
		actual_output = task2.sort_students(input_data)
		return CaseReport(
			name="5. 高錯誤檢出情況（多層 tie-break 混合）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task2.py::TestTask2StudentRanking::test_high_error_detection_case",
			fix_note="這組同時驗證 score、age、name 三層排序，最容易抓出 key 欄位順序寫反的問題。",
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


class TestTask2StudentRanking(unittest.TestCase):
	def test_normal_input(self):
		case = _run_case("normal")
		self.assertTrue(case.passed)

	def test_boundary_empty_input(self):
		case = _run_case("boundary")
		self.assertTrue(case.passed)

	def test_tie_break_by_name(self):
		case = _run_case("duplicate_tie")
		self.assertTrue(case.passed)

	def test_counterexample_numeric_string_input(self):
		case = _run_case("counterexample")
		self.assertTrue(case.passed)

	def test_high_error_detection_case(self):
		case = _run_case("high_error_detection")
		self.assertTrue(case.passed)


def run_suite_once() -> bool:
	case_report_ok = run_all_case_reports()
	print("\n--- unittest 驗證 ---")
	suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTask2StudentRanking)
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
