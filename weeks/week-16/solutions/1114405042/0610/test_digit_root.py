"""數字根 — 測試

題目：digit_root(n) 反覆把 n 的各位數字相加，直到剩一位數，回傳該一位數。
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_multidigit(self):
        self.assertEqual(digit_root(24), 6)
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_single_digit(self):
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(9), 9)

    def test_edge_large_number(self):
        self.assertEqual(digit_root(2000000000), 2)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError) as ctx:
            digit_root(0)
        self.assertEqual(str(ctx.exception), "n must be >= 1")
        with self.assertRaises(ValueError) as ctx:
            digit_root(-5)
        self.assertEqual(str(ctx.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
