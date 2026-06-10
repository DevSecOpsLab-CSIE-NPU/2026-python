"""數字根 — unittest 測試

題目：digit_root(n) 反覆把 n 的各位數字相加，直到剩一位數，回傳該一位數。
      若 n < 1，應 raise ValueError("n must be >= 1")。

測試涵蓋：
  1. 基本多位數案例
  2. 需要重複加總到一位數的案例
  3. 一位數與最大範圍 edge case
  4. n < 1 的例外案例
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(digit_root(24), 6)

    def test_repeated_sum_until_one_digit(self):
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_case(self):
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(2_000_000_000), 2)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)


if __name__ == "__main__":
    unittest.main()
