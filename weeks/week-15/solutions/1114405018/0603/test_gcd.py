"""UVA 11417 GCD — tests for sum_of_gcd."""

import unittest

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1_edge_case(self):
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2_minimum_useful_input(self):
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_5_intermediate_case(self):
        self.assertEqual(sum_of_gcd(5), 11)

    def test_n_equals_10_sample_case(self):
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()