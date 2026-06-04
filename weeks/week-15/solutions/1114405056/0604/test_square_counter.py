"""平方數計數 — 測試

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。
"""

import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        """[1, 10] 內有 3 個完全平方數：1, 4, 9"""
        self.assertEqual(count_squares(1, 10), 3)

    def test_basic_range_1_to_4(self):
        """[1, 4] 內有 2 個完全平方數：1, 4"""
        self.assertEqual(count_squares(1, 4), 2)

    def test_no_squares_in_range(self):
        """[5, 8] 內沒有完全平方數"""
        self.assertEqual(count_squares(5, 8), 0)

    def test_edge_single_point_is_square(self):
        """單點區間且剛好是完全平方數：[1, 1] 應為 1"""
        self.assertEqual(count_squares(1, 1), 1)

    def test_edge_single_point_large_square(self):
        """單點區間且是較大的完全平方數：[100, 100] 應為 1"""
        self.assertEqual(count_squares(100, 100), 1)

    def test_edge_single_point_not_square(self):
        """單點區間且不是完全平方數：[5, 5] 應為 0"""
        self.assertEqual(count_squares(5, 5), 0)

    def test_large_range(self):
        """[1, 100] 內有 10 個完全平方數：1,4,9,16,25,36,49,64,81,100"""
        self.assertEqual(count_squares(1, 100), 10)

    def test_invalid_input_raises(self):
        """a > b 應丟出 ValueError("a must be <= b")"""
        with self.assertRaises(ValueError) as ctx:
            count_squares(5, 2)
        self.assertEqual(str(ctx.exception), "a must be <= b")

    def test_invalid_input_equal_after_swap(self):
        """確認 a > b 時（非 a == b）皆丟出 ValueError"""
        with self.assertRaises(ValueError):
            count_squares(10, 1)


if __name__ == "__main__":
    unittest.main()
