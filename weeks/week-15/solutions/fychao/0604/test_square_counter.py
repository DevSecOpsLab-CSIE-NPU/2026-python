"""平方數計數 — 測試

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。
"""

import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case_single_point_square(self):
        self.assertEqual(count_squares(1, 1), 1)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()
