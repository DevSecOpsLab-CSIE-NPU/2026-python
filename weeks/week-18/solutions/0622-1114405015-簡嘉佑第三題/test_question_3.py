import unittest

from question_3_solution import BASE, digital_root_in_base, solve, sum_digits_in_base


class TestQuestion3(unittest.TestCase):
    def test_base_value(self):
        self.assertEqual(BASE, 7)

    def test_zero(self):
        self.assertEqual(digital_root_in_base(0, 7), 0)

    def test_sample_values_with_base7(self):
        # Same numbers from sheet sample, but with student's base = 7.
        self.assertEqual(digital_root_in_base(0, 7), 0)
        self.assertEqual(digital_root_in_base(8, 7), 2)
        self.assertEqual(digital_root_in_base(63, 7), 3)

    def test_multiple_rounds(self):
        # 1000 (base10) in base7 is 2626, sum=16, then 16(base7=22)->4
        self.assertEqual(digital_root_in_base(1000, 7), 4)

    def test_large_number(self):
        self.assertEqual(digital_root_in_base(10**9, 7), 1)

    def test_sum_digits_helper(self):
        # 63(base10) = 120(base7) => 1+2+0=3
        self.assertEqual(sum_digits_in_base(63, 7), 3)

    def test_solve_lines(self):
        lines = ["0\n", "8\n", "63\n", "\n", "1000\n"]
        self.assertEqual(solve(lines), ["0", "2", "3", "4"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
