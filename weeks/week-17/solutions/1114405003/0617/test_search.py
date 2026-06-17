"""0617 任務二 — linear_search / binary_search 測試

紅燈 commit: test: 0617 搜尋函式測試
綠燈 commit: feat: 0617 實作 linear_search / binary_search
"""

import unittest

from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def test_found(self):
        """找到 target,回傳第一個 index"""
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        """找不到 target,回傳 -1"""
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        """空 list,回傳 -1"""
        self.assertEqual(linear_search([], 1), -1)

    def test_duplicates(self):
        """重複元素,回傳第一個 index"""
        self.assertEqual(linear_search([1, 2, 2, 2, 3], 2), 1)

    def test_first_element(self):
        """target 在第一個位置"""
        self.assertEqual(linear_search([10, 20, 30], 10), 0)

    def test_last_element(self):
        """target 在最後一個位置"""
        self.assertEqual(linear_search([10, 20, 30], 30), 2)

    def test_does_not_modify_data(self):
        """不可修改傳入的 data"""
        data = [3, 1, 4, 1, 5]
        original = data.copy()
        linear_search(data, 4)
        self.assertEqual(data, original)


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        """找到 target,回傳第一個 index"""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        """找不到 target,回傳 -1"""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        """空 list,回傳 -1"""
        self.assertEqual(binary_search([], 1), -1)

    def test_duplicates(self):
        """重複元素,回傳第一個 index"""
        self.assertEqual(binary_search([1, 2, 2, 2, 3], 2), 1)

    def test_first_element(self):
        """target 在第一個位置"""
        self.assertEqual(binary_search([10, 20, 30], 10), 0)

    def test_last_element(self):
        """target 在最後一個位置"""
        self.assertEqual(binary_search([10, 20, 30], 30), 2)

    def test_does_not_modify_data(self):
        """不可修改傳入的 data"""
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        binary_search(data, 3)
        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
