import unittest
try:
    from gcd import sum_of_gcd
except ImportError:
    sum_of_gcd = None

class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_2(self): self.assertEqual(sum_of_gcd(2), 1)
    def test_n_equals_10(self): self.assertEqual(sum_of_gcd(10), 67)
    def test_edge_case_n1(self): self.assertEqual(sum_of_gcd(1), 0)

if __name__ == '__main__':
    unittest.main()
