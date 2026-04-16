"""tests/test_task1.py — Task 1: Sequence Clean 的單元測試"""
import unittest
import sys
import os

# 讓測試可以 import 上一層的模組
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from task1_sequence_clean import dedupe_ordered, sort_asc, sort_desc, filter_evens


class TestDedupeOrdered(unittest.TestCase):
    """測試去重且保留順序的函式。"""

    def test_normal_case(self):
        """一般情況：有多個重複值。"""
        self.assertEqual(dedupe_ordered([5, 3, 5, 2, 9, 2, 8, 3, 1]), [5, 3, 2, 9, 8, 1])

    def test_no_duplicates(self):
        """已無重複值時，輸出應與輸入相同。"""
        self.assertEqual(dedupe_ordered([1, 2, 3]), [1, 2, 3])

    def test_all_same(self):
        """全部相同時，只保留第一個。"""
        self.assertEqual(dedupe_ordered([7, 7, 7]), [7])

    def test_empty(self):
        """空列表應回傳空列表。"""
        self.assertEqual(dedupe_ordered([]), [])

    def test_preserves_order(self):
        """確認第一次出現的順序被保留（後面的重複應被去除）。"""
        self.assertEqual(dedupe_ordered([3, 1, 2, 1, 3]), [3, 1, 2])


class TestSortAsc(unittest.TestCase):
    """測試由小到大排序（保留重複值）。"""

    def test_normal_case(self):
        """含重複值的一般輸入。"""
        self.assertEqual(sort_asc([5, 3, 5, 2, 9, 2, 8, 3, 1]),
                         [1, 2, 2, 3, 3, 5, 5, 8, 9])

    def test_already_sorted(self):
        """已排好序的輸入，輸出不變。"""
        self.assertEqual(sort_asc([1, 2, 3]), [1, 2, 3])

    def test_single_element(self):
        """單一元素仍可正確處理。"""
        self.assertEqual(sort_asc([42]), [42])


class TestSortDesc(unittest.TestCase):
    """測試由大到小排序（保留重複值）。"""

    def test_normal_case(self):
        """含重複值的一般輸入。"""
        self.assertEqual(sort_desc([5, 3, 5, 2, 9, 2, 8, 3, 1]),
                         [9, 8, 5, 5, 3, 3, 2, 2, 1])

    def test_already_desc(self):
        """已降序排列的輸入，輸出不變。"""
        self.assertEqual(sort_desc([9, 8, 7]), [9, 8, 7])

    def test_single_element(self):
        """單一元素仍可正確處理。"""
        self.assertEqual(sort_desc([5]), [5])


class TestFilterEvens(unittest.TestCase):
    """測試偶數篩選（保留原始順序與重複值）。"""

    def test_normal_case(self):
        """含重複偶數的一般輸入。"""
        self.assertEqual(filter_evens([5, 3, 5, 2, 9, 2, 8, 3, 1]), [2, 2, 8])

    def test_no_evens(self):
        """全為奇數時，應回傳空列表。"""
        self.assertEqual(filter_evens([1, 3, 5]), [])

    def test_all_evens(self):
        """全為偶數時，輸出與輸入相同。"""
        self.assertEqual(filter_evens([2, 4, 6]), [2, 4, 6])

    def test_empty(self):
        """空列表應回傳空列表。"""
        self.assertEqual(filter_evens([]), [])


if __name__ == "__main__":
    unittest.main()
