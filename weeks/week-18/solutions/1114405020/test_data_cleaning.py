import unittest
from data_cleaning import clean_data


class TestDataCleaning(unittest.TestCase):
    def test_sample_1(self):
        """測試範例測資 1 (學號末碼 0，D = 2)
        輸入: 4 7 4 2 9 2 6 7, D = 2
        1. 去重保序: 4 7 2 9 6
        2. D=2 整除: 4 2 6
        3. 升冪排序: 2 4 6
        """
        self.assertEqual(clean_data([4, 7, 4, 2, 9, 2, 6, 7], 2), [2, 4, 6])

    def test_sample_2_none(self):
        """測試範例測資 2 (無偶數符合)
        輸入: 1 3 5, D = 2
        結果應該為空數列 []
        """
        self.assertEqual(clean_data([1, 3, 5], 2), [])

    def test_negative_numbers(self):
        """測試 Edge Case：包含負數與能被 2 整除的數
        輸入: -8, 12, -8, 16, 5, 0, D = 2
        結果: [-8, 0, 12, 16]
        """
        self.assertEqual(clean_data([-8, 12, -8, 16, 5, 0], 2), [-8, 0, 12, 16])

    def test_empty_input(self):
        """測試 Edge Case：空數列"""
        self.assertEqual(clean_data([], 2), [])

    def test_invalid_divisor(self):
        """測試例外處理：D < 1 應拋出 ValueError"""
        with self.assertRaises(ValueError):
            clean_data([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            clean_data([1, 2, 3], -1)


if __name__ == "__main__":
    unittest.main()
