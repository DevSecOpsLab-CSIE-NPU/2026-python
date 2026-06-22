import unittest
from main import binary_search, get_target, linear_search


class TestQuestion4(unittest.TestCase):
    def test_get_target(self):
        self.assertEqual(get_target("1114405017"), 117)

    def test_linear_search_found(self):
        index, comparisons = linear_search([1, 2, 117, 130], 117)
        self.assertEqual(index, 2)
        self.assertEqual(comparisons, 3)

    def test_linear_search_not_found(self):
        index, comparisons = linear_search([1, 2, 3, 4], 117)
        self.assertEqual(index, -1)
        self.assertEqual(comparisons, 4)

    def test_binary_search_found(self):
        index, comparisons = binary_search([1, 2, 117, 130], 117)
        self.assertEqual(index, 2)
        self.assertGreaterEqual(comparisons, 1)

    def test_binary_search_not_found(self):
        index, comparisons = binary_search([1, 2, 3, 4], 117)
        self.assertEqual(index, -1)


if __name__ == "__main__":
    unittest.main()
