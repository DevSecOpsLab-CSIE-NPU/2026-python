"""
Test for Task 1: Sequence Clean
"""

import unittest
from task1_sequence_clean import (
    deduplicate,
    sort_ascending,
    sort_descending,
    filter_evens,
    sequence_clean,
    format_output
)


class TestDeduplicateFunction(unittest.TestCase):
    """測試去重函式。"""
    
    def test_deduplicate_basic(self):
        """基本去重測試：正常序列去重。"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [5, 3, 2, 9, 8, 1]
        self.assertEqual(deduplicate(numbers), expected)
    
    def test_deduplicate_no_duplicates(self):
        """邊界測試：沒有重複元素。"""
        numbers = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(deduplicate(numbers), expected)
    
    def test_deduplicate_all_same(self):
        """邊界測試：全部元素相同。"""
        numbers = [7, 7, 7, 7]
        expected = [7]
        self.assertEqual(deduplicate(numbers), expected)


class TestSortAscendingFunction(unittest.TestCase):
    """測試升序排序函式。"""
    
    def test_sort_ascending_basic(self):
        """基本升序測試。"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [1, 2, 2, 3, 3, 5, 5, 8, 9]
        self.assertEqual(sort_ascending(numbers), expected)
    
    def test_sort_ascending_already_sorted(self):
        """邊界測試：已排序序列。"""
        numbers = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(sort_ascending(numbers), expected)
    
    def test_sort_ascending_reverse_order(self):
        """邊界測試：反向序列。"""
        numbers = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(sort_ascending(numbers), expected)


class TestSortDescendingFunction(unittest.TestCase):
    """測試降序排序函式。"""
    
    def test_sort_descending_basic(self):
        """基本降序測試。"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [9, 8, 5, 5, 3, 3, 2, 2, 1]
        self.assertEqual(sort_descending(numbers), expected)
    
    def test_sort_descending_already_sorted(self):
        """邊界測試：已反向排序序列。"""
        numbers = [5, 4, 3, 2, 1]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(sort_descending(numbers), expected)
    
    def test_sort_descending_ascending_order(self):
        """邊界測試：升序序列。"""
        numbers = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(sort_descending(numbers), expected)


class TestFilterEvensFunction(unittest.TestCase):
    """測試篩選偶數函式。"""
    
    def test_filter_evens_basic(self):
        """基本篩選測試。"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [2, 2, 8]
        self.assertEqual(filter_evens(numbers), expected)
    
    def test_filter_evens_no_evens(self):
        """邊界測試：沒有偶數。"""
        numbers = [1, 3, 5, 7, 9]
        expected = []
        self.assertEqual(filter_evens(numbers), expected)
    
    def test_filter_evens_all_evens(self):
        """邊界測試：全部都是偶數。"""
        numbers = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        self.assertEqual(filter_evens(numbers), expected)


class TestSequenceCleanIntegration(unittest.TestCase):
    """整合測試：sequence_clean 函式。"""
    
    def test_sequence_clean_basic(self):
        """基本整合測試：使用題目範例。"""
        input_str = "5 3 5 2 9 2 8 3 1"
        result = sequence_clean(input_str)
        
        self.assertEqual(result['dedupe'], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result['asc'], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result['desc'], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result['evens'], [2, 2, 8])
    
    def test_sequence_clean_single_number(self):
        """邊界測試：單一數字。"""
        input_str = "42"
        result = sequence_clean(input_str)
        
        self.assertEqual(result['dedupe'], [42])
        self.assertEqual(result['asc'], [42])
        self.assertEqual(result['desc'], [42])
        self.assertEqual(result['evens'], [42])
    
    def test_sequence_clean_no_evens(self):
        """邊界測試：沒有偶數。"""
        input_str = "1 3 5 7"
        result = sequence_clean(input_str)
        
        self.assertEqual(result['dedupe'], [1, 3, 5, 7])
        self.assertEqual(result['evens'], [])


class TestFormatOutput(unittest.TestCase):
    """測試輸出格式化函式。"""
    
    def test_format_output_basic(self):
        """基本格式化測試。"""
        results = {
            'dedupe': [5, 3, 2, 9, 8, 1],
            'asc': [1, 2, 2, 3, 3, 5, 5, 8, 9],
            'desc': [9, 8, 5, 5, 3, 3, 2, 2, 1],
            'evens': [2, 2, 8]
        }
        output = format_output(results)
        expected_lines = [
            "dedupe: 5 3 2 9 8 1",
            "asc: 1 2 2 3 3 5 5 8 9",
            "desc: 9 8 5 5 3 3 2 2 1",
            "evens: 2 2 8"
        ]
        self.assertEqual(output, '\n'.join(expected_lines))


if __name__ == '__main__':
    unittest.main()
