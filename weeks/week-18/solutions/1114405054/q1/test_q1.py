import unittest
from q1 import clean_data


class TestCleanData(unittest.TestCase):

    def test_normal_dedupe_and_filter(self):
        self.assertEqual(clean_data([2, 4, 4, 6], 2), [2, 4, 6])

    def test_all_odd_returns_empty(self):
        self.assertEqual(clean_data([1, 3, 5], 2), [])

    def test_negatives_and_zero(self):
        self.assertEqual(clean_data([0, -2, -4, 4], 2), [-4, -2, 0, 4])

    def test_repeated_even_numbers(self):
        self.assertEqual(clean_data([2, 2, 4, 4, 6], 2), [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
