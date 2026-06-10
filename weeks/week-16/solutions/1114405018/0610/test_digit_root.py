"""數字根 — 測試骨架"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(digit_root(24), 6)
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_case(self):
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(9), 9)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError) as cm:
            digit_root(0)
        self.assertEqual(str(cm.exception), "n must be >= 1")
        with self.assertRaises(ValueError) as cm:
            digit_root(-5)
        self.assertEqual(str(cm.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
