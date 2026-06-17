"""0617 任務二 — search 測試"""

import unittest
from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def test_found_at_head(self):
        self.assertEqual(linear_search([10, 20, 30, 40], 10), 0)

    def test_found_at_tail(self):
        self.assertEqual(linear_search([10, 20, 30, 40], 40), 3)

    def test_found_at_middle(self):
        self.assertEqual(linear_search([10, 20, 30, 40], 30), 2)

    def test_not_found(self):
        self.assertEqual(linear_search([10, 20, 30, 40], 99), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(linear_search([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(linear_search([42], 7), -1)

    def test_does_not_mutate_data(self):
        data = [3, 1, 4, 1, 5]
        original = data.copy()
        linear_search(data, 4)
        self.assertEqual(data, original)


class TestBinarySearch(unittest.TestCase):
    def test_found_at_head(self):
        self.assertEqual(binary_search([10, 20, 30, 40], 10), 0)

    def test_found_at_tail(self):
        self.assertEqual(binary_search([10, 20, 30, 40], 40), 3)

    def test_found_at_middle(self):
        self.assertEqual(binary_search([10, 20, 30, 40], 30), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([10, 20, 30, 40], 99), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([42], 7), -1)

    def test_does_not_mutate_data(self):
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        binary_search(data, 3)
        self.assertEqual(data, original)

    def test_large_list(self):
        data = list(range(10000))
        self.assertEqual(binary_search(data, 0), 0)
        self.assertEqual(binary_search(data, 9999), 9999)
        self.assertEqual(binary_search(data, 5000), 5000)


if __name__ == "__main__":
    unittest.main()
