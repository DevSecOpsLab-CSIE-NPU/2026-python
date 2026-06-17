"""0617 任務二 — search.py 搜尋函式測試

測試目標:
1. linear_search 找到目標時回傳正確 index
2. linear_search 找不到目標時回傳 -1
3. linear_search 不可修改傳入的 data
4. binary_search 在已排序資料中找到目標時回傳正確 index
5. binary_search 找不到目標時回傳 -1
6. binary_search 不可修改傳入的 data
7. binary_search 在空 list 中搜尋時回傳 -1

注意:
- binary_search 的前提是 data 已排序。
- 未排序 data 的處理方式由 search.py 的 docstring 定義。
"""

import unittest

from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def test_linear_search_returns_index_when_found(self):
        """linear_search 找到目標時，應回傳目標所在 index。"""
        data = [10, 20, 30, 40, 50]

        result = linear_search(data, 30)

        self.assertEqual(result, 2)

    def test_linear_search_returns_minus_one_when_not_found(self):
        """linear_search 找不到目標時，應回傳 -1。"""
        data = [10, 20, 30, 40, 50]

        result = linear_search(data, 99)

        self.assertEqual(result, -1)

    def test_linear_search_does_not_modify_data(self):
        """linear_search 不可以修改傳入的 data。"""
        data = [3, 1, 2]
        original = data.copy()

        linear_search(data, 1)

        self.assertEqual(data, original)

    def test_linear_search_empty_list(self):
        """linear_search 搜尋空 list 時，應回傳 -1。"""
        data = []

        result = linear_search(data, 10)

        self.assertEqual(result, -1)

    def test_linear_search_returns_first_matching_index(self):
        """linear_search 遇到重複元素時，應回傳第一個符合的 index。"""
        data = [5, 3, 5, 7]

        result = linear_search(data, 5)

        self.assertEqual(result, 0)


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_returns_index_when_found(self):
        """binary_search 在已排序資料中找到目標時，應回傳正確 index。"""
        data = [10, 20, 30, 40, 50]

        result = binary_search(data, 40)

        self.assertEqual(result, 3)

    def test_binary_search_returns_minus_one_when_not_found(self):
        """binary_search 找不到目標時，應回傳 -1。"""
        data = [10, 20, 30, 40, 50]

        result = binary_search(data, 99)

        self.assertEqual(result, -1)

    def test_binary_search_does_not_modify_data(self):
        """binary_search 不可以修改傳入的 data。"""
        data = [1, 2, 3, 4, 5]
        original = data.copy()

        binary_search(data, 4)

        self.assertEqual(data, original)

    def test_binary_search_empty_list(self):
        """binary_search 搜尋空 list 時，應回傳 -1。"""
        data = []

        result = binary_search(data, 10)

        self.assertEqual(result, -1)

    def test_binary_search_single_item_found(self):
        """binary_search 在單一元素 list 中找到目標時，應回傳 0。"""
        data = [42]

        result = binary_search(data, 42)

        self.assertEqual(result, 0)

    def test_binary_search_single_item_not_found(self):
        """binary_search 在單一元素 list 中找不到目標時，應回傳 -1。"""
        data = [42]

        result = binary_search(data, 99)

        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()