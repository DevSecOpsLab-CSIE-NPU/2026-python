"""搜尋演算法正確性測試"""

import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 3, 5, 7, 9, 11, 13]

    def test_linear_found(self):
        self.assertEqual(linear_search(self.data, 7), 3)

    def test_linear_not_found(self):
        self.assertEqual(linear_search(self.data, 4), -1)

    def test_linear_first_element(self):
        self.assertEqual(linear_search(self.data, 1), 0)

    def test_linear_last_element(self):
        self.assertEqual(linear_search(self.data, 13), 6)

    def test_binary_found(self):
        self.assertEqual(binary_search(self.data, 7), 3)

    def test_binary_not_found(self):
        self.assertEqual(binary_search(self.data, 4), -1)

    def test_binary_first_element(self):
        self.assertEqual(binary_search(self.data, 1), 0)

    def test_binary_last_element(self):
        self.assertEqual(binary_search(self.data, 13), 6)

    def test_does_not_mutate_data(self):
        original = self.data.copy()
        linear_search(self.data, 7)
        binary_search(self.data, 7)
        self.assertEqual(self.data, original)

    def test_empty_data(self):
        self.assertEqual(linear_search([], 1), -1)
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
