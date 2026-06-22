import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from task3_digit_root import digit_root, solve_input


class TestDigitRoot(unittest.TestCase):

    def test_sample_base8_zero(self):
        self.assertEqual(digit_root(0, 8), 0)

    def test_sample_base8_8(self):
        self.assertEqual(digit_root(8, 8), 1)

    def test_sample_base8_63(self):
        self.assertEqual(digit_root(63, 8), 7)

    def test_base13_zero(self):
        self.assertEqual(digit_root(0, 13), 0)

    def test_base13_single_digit(self):
        self.assertEqual(digit_root(5, 13), 5)

    def test_base13_13(self):
        self.assertEqual(digit_root(13, 13), 1)

    def test_base13_26(self):
        self.assertEqual(digit_root(26, 13), 2)

    def test_base13_168(self):
        self.assertEqual(digit_root(168, 13), 12)

    def test_base13_169(self):
        self.assertEqual(digit_root(169, 13), 1)

    def test_base13_large_number(self):
        self.assertEqual(digit_root(999999999, 13), 3)

    def test_base2_5(self):
        self.assertEqual(digit_root(5, 2), 1)

    def test_base16_255(self):
        self.assertEqual(digit_root(255, 16), 15)

    def test_solve_input_multiline(self):
        data = "0\n8\n63\n"
        self.assertEqual(solve_input(data, 8), "0\n1\n7")

    def test_solve_input_empty(self):
        data = ""
        self.assertEqual(solve_input(data, 8), "")


if __name__ == '__main__':
    unittest.main()
