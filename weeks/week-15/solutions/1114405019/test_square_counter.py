"""平方數計數 — 測試

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。
"""

import unittest
from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        # 1~10：完全平方數有 1, 4, 9，共 3 個
        self.assertEqual(count_squares(1, 10), 3)

    def test_no_squares_in_range(self):
        # 5~8：無完全平方數
        self.assertEqual(count_squares(5, 8), 0)

    def test_edge_single_point_is_square(self):
        # edge case：單點且本身就是完全平方數
        self.assertEqual(count_squares(1, 1), 1)
        self.assertEqual(count_squares(100, 100), 1)

    def test_edge_single_point_not_square(self):
        # edge case：單點但不是完全平方數
        self.assertEqual(count_squares(2, 2), 0)

    def test_invalid_input_raises(self):
        # a > b 應丟出 ValueError
        with self.assertRaises(ValueError):
            count_squares(5, 2)

    def test_invalid_input_message(self):
        # 驗證例外訊息內容
        with self.assertRaises(ValueError) as ctx:
            count_squares(10, 1)
        self.assertEqual(str(ctx.exception), "a must be <= b")


if __name__ == "__main__":
    unittest.main()
