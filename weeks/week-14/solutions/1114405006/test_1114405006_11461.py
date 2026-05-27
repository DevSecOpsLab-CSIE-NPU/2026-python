# -*- coding: utf-8 -*-
"""
針對 `solution_1114405006_11461.py` 的 unit tests（使用 unittest）

測試重點：
- 題目範例輸入輸出
- 單一區間的邊界情況
- 跨越多個平方數的區間
- main() 的標準輸入/輸出處理

所有註解皆為繁體中文。
"""
import io
import sys
import unittest

from solution_1114405006_11461 import count_square_numbers, main


class TestSquareNumbers(unittest.TestCase):
    def test_sample_cases(self):
        # 題目提供的範例，應與輸出完全一致
        self.assertEqual(count_square_numbers(1, 4), 2)
        self.assertEqual(count_square_numbers(1, 10), 3)
        self.assertEqual(count_square_numbers(1, 100000), 316)

    def test_single_number_square(self):
        # 區間只有一個數，而且該數本身是完全平方數
        self.assertEqual(count_square_numbers(49, 49), 1)

    def test_single_number_non_square(self):
        # 區間只有一個數，但該數不是完全平方數
        self.assertEqual(count_square_numbers(50, 50), 0)

    def test_range_with_no_square(self):
        # 例如 [2, 3] 之間沒有完全平方數
        self.assertEqual(count_square_numbers(2, 3), 0)

    def test_range_with_multiple_squares(self):
        # [15, 30] 內有 16 與 25 兩個完全平方數
        self.assertEqual(count_square_numbers(15, 30), 2)

    def test_main_io(self):
        # 驗證 main() 的輸入輸出：模擬 stdin，檢查 stdout
        sample_input = """
1 4
1 10
1 100000
0 0
"""
        expected_output = """
2
3
316
"""
        orig_stdin = sys.stdin
        orig_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(sample_input.strip() + "\n")
            sys.stdout = io.StringIO()
            main()
            out = sys.stdout.getvalue()
            self.assertEqual(out.strip(), expected_output.strip())
        finally:
            sys.stdin = orig_stdin
            sys.stdout = orig_stdout


if __name__ == '__main__':
    unittest.main()
