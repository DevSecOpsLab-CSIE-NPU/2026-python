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
    def test_basic_multi_step(self):
        # 199 → 19 → 10 → 1
        self.assertEqual(digit_root(199), 1)

    def test_basic_single_step(self):
        # 24 → 6
        self.assertEqual(digit_root(24), 6)

    def test_basic_9999(self):
        # 9999 → 36 → 9
        self.assertEqual(digit_root(9999), 9)

    def test_edge_single_digit(self):
        # 已是一位數，直接回傳
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(9), 9)

    def test_edge_large_number(self):
        # 靠近上限 2,000,000,000
        self.assertEqual(digit_root(2000000000), digit_root(2000000000))
        # 2+0+...+0 = 2
        self.assertEqual(digit_root(2000000000), 2)

    def test_invalid_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            digit_root(0)
        self.assertEqual(str(ctx.exception), "n must be >= 1")

    def test_invalid_negative_raises(self):
        with self.assertRaises(ValueError) as ctx:
            digit_root(-5)
        self.assertEqual(str(ctx.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
