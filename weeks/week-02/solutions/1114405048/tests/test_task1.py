import unittest
import sys
sys.path.insert(0, '..')
from task1_sequence_clean import deduplicate, sort_asc, sort_desc, filter_evens


class TestSequenceClean(unittest.TestCase):
    """Task 1: Sequence Clean - 3個測試案例 x 4個函式"""
    
    # ===== Test deduplicate =====
    def test_deduplicate_normal(self):
        """正常情況：有重複的整數"""
        result = deduplicate([5, 3, 5, 2, 9, 2, 8, 3, 1])
        self.assertEqual(result, [5, 3, 2, 9, 8, 1])
    
    def test_deduplicate_edge_empty(self):
        """邊界情況：空列表"""
        result = deduplicate([])
        self.assertEqual(result, [])
    
    def test_deduplicate_no_duplicates(self):
        """反例：沒有重複值"""
        result = deduplicate([1, 2, 3, 4])
        self.assertEqual(result, [1, 2, 3, 4])
    
    # ===== Test sort_asc =====
    def test_sort_asc_normal(self):
        """正常情況：有重複的整數"""
        result = sort_asc([5, 3, 5, 2, 9, 2, 8, 3, 1])
        self.assertEqual(result, [1, 2, 2, 3, 3, 5, 5, 8, 9])
    
    def test_sort_asc_edge_single(self):
        """邊界情況：單一元素"""
        result = sort_asc([42])
        self.assertEqual(result, [42])
    
    def test_sort_asc_already_sorted(self):
        """反例：已排序的列表"""
        result = sort_asc([1, 2, 3, 4])
        self.assertEqual(result, [1, 2, 3, 4])
    
    # ===== Test sort_desc =====
    def test_sort_desc_normal(self):
        """正常情況：有重複的整數"""
        result = sort_desc([5, 3, 5, 2, 9, 2, 8, 3, 1])
        self.assertEqual(result, [9, 8, 5, 5, 3, 3, 2, 2, 1])
    
    def test_sort_desc_edge_negative(self):
        """邊界情況：包含負數"""
        result = sort_desc([5, -3, 2, -1])
        self.assertEqual(result, [5, 2, -1, -3])
    
    def test_sort_desc_reverse_sorted(self):
        """反例：已反序排列的列表"""
        result = sort_desc([4, 3, 2, 1])
        self.assertEqual(result, [4, 3, 2, 1])
    
    # ===== Test filter_evens =====
    def test_filter_evens_normal(self):
        """正常情況：有奇偶混合"""
        result = filter_evens([5, 3, 5, 2, 9, 2, 8, 3, 1])
        self.assertEqual(result, [2, 2, 8])
    
    def test_filter_evens_edge_no_evens(self):
        """邊界情況：沒有偶數"""
        result = filter_evens([1, 3, 5, 7])
        self.assertEqual(result, [])
    
    def test_filter_evens_all_evens(self):
        """反例：全部是偶數"""
        result = filter_evens([2, 4, 6, 8])
        self.assertEqual(result, [2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()
