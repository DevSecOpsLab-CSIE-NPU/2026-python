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

from digit_root import digit_root  # 完成 digit_root.py 後會由此 import


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        # 基本案例
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(38), 2)
        self.assertEqual(digit_root(12345), 6)
        self.assertEqual(digit_root(9), 9)

    def test_edge_case(self):
        # edge cases: 最小與最大的允許值，以及全部 9 的情形
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(2000000000), 2)
        self.assertEqual(digit_root(999999999), 9)

    def test_invalid_input_raises(self):
        # 例外案例：n < 1 時要 raise 指定訊息的 ValueError
        with self.assertRaisesRegex(ValueError, r"^n must be >= 1$"):
            digit_root(0)
        with self.assertRaisesRegex(ValueError, r"^n must be >= 1$"):
            digit_root(-10)


if __name__ == "__main__":
    unittest.main()
