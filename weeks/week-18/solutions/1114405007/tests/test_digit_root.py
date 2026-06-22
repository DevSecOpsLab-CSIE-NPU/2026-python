import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task3_digit_root import digit_root, solve


class TestDigitRoot(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(digit_root(0, 11), 0)

    def test_single_digit_lt_base(self):
        self.assertEqual(digit_root(5, 11), 5)

    def test_two_digit_sum_lt_base(self):
        self.assertEqual(digit_root(10, 11), 10)

    def test_two_digit_sum_eq_base(self):
        self.assertEqual(digit_root(11, 11), 1)

    def test_three_digit(self):
        self.assertEqual(digit_root(20, 11), 10)

    def test_large_number(self):
        self.assertEqual(digit_root(121, 11), 1)

    def test_another_large(self):
        self.assertEqual(digit_root(100, 11), 10)

    def test_big_number(self):
        self.assertEqual(digit_root(10**9, 11), 10)


class TestSolve(unittest.TestCase):

    def test_sample_multi_line(self):
        input_data = "0\n8\n63\n"
        expected = "0\n1\n7\n"
        self.assertEqual(solve(input_data, 8), expected)

    def test_single_line_zero(self):
        input_data = "0\n"
        expected = "0\n"
        self.assertEqual(solve(input_data, 11), expected)

    def test_multiple_with_base11(self):
        input_data = "0\n1\n10\n20\n"
        expected = "0\n1\n10\n10\n"
        self.assertEqual(solve(input_data, 11), expected)

    def test_empty_input(self):
        input_data = ""
        expected = ""
        self.assertEqual(solve(input_data, 11), expected)


if __name__ == "__main__":
    unittest.main()
