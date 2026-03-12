"""
Test Suite for Task 1: Sequence Clean
測試序列清理、排序、篩選功能
"""

import unittest
from task1_sequence_clean import (
    deduplicate, sort_ascending, sort_descending, 
    filter_evens, process_sequence
)


class TestDeduplication(unittest.TestCase):
    """去重功能測試"""
    
    def test_deduplicate_preserves_first_occurrence(self):
        """測試去重保留第一次出現順序"""
        result = deduplicate([5, 3, 5, 2, 9, 2, 8, 3, 1])
        expected = [5, 3, 2, 9, 8, 1]
        self.assertEqual(result, expected)
    
    def test_deduplicate_no_duplicates(self):
        """測試沒有重複值的情況"""
        result = deduplicate([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)
    
    def test_deduplicate_all_same(self):
        """測試所有值相同的邊界情況"""
        result = deduplicate([5, 5, 5, 5])
        expected = [5]
        self.assertEqual(result, expected)


class TestSorting(unittest.TestCase):
    """排序功能測試"""
    
    def test_sort_ascending(self):
        """測試升序排序"""
        result = sort_ascending([5, 3, 5, 2, 9, 2, 8, 3, 1])
        expected = [1, 2, 2, 3, 3, 5, 5, 8, 9]
        self.assertEqual(result, expected)
    
    def test_sort_descending(self):
        """測試降序排序"""
        result = sort_descending([5, 3, 5, 2, 9, 2, 8, 3, 1])
        expected = [9, 8, 5, 5, 3, 3, 2, 2, 1]
        self.assertEqual(result, expected)
    
    def test_sort_empty_list(self):
        """測試空列表排序"""
        result = sort_ascending([])
        expected = []
        self.assertEqual(result, expected)


class TestFilterEvens(unittest.TestCase):
    """偶數篩選功能測試"""
    
    def test_filter_evens_maintains_order(self):
        """測試偶數篩選維持原始順序"""
        result = filter_evens([5, 3, 5, 2, 9, 2, 8, 3, 1])
        expected = [2, 2, 8]
        self.assertEqual(result, expected)
    
    def test_filter_evens_no_even_numbers(self):
        """測試沒有偶數的情況"""
        result = filter_evens([1, 3, 5, 7, 9])
        expected = []
        self.assertEqual(result, expected)
    
    def test_filter_evens_all_even_numbers(self):
        """測試全是偶數的情況"""
        result = filter_evens([2, 4, 6, 8])
        expected = [2, 4, 6, 8]
        self.assertEqual(result, expected)


class TestProcessSequence(unittest.TestCase):
    """完整流程測試"""
    
    def test_process_sequence_example(self):
        """測試作業範例"""
        input_str = "5 3 5 2 9 2 8 3 1"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result['asc'], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result['desc'], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result['evens'], [2, 2, 8])
    
    def test_process_sequence_single_number(self):
        """測試單一數字的邊界情況"""
        input_str = "42"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [42])
        self.assertEqual(result['asc'], [42])
        self.assertEqual(result['desc'], [42])
        self.assertEqual(result['evens'], [42])
    
    def test_process_sequence_increasing_order(self):
        """測試已排序的輸入"""
        input_str = "1 2 3 4 5"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [1, 2, 3, 4, 5])
        self.assertEqual(result['asc'], [1, 2, 3, 4, 5])
        self.assertEqual(result['desc'], [5, 4, 3, 2, 1])
        self.assertEqual(result['evens'], [2, 4])


if __name__ == '__main__':
    unittest.main()
