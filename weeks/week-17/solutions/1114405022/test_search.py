import unittest

from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def test_found(self):
        data = [3, 1, 4, 1, 5, 9]
        self.assertEqual(linear_search(data, 4), 2)
        self.assertEqual(linear_search(data, 3), 0)
        self.assertEqual(linear_search(data, 9), 5)

    def test_not_found(self):
        data = [3, 1, 4, 1, 5, 9]
        self.assertEqual(linear_search(data, 99), -1)

    def test_empty(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_single_element(self):
        self.assertEqual(linear_search([7], 7), 0)
        self.assertEqual(linear_search([7], 5), -1)


class TestBinarySearch(unittest.TestCase):
    def test_found_sorted(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 7), 3)
        self.assertEqual(binary_search(data, 11), 5)

    def test_not_found_sorted(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(data, 4), -1)
        self.assertEqual(binary_search(data, 0), -1)
        self.assertEqual(binary_search(data, 99), -1)

    def test_empty(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element(self):
        self.assertEqual(binary_search([7], 7), 0)
        self.assertEqual(binary_search([7], 5), -1)

    def test_rejects_unsorted(self):
        with self.assertRaises(ValueError):
            binary_search([3, 1, 4, 1, 5], 3)
