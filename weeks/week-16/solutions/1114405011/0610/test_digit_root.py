"""Tests for digit_root.

Requirements covered:
- At least 3 test cases
- Includes edge case(s)
- Includes invalid-input exception case
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_value(self):
        self.assertEqual(digit_root(199), 1)

    def test_multi_round_sum(self):
        self.assertEqual(digit_root(9875), 2)

    def test_edge_minimum_valid_input(self):
        # Edge case: minimum allowed n
        self.assertEqual(digit_root(1), 1)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "^n must be >= 1$"):
            digit_root(0)


if __name__ == "__main__":
    unittest.main()
