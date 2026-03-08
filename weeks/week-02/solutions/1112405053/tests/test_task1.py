from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
import unittest
from dataclasses import dataclass
from typing import Any, Callable


ROOT_DIR = Path(__file__).resolve().parents[1]
TARGET_FILE = ROOT_DIR / "task1-Sequence Clean.py"


def load_task1_module():
	spec = importlib.util.spec_from_file_location("task1_sequence_clean", TARGET_FILE)
	if spec is None or spec.loader is None:
		raise ImportError(f"無法載入目標檔案: {TARGET_FILE}")

	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


task1 = load_task1_module()


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
		input_data = "5 2 3 2 8 7 8 4 4 10 1"
		expected_output = (
			[5, 2, 3, 8, 7, 4, 10, 1],
			[1, 2, 2, 3, 4, 4, 5, 7, 8, 8, 10],
			[10, 8, 8, 7, 5, 4, 4, 3, 2, 2, 1],
			[2, 2, 8, 8, 4, 4, 10],
		)
		actual_output = task1.process_input_line(input_data)
		return CaseReport(
			name="1. 一般情況（正常輸入）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task1.py::TestTask1SequenceClean::test_normal_input",
			fix_note="確認主流程為去重保序、排序與偶數擷取三者分離，避免把偶數結果誤拿去做全排序輸出。",
		)

	if case_name == "boundary":
		input_data = ""
		expected_output = (
			[5, 2, 3, 8, 7, 4, 10, 1],
			[1, 2, 2, 3, 4, 4, 5, 7, 8, 8, 10],
			[10, 8, 8, 7, 5, 4, 4, 3, 2, 2, 1],
			[2, 2, 8, 8, 4, 4, 10],
		)
		actual_output = task1.process_input_line(input_data)
		return CaseReport(
			name="2. 邊界情況（空輸入）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task1.py::TestTask1SequenceClean::test_boundary_empty_input",
			fix_note="空輸入必須走預設範例資料，避免直接 split 後得到空陣列導致輸出與規格不符。",
		)

	if case_name == "duplicate_tie":
		input_data = [4, 4, 2, 2, 8, 8, 6, 6]
		expected_output = [2, 4, 6, 8]
		actual_output = task1.sequence_clean(input_data)
		return CaseReport(
			name="3. 重複值/同分排序情況",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task1.py::TestTask1SequenceClean::test_duplicate_and_sort_behavior",
			fix_note="去重與排序需先後一致，否則重複偶數在不同順序下可能產生不穩定結果。",
		)

	if case_name == "counterexample":
		input_data = [2, 1, 2, 3, 4, 5, 4]
		expected_output = [2, 4]
		actual_output = task1.sequence_clean(input_data)
		return CaseReport(
			name="4. 反例（容易寫錯）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task1.py::TestTask1SequenceClean::test_counterexample_no_order_break",
			fix_note="不能用 set(seq) 直接去重，否則元素首次出現順序會被破壞而導致後續流程錯誤。",
		)

	if case_name == "high_error_detection":
		input_data = [-2, -3, -2, 0, 1, 0, 4, -4, 4]
		expected_output = [-4, -2, 0, 4]
		actual_output = task1.sequence_clean(input_data)
		return CaseReport(
			name="5. 高錯誤檢出情況（負數+0+重複）",
			input_data=input_data,
			expected_output=expected_output,
			actual_output=actual_output,
			passed=(actual_output == expected_output),
			test_function="tests/test_task1.py::TestTask1SequenceClean::test_high_error_detection_case",
			fix_note="偶數判斷需正確涵蓋負數與 0，且在去重後再排序才不會漏值或順序錯置。",
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


class TestTask1SequenceClean(unittest.TestCase):
	def test_normal_input(self):
		case = _run_case("normal")
		self.assertTrue(case.passed)

	def test_boundary_empty_input(self):
		case = _run_case("boundary")
		self.assertTrue(case.passed)

	def test_duplicate_and_sort_behavior(self):
		case = _run_case("duplicate_tie")
		self.assertTrue(case.passed)

	def test_counterexample_no_order_break(self):
		case = _run_case("counterexample")
		self.assertTrue(case.passed)

	def test_high_error_detection_case(self):
		case = _run_case("high_error_detection")
		self.assertTrue(case.passed)


def run_suite_once() -> bool:
	case_report_ok = run_all_case_reports()
	print("\n--- unittest 驗證 ---")
	suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTask1SequenceClean)
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

	# 任一輪失敗就回傳非 0，方便 CI / 腳本判斷
	if passed_runs != total_runs:
		sys.exit(1)
