"""0617 任務二 — linear_search / binary_search 測試"""

import unittest
from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def test_finds_target_in_middle(self):
        result = linear_search([10, 20, 30, 40], 30)
        self.assertEqual(result, 2)

    def test_returns_minus_one_when_not_found(self):
        result = linear_search([1, 2, 3], 99)
        self.assertEqual(result, -1)

    def test_finds_target_at_beginning(self):
        result = linear_search([5, 10, 15], 5)
        self.assertEqual(result, 0)

    def test_finds_target_at_end(self):
        result = linear_search([5, 10, 15], 15)
        self.assertEqual(result, 2)

    def test_empty_list_returns_minus_one(self):
        result = linear_search([], 1)
        self.assertEqual(result, -1)

    def test_rejects_none_data(self):
        with self.assertRaises(ValueError):
            linear_search(None, 5)


class TestBinarySearch(unittest.TestCase):
    def test_finds_target_in_sorted(self):
        result = binary_search([10, 20, 30, 40, 50], 30)
        self.assertEqual(result, 2)

    def test_returns_minus_one_when_not_found(self):
        result = binary_search([1, 2, 3, 4], 99)
        self.assertEqual(result, -1)

    def test_empty_list_returns_minus_one(self):
        result = binary_search([], 1)
        self.assertEqual(result, -1)

    def test_rejects_none_data(self):
        with self.assertRaises(ValueError):
            binary_search(None, 5)


if __name__ == "__main__":
    unittest.main()
