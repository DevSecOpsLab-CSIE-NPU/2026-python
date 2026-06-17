import unittest
from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):

    def test_found_first(self):
        self.assertEqual(linear_search([1, 2, 3], 1), 0)

    def test_found_last(self):
        self.assertEqual(linear_search([1, 2, 3], 3), 2)

    def test_not_found(self):
        self.assertEqual(linear_search([1, 2, 3], 4), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_duplicates_returns_first(self):
        self.assertEqual(linear_search([2, 2, 3], 2), 0)

    def test_data_not_modified(self):
        data = [3, 1, 2]
        original = data.copy()
        linear_search(data, 2)
        self.assertEqual(data, original)


class TestBinarySearch(unittest.TestCase):

    def test_found_first(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_found_last(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_found_mid(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([5], 3), -1)

    def test_data_not_modified(self):
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        binary_search(data, 3)
        self.assertEqual(data, original)


if __name__ == '__main__':
    unittest.main()
