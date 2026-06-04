"""平方數計數 — 測試檔（for TDD red phase）

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。

說明：這是 TDD 的測試檔，包含至少 3 個 test case：
  - 基本案例
  - edge case（單點區間）
  - 例外案例（a > b 時應丟 ValueError）
"""

import unittest

from square_counter import count_squares  # 完成實作後解除註解並實作功能


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        """基本案例：1 到 10 應有 3 個完全平方數（1,4,9）"""
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case_single_point(self):
        """Edge case：單一點區間，若該點為平方數應回傳 1"""
        self.assertEqual(count_squares(100, 100), 1)

    def test_invalid_input_raises(self):
        """例外案例：a > b 時應丟 ValueError"""
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()
