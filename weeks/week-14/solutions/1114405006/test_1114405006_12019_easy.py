# -*- coding: utf-8 -*-
"""
針對 `solution_1114405006-12019-easy.py` 的 unit tests（使用 unittest）

測試重點：
- 題目範例輸入輸出
- 幾個代表性日期是否對應正確星期
- 主程式 `main()` 的標準輸入/輸出處理

這份測試同時示範如何載入檔名含 `-easy` 的 Python 模組。
所有註解皆為繁體中文。
"""
import io
import sys
import unittest
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solution_1114405006-12019-easy.py")
SPEC = spec_from_file_location("solution_1114405006_12019_easy", MODULE_PATH)
solution = module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(solution)


class TestDoomsday2012Easy(unittest.TestCase):
    def test_sample_io(self):
        # 題目範例：檢查輸入輸出是否符合預期
        sample_input = """
3
3 7
1 10
12 25
"""
        expected_output = """
Wednesday
Tuesday
Tuesday
"""
        orig_stdin = sys.stdin
        orig_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(sample_input.strip() + "\n")
            sys.stdout = io.StringIO()
            solution.main()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdin = orig_stdin
            sys.stdout = orig_stdout

    def test_known_dates(self):
        # 2012 年的代表性日期：用來確認星期對應是否正確
        self.assertEqual(solution.weekday_2012_easy(1, 1), "Sunday")
        self.assertEqual(solution.weekday_2012_easy(3, 7), "Wednesday")
        self.assertEqual(solution.weekday_2012_easy(12, 25), "Tuesday")

    def test_doomsday_dates(self):
        # 題目表上的 doomsday 日期都應落在 Wednesday
        self.assertEqual(solution.weekday_2012_easy(1, 10), "Tuesday")
        self.assertEqual(solution.weekday_2012_easy(4, 4), "Wednesday")
        self.assertEqual(solution.weekday_2012_easy(10, 10), "Wednesday")


if __name__ == '__main__':
    unittest.main()
