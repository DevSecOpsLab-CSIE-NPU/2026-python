"""0617 任務二 — search.py 測試

涵蓋：
  - linear_search：一般情況、找不到、空 list、重複元素
  - binary_search：一般情況、找不到、空 list、只有一個元素、邊界（第一/最後）
  - 兩者都不修改 data（驗證）
"""

import unittest
from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):

    def test_found_in_middle(self):
        self.assertEqual(linear_search([1, 3, 5, 7, 9], 5), 2)

    def test_found_at_start(self):
        self.assertEqual(linear_search([10, 20, 30], 10), 0)

    def test_found_at_end(self):
        self.assertEqual(linear_search([10, 20, 30], 30), 2)

    def test_not_found(self):
        self.assertEqual(linear_search([1, 2, 3], 99), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_duplicate_returns_first(self):
        """有重複元素時，應回傳第一個出現的 index。"""
        self.assertEqual(linear_search([5, 3, 5, 5], 5), 0)

    def test_does_not_modify_data(self):
        data = [3, 1, 4, 1, 5]
        original = data.copy()
        linear_search(data, 4)
        self.assertEqual(data, original)


class TestBinarySearch(unittest.TestCase):

    def test_found_in_middle(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_found_at_start(self):
        self.assertEqual(binary_search([10, 20, 30], 10), 0)

    def test_found_at_end(self):
        self.assertEqual(binary_search([10, 20, 30], 30), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 4), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([42], 0), -1)

    def test_large_sorted_list(self):
        data = list(range(0, 10000, 2))  # 偶數 0..9998
        self.assertEqual(binary_search(data, 4998), 2499)
        self.assertEqual(binary_search(data, 9998), 4999)
        self.assertEqual(binary_search(data, 1), -1)   # 奇數找不到

    def test_does_not_modify_data(self):
        data = [1, 3, 5, 7, 9]
        original = data.copy()
        binary_search(data, 7)
        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main(verbosity=2)
