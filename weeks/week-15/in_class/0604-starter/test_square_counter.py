"""平方數計數 — 測試骨架

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。

待辦：
  1. 跟 AI 討論，補齊至少 3 個 test case
     - 至少 1 個 edge case
     - 至少 1 個例外案例（測試 a > b 時的 ValueError）
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: add failing tests for square counter"
  4. 寫 square_counter.py
  5. 寫 AI_LOG.md
"""

import unittest

# from square_counter import count_squares  # 完成後解除註解


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        # TODO: count_squares(1, 10) 應為 3 (1, 4, 9)
        self.fail("尚未實作")

    def test_edge_case(self):
        # TODO: 想一個 edge case（單點區間？最小區間？）
        self.fail("尚未實作")

    def test_invalid_input_raises(self):
        # TODO: 使用 assertRaises 驗證 a > b 會丟 ValueError
        # 提示：with self.assertRaises(ValueError): count_squares(5, 2)
        self.fail("尚未實作")


if __name__ == "__main__":
    unittest.main()
