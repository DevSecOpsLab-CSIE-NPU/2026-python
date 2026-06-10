"""進位計數 — 測試骨架

題目：count_carries(a, b) 回傳直式計算 a + b 時發生進位的次數。
      若 a 或 b 為負數，應 raise ValueError("operands must be non-negative")。

待辦：
  1. 自己打提示詞跟 AI 拆 test case，補齊至少 3 個
     - 至少 1 個 edge case（提示一個方向：進位會不會連鎖？）
     - 至少 1 個例外案例
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: add failing tests for carry counter"
  4. 寫 carry_counter.py，全綠後 commit: "feat: implement carry counter"
  5. 寫 AI_LOG.md（提示詞逐字記錄）
"""

import unittest

# from carry_counter import count_carries  # 完成 carry_counter.py 後解除註解


class TestCountCarries(unittest.TestCase):
    def test_basic(self):
        self.fail("尚未實作 — 自己打提示詞跟 AI 討論後補上")

    def test_edge_case(self):
        self.fail("尚未實作")

    def test_invalid_input_raises(self):
        self.fail("尚未實作")


if __name__ == "__main__":
    unittest.main()
