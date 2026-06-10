"""數字根 — 測試案例

題目：digit_root(n) 反覆把 n 的各位數字相加，直到剩一位數，回傳該一位數。
      若 n < 1，應 raise ValueError("n must be >= 1")。
"""

import unittest

from digit_root import digit_root  # 預期一開始會發生 ImportError，這是正常的紅燈


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        # 一般案例
        self.assertEqual(digit_root(24), 6)
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_case(self):
        # 邊界案例：已經是一位數的情況
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(1), 1)
        # 邊界案例：極大值 (題目範圍上限 2,000,000,000)
        self.assertEqual(digit_root(2000000000), 2)

    def test_invalid_input_raises(self):
        # 例外案例：當 n < 1 應該拋出精確的 ValueError 錯誤訊息
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(-10)

if __name__ == "__main__":
    unittest.main()