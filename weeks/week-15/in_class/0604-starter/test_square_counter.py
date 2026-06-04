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

# 解除註解以便測試初期會失敗（尚未實作 square_counter.py）
from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        # 基本範例：1..10 包含 1,4,9
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case(self):
        # edge case：單點區間且為平方數
        self.assertEqual(count_squares(16, 16), 1)

    def test_negative_to_positive(self):
        # edge case：包含負數到正數，0 也算平方數
        self.assertEqual(count_squares(-5, 5), 3)

    def test_invalid_input_raises(self):
        # 驗證 a > b 會丟出 ValueError
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()
