"""平方數計數 — 測試骨架

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。

範例：
- count_squares(1, 10) = 3 (1, 4, 9)
- count_squares(1, 1) = 1 (1)
- count_squares(5, 8) = 0 (無)
- count_squares(5, 3) 應丟 ValueError
"""

import unittest
from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        """基本案例：count_squares(1, 10) 應為 3 (1, 4, 9)"""
        self.assertEqual(count_squares(1, 10), 3)

    def test_single_point_is_square(self):
        """Edge case：單點區間，1 本身就是完全平方數"""
        self.assertEqual(count_squares(1, 1), 1)

    def test_no_squares_in_range(self):
        """Edge case：區間內沒有完全平方數"""
        self.assertEqual(count_squares(5, 8), 0)

    def test_single_large_perfect_square(self):
        """Edge case：大數字的完全平方數"""
        self.assertEqual(count_squares(100, 100), 1)

    def test_invalid_input_raises_value_error(self):
        """例外案例：a > b 應丟 ValueError"""
        with self.assertRaises(ValueError):
            count_squares(5, 3)


if __name__ == "__main__":
    unittest.main()
