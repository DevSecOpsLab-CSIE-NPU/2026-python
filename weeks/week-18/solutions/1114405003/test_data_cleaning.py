"""
第一題 資料清理 - 測試檔案
學號: 1114405003
D = 5 (個位 3 % 4 + 2 = 5)
"""
import unittest
from data_cleaning import clean_data


class TestDataCleaning(unittest.TestCase):
    """資料清理測試"""

    def test_sample_1(self):
        """範例測資1: 去重+篩選+排序 -> NONE"""
        nums = [4, 7, 4, 2, 9, 2, 6, 7]
        result = clean_data(nums, 5)
        self.assertEqual(result, [])

    def test_sample_2(self):
        """範例測資2: 去重+篩選+排序 -> [5]"""
        nums = [1, 3, 5]
        result = clean_data(nums, 5)
        self.assertEqual(result, [5])

    def test_empty_after_filter(self):
        """全部被過濾掉"""
        nums = [1, 2, 3, 4]
        result = clean_data(nums, 5)
        self.assertEqual(result, [])

    def test_all_duplicates(self):
        """全部重複，去重後只剩一個"""
        nums = [5, 5, 5, 5]
        result = clean_data(nums, 5)
        self.assertEqual(result, [5])

    def test_single_element(self):
        """n=1 單一元素"""
        nums = [10]
        result = clean_data(nums, 5)
        self.assertEqual(result, [10])

    def test_single_element_filtered(self):
        """n=1 單一元素被過濾"""
        nums = [3]
        result = clean_data(nums, 5)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        """含負數"""
        nums = [-10, -5, 0, 5, 10]
        result = clean_data(nums, 5)
        self.assertEqual(result, [-10, -5, 0, 5, 10])

    def test_zero(self):
        """含0，0能被任何數整除"""
        nums = [0, 1, 2, 3]
        result = clean_data(nums, 5)
        self.assertEqual(result, [0])

    def test_already_sorted(self):
        """已排序的輸入"""
        nums = [5, 10, 15, 20]
        result = clean_data(nums, 5)
        self.assertEqual(result, [5, 10, 15, 20])

    def test_reverse_sorted(self):
        """反向排序的輸入"""
        nums = [20, 15, 10, 5]
        result = clean_data(nums, 5)
        self.assertEqual(result, [5, 10, 15, 20])

    def test_large_numbers(self):
        """大數"""
        nums = [10**9, -10**9, 0]
        result = clean_data(nums, 5)
        self.assertEqual(result, [-10**9, 0, 10**9])

    def test_preserve_first_occurrence(self):
        """去重時保留第一次出現的順序"""
        nums = [3, 5, 3, 10, 5, 15]
        result = clean_data(nums, 5)
        self.assertEqual(result, [5, 10, 15])

    def test_d_equals_1(self):
        """D=1 時所有數都保留"""
        nums = [3, 1, 4, 1, 5, 9]
        result = clean_data(nums, 1)
        self.assertEqual(result, [1, 3, 4, 5, 9])

    def test_d_equals_2(self):
        """D=2 只保留偶數"""
        nums = [1, 2, 3, 4, 5, 6]
        result = clean_data(nums, 2)
        self.assertEqual(result, [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
