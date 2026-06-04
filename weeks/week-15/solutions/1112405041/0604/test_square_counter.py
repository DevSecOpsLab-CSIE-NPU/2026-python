"""平方數計數 — 測試案例

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。
"""

import unittest

# 紅燈階段：匯入預期會失敗
try:
    from square_counter import count_squares
except ImportError:
    count_squares = None


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        # count_squares(1, 10) 應為 3 (1, 4, 9)
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case_single_point(self):
        # count_squares(1, 1) 應為 1
        self.assertEqual(count_squares(1, 1), 1)
        # count_squares(100, 100) 應為 1
        self.assertEqual(count_squares(100, 100), 1)

    def test_invalid_input_raises(self):
        # 使用 assertRaises 驗證 a > b 會丟 ValueError
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()
