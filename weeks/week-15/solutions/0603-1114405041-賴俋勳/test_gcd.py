"""Tests for UVA 11417: sum_of_gcd."""

import unittest

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_2(self):
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        self.assertEqual(sum_of_gcd(10), 67)

    def test_edge_case_n_equals_1(self):
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_5(self):
        self.assertEqual(sum_of_gcd(5), 11)


if __name__ == "__main__":
    unittest.main()
