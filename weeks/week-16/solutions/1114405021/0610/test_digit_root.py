"""Tests for digit_root in base 8."""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_multidigit_number(self):
        self.assertEqual(digit_root(64), 1)

    def test_edge_case_single_digit(self):
        self.assertEqual(digit_root(7), 7)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)

    def test_repeated_reduction(self):
        self.assertEqual(digit_root(511), 7)


if __name__ == "__main__":
    unittest.main()