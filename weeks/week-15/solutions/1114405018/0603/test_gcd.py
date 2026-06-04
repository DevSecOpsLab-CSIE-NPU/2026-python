"""UVA 11417 GCD — tests for sum_of_gcd."""

import unittest

# from gcd import sum_of_gcd  # gcd.py 尚未實作，先保持註解以確保紅燈由匯入錯誤觸發


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1_edge_case(self):
        # edge case: no pairs
        self.fail("尚未實作 — 請補上斷言")

    def test_n_equals_2_minimum_useful_input(self):
        # gcd(1,2) = 1
        self.fail("尚未實作 — 請補上斷言")

    def test_n_equals_10_sample_case(self):
        # sample answer: 67
        self.fail("尚未實作 — 請補上斷言")


if __name__ == "__main__":
    unittest.main()
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