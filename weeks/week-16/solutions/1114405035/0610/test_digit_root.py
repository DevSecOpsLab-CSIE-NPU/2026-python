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

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        # 測試基本多位數
        self.assertEqual(digit_root(24), 6)
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_case(self):
        # 測試邊界案例：一位數、極大值
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(2000000000), 2)

    def test_invalid_input_raises(self):
        # 測試例外案例：n < 1
        with self.assertRaises(ValueError) as context:
            digit_root(0)
        self.assertEqual(str(context.exception), "n must be >= 1")

        with self.assertRaises(ValueError) as context:
            digit_root(-100)
        self.assertEqual(str(context.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()

