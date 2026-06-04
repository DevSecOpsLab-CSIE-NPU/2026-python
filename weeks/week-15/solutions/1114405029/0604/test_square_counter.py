"""平方數計數 — unittest 測試檔

題目：
count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
若 a > b，應 raise ValueError("a must be <= b")。

TDD 流程：
1. 先寫測試
2. 先跑出紅燈
3. commit 測試
4. 再寫 square_counter.py 實作
"""

import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        """基本案例：1 到 10 之間有 1、4、9，共 3 個完全平方數。"""
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case_single_square(self):
        """Edge case：單點區間 1 到 1，本身就是完全平方數。"""
        self.assertEqual(count_squares(1, 1), 1)

    def test_range_without_square(self):
        """補充案例：5 到 8 之間沒有任何完全平方數。"""
        self.assertEqual(count_squares(5, 8), 0)

    def test_invalid_input_raises(self):
        """例外案例：a > b 時，應丟出 ValueError。"""
        with self.assertRaises(ValueError) as context:
            count_squares(5, 2)

        self.assertEqual(str(context.exception), "a must be <= b")


if __name__ == "__main__":
    unittest.main()