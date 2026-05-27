import io
import unittest

from solution_11417 import build_gcd_sums, gcd_sum, solve


class TestGcdSum(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(gcd_sum(10), 67)
        self.assertEqual(gcd_sum(100), 13015)
        self.assertEqual(gcd_sum(500), 442011)

    def test_small_values(self):
        self.assertEqual(gcd_sum(2), 1)
        self.assertEqual(gcd_sum(3), 3)
        self.assertEqual(gcd_sum(4), 7)

    def test_precomputed_values_match_direct_function(self):
        sums = build_gcd_sums(20)
        for n in range(2, 21):
            self.assertEqual(sums[n], gcd_sum(n))

    def test_solve_sample_input(self):
        sample_input = """10
100
500
0
"""
        expected = "67\n13015\n442011"
        self.assertEqual(solve(io.StringIO(sample_input)), expected)


if __name__ == "__main__":
    unittest.main()
