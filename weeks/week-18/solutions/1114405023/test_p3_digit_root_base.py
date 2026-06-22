"""
第三題測試：任意進位的數字根
"""

import unittest

from p3_digit_root_base import digit_root, solve, sum_digits_in_base


class TestDigitRootBase(unittest.TestCase):
    def test_zero_should_return_zero(self):
        self.assertEqual(digit_root(0), 0)

    def test_value_smaller_than_base_should_return_itself(self):
        self.assertEqual(digit_root(2), 2)

    def test_sum_digits_in_base_three(self):
        # 8 的三進位是 22，所以 2 + 2 = 4
        self.assertEqual(sum_digits_in_base(8), 4)

    def test_digit_root_base_three(self):
        # 8 -> base3: 22 -> 4；4 -> base3: 11 -> 2
        self.assertEqual(digit_root(8), 2)

    def test_solve_multiple_lines(self):
        input_text = "0\n8\n63\n"
        expected = "0\n2\n1"
        self.assertEqual(solve(input_text), expected)


if __name__ == "__main__":
    unittest.main()
