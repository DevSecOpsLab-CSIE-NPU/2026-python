import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task1_sequence_clean import process_sequence


class TestTask1SequenceClean(unittest.TestCase):
    """Task 1: Sequence Clean 測試類別"""

    def test_normal_case(self):
        """一般情況：正常數列去重、排序、偶數"""
        result = process_sequence("5 3 5 2 9 2 8 3 1")
        self.assertEqual(result["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result["evens"], [2, 2, 8])

    def test_all_same(self):
        """邊界情況：所有元素相同"""
        result = process_sequence("8 8 8 8")
        self.assertEqual(result["dedupe"], [8])
        self.assertEqual(result["asc"], [8, 8, 8, 8])
        self.assertEqual(result["desc"], [8, 8, 8, 8])
        self.assertEqual(result["evens"], [8, 8, 8, 8])

    def test_empty_input(self):
        """邊界情況：空字串"""
        result = process_sequence("")
        self.assertEqual(result["dedupe"], [])
        self.assertEqual(result["asc"], [])
        self.assertEqual(result["desc"], [])
        self.assertEqual(result["evens"], [])

    def test_all_odd(self):
        """反例：全部是奇數，偶數序列應為空"""
        result = process_sequence("1 3 5 7")
        self.assertEqual(result["dedupe"], [1, 3, 5, 7])
        self.assertEqual(result["evens"], [])

    def test_all_even(self):
        """反例：全部是偶數"""
        result = process_sequence("4 2 6 8")
        self.assertEqual(result["dedupe"], [4, 2, 6, 8])
        self.assertEqual(result["evens"], [4, 2, 6, 8])

    def test_preserve_order_in_dedupe(self):
        """驗證去重保留第一次出現順序"""
        result = process_sequence("1 2 1 3 2 4")
        self.assertEqual(result["dedupe"], [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
