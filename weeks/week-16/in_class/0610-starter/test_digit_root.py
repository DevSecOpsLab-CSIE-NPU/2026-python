"""數字根 — 測試骨架

題目：digit_root(n) 反覆把 n 的各位數字相加，直到剩一位數，回傳該一位數。
      若 n < 1，應 raise ValueError("n must be >= 1")。

待辦：
  1. 自己打提示詞跟 AI 拆 test case，補齊至少 3 個
     - 至少 1 個 edge case
     - 至少 1 個例外案例
     （AI 給的案例齊不齊，自己驗收——這是 AI_LOG 要寫的事）
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: add failing tests for digit root"
  4. 寫 digit_root.py，全綠後 commit: "feat: implement digit root"
  5. 寫 AI_LOG.md（提示詞逐字記錄）
"""

import unittest

# from digit_root import digit_root  # 完成 digit_root.py 後解除註解


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        self.fail("尚未實作 — 自己打提示詞跟 AI 討論後補上")

    def test_edge_case(self):
        self.fail("尚未實作")

    def test_invalid_input_raises(self):
        self.fail("尚未實作")


if __name__ == "__main__":
    unittest.main()
