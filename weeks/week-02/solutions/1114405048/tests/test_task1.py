"""
Task 1 Unit Tests: Sequence Clean
測試序列去重、排序、篩選偶數功能
"""

import unittest
from task1_sequence_clean import (
    deduplicate,
    sort_ascending,
    sort_descending,
    filter_evens,
    process_sequence
)


class TestDeduplicate(unittest.TestCase):
    """測試去重功能"""
    
    def test_deduplicate_normal(self):
        """正常情況：包含重複元素"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [5, 3, 2, 9, 8, 1]
        self.assertEqual(deduplicate(numbers), expected)
    
    def test_deduplicate_no_duplicates(self):
        """邊界：沒有重複元素"""
        numbers = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(deduplicate(numbers), expected)
    
    def test_deduplicate_all_same(self):
        """反例：所有元素相同"""
        numbers = [5, 5, 5, 5]
        expected = [5]
        self.assertEqual(deduplicate(numbers), expected)


class TestSorting(unittest.TestCase):
    """測試排序功能"""
    
    def test_sort_ascending_normal(self):
        """由小到大排序"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [1, 2, 2, 3, 3, 5, 5, 8, 9]
        self.assertEqual(sort_ascending(numbers), expected)
    
    def test_sort_descending_normal(self):
        """由大到小排序"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [9, 8, 5, 5, 3, 3, 2, 2, 1]
        self.assertEqual(sort_descending(numbers), expected)
    
    def test_sort_negative_numbers(self):
        """包含負數的排序"""
        numbers = [3, -1, 0, 2, -5]
        asc = sort_ascending(numbers)
        desc = sort_descending(numbers)
        self.assertEqual(asc, [-5, -1, 0, 2, 3])
        self.assertEqual(desc, [3, 2, 0, -1, -5])


class TestFilterEvens(unittest.TestCase):
    """測試偶數篩選"""
    
    def test_filter_evens_normal(self):
        """正常情況：包含奇偶數"""
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [2, 2, 8]
        self.assertEqual(filter_evens(numbers), expected)
    
    def test_filter_evens_all_odd(self):
        """邊界：全是奇數"""
        numbers = [1, 3, 5, 7, 9]
        expected = []
        self.assertEqual(filter_evens(numbers), expected)
    
    def test_filter_evens_all_even(self):
        """邊界：全是偶數"""
        numbers = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        self.assertEqual(filter_evens(numbers), expected)


class TestProcessSequence(unittest.TestCase):
    """測試完整的序列處理函式"""
    
    def test_process_sequence_example(self):
        """使用題目範例"""
        input_line = "5 3 5 2 9 2 8 3 1"
        output = process_sequence(input_line)
        self.assertEqual(len(output), 4)
        self.assertEqual(output[0], "dedupe: 5 3 2 9 8 1")
        self.assertEqual(output[1], "asc: 1 2 2 3 3 5 5 8 9")
        self.assertEqual(output[2], "desc: 9 8 5 5 3 3 2 2 1")
        self.assertEqual(output[3], "evens: 2 2 8")
    
    def test_process_sequence_single_element(self):
        """只有一個元素"""
        input_line = "42"
        output = process_sequence(input_line)
        self.assertEqual(output[0], "dedupe: 42")
        self.assertEqual(output[1], "asc: 42")
        self.assertEqual(output[2], "desc: 42")
        self.assertEqual(output[3], "evens: 42")
    
    def test_process_sequence_no_evens(self):
        """沒有偶數"""
        input_line = "1 3 5 7"
        output = process_sequence(input_line)
        self.assertEqual(output[3], "evens: ")


if __name__ == "__main__":
    unittest.main()
