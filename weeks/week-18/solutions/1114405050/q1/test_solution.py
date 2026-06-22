import unittest
from solution import clean_data

class TestDataCleaning(unittest.TestCase):
    def test_sample_case(self):
        # 範例測試案例: D=2
        # 輸入: 4 7 4 2 9 2 6 7
        # 步驟: 
        # 1. 去重: 4 7 2 9 6
        # 2. D=2整除: 4 2 6
        # 3. 排序: 2 4 6
        self.assertEqual(clean_data(8, [4, 7, 4, 2, 9, 2, 6, 7], 2), [2, 4, 6])

    def test_none_case(self):
        # 無符合案例: D=2
        # 輸入: 1 3 5
        # 步驟:
        # 1. 去重: 1 3 5
        # 2. D=2整除: None
        self.assertEqual(clean_data(3, [1, 3, 5], 2), [])

    def test_edge_case_empty(self):
        # 邊界案例: 空陣列
        self.assertEqual(clean_data(0, [], 2), [])

    def test_negative_numbers(self):
        # 負數案例: D=2
        # 輸入: -4, -2, -1, 0, 2, 4
        # 步驟:
        # 1. 去重: -4, -2, -1, 0, 2, 4
        # 2. D=2整除: -4, -2, 0, 2, 4
        # 3. 排序: -4, -2, 0, 2, 4
        self.assertEqual(clean_data(6, [-4, -2, -1, 0, 2, 4], 2), [-4, -2, 0, 2, 4])

if __name__ == '__main__':
    unittest.main()
