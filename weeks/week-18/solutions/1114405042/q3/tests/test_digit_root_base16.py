import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from digit_root_base16 import digit_root_base16


class TestDigitRootBase16(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(digit_root_base16(0), 0)

    def test_single_digit(self):
        self.assertEqual(digit_root_base16(8), 8)

    def test_two_hex_digits(self):
        self.assertEqual(digit_root_base16(63), 3)

    def test_large_number(self):
        self.assertEqual(digit_root_base16(255), 15)

    def test_power_of_16(self):
        self.assertEqual(digit_root_base16(16), 1)
        self.assertEqual(digit_root_base16(256), 1)

    def test_random_value(self):
        self.assertEqual(digit_root_base16(100), 10)

    def test_hex_abc(self):
        self.assertEqual(digit_root_base16(0xABC), 3)

    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            digit_root_base16(-1)

    def test_invalid_negative_large(self):
        with self.assertRaises(ValueError):
            digit_root_base16(-100)


if __name__ == "__main__":
    unittest.main()
