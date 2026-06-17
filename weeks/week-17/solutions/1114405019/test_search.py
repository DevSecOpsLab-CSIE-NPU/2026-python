"""0617 任務二 — search.py 輕量測試(不要求完整紅綠燈)。"""

import unittest

from search import binary_search, linear_search


class TestLinearSearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(linear_search([5, 3, 8, 1], 8), 2)

    def test_not_found(self):
        self.assertEqual(linear_search([5, 3, 8, 1], 99), -1)

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        linear_search(data, 2)
        self.assertEqual(data, [3, 1, 2])


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 7), 3)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 4), -1)

    def test_does_not_mutate_input(self):
        data = [1, 2, 3]
        binary_search(data, 2)
        self.assertEqual(data, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
