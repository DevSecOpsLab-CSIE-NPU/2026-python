import unittest

from uva11417 import sum_gcd_pairs
from square_count import count_squares


class TestSolutions(unittest.TestCase):
    def test_sum_gcd_pairs_small(self):
        self.assertEqual(sum_gcd_pairs(1), 0)
        self.assertEqual(sum_gcd_pairs(2), 1)  # gcd(1,2)=1
        self.assertEqual(sum_gcd_pairs(3), 3)  # gcd pairs: (1,2)=1,(1,3)=1,(2,3)=1
        self.assertEqual(sum_gcd_pairs(4), 7)  # manual check

    def test_count_squares(self):
        self.assertEqual(count_squares(0), 0)
        self.assertEqual(count_squares(1), 1)
        self.assertEqual(count_squares(15), 3)  # 1,4,9
        self.assertEqual(count_squares(16), 4)


if __name__ == "__main__":
    unittest.main()
