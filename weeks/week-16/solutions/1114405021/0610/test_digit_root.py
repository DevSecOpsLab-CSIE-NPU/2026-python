"""數字根 — 測試實作（solutions/1114405021）

包含至少 3 個測試：一般案例、邊界、例外。
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(digit_root(199), 1)

    def test_single_digit(self):
        self.assertEqual(digit_root(7), 7)

    def test_max_boundary(self):
        self.assertEqual(digit_root(2000000000), 2)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError) as ctx:
            digit_root(0)
        self.assertEqual(str(ctx.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
