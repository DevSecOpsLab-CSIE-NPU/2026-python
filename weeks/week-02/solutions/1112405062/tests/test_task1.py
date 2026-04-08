"""
================================================================================
Task 1: Sequence Clean 測試程式
================================================================================

題目說明：
    給定一行以空白分隔的整數，請輸出：
    1. 去重後（保留第一次出現順序）的序列
    2. 由小到大排序結果
    3. 由大到小排序結果
    4. 偶數序列（維持原始順序）

================================================================================
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task1_sequence_clean import sequence_clean

class TestSequenceClean(unittest.TestCase):
    """測試序列清理功能"""

    def test_basic_case(self):
        """測試基本情況：5 3 5 2 9 2 8 3 1"""
        input_data = "5 3 5 2 9 2 8 3 1"
        result = sequence_clean(input_data)
        self.assertEqual(result["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result["evens"], [2, 2, 8])

    def test_empty_input(self):
        """測試空輸入"""
        input_data = ""
        result = sequence_clean(input_data)
        self.assertEqual(result["dedupe"], [])
        self.assertEqual(result["asc"], [])
        self.assertEqual(result["desc"], [])
        self.assertEqual(result["evens"], [])

    def test_single_element(self):
        """測試單一元素"""
        input_data = "7"
        result = sequence_clean(input_data)
        self.assertEqual(result["dedupe"], [7])
        self.assertEqual(result["asc"], [7])
        self.assertEqual(result["desc"], [7])
        self.assertEqual(result["evens"], [])

    def test_all_same(self):
        """測試全部相同元素"""
        input_data = "5 5 5 5"
        result = sequence_clean(input_data)
        self.assertEqual(result["dedupe"], [5])
        self.assertEqual(result["asc"], [5, 5, 5, 5])
        self.assertEqual(result["desc"], [5, 5, 5, 5])
        self.assertEqual(result["evens"], [5, 5, 5, 5])

    def test_no_evens(self):
        """測試無偶數情況"""
        input_data = "1 3 5 7"
        result = sequence_clean(input_data)
        self.assertEqual(result["evens"], [])

    def test_only_evens(self):
        """測試全是偶數情況"""
        input_data = "2 4 6 8"
        result = sequence_clean(input_data)
        self.assertEqual(result["evens"], [2, 4, 6, 8])

    def test_negative_numbers(self):
        """測試包含負數"""
        input_data = "-3 2 -1 2 0"
        result = sequence_clean(input_data)
        self.assertEqual(result["dedupe"], [-3, 2, -1, 0])
        self.assertEqual(result["evens"], [2, 2, 0])


if __name__ == "__main__":
    unittest.main()
