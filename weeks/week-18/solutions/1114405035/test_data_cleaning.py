import unittest
from data_cleaning import clean_and_filter_data

class TestDataCleaning(unittest.TestCase):
    def test_sample_case_1(self):
        # 測試範例一（整除數 D=3）
        # 原始：4 7 4 2 9 2 6 7
        # 去重保序：4 7 2 9 6
        # 被 3 整除：9 6
        # 排序後：6 9
        raw_data = [4, 7, 4, 2, 9, 2, 6, 7]
        result = clean_and_filter_data(raw_data, 3)
        self.assertEqual(result, [6, 9])

    def test_sample_case_2(self):
        # 測試範例二（整除數 D=3）
        # 原始：1 3 5
        # 去重保序：1 3 5
        # 被 3 整除：3
        # 排序後：3
        raw_data = [1, 3, 5]
        result = clean_and_filter_data(raw_data, 3)
        self.assertEqual(result, [3])

    def test_edge_case_empty_result(self):
        # 邊角案例：沒有任何數被 3 整除
        raw_data = [1, 2, 4, 5]
        result = clean_and_filter_data(raw_data, 3)
        self.assertEqual(result, [])

    def test_edge_case_negative_and_zero(self):
        # 邊角案例：包含負整數與 0 的狀況（D=3）
        # 原始：0, -3, 4
        # 0 % 3 == 0 (保留), -3 % 3 == 0 (保留)
        # 排序後：-3, 0
        raw_data = [0, -3, 4]
        result = clean_and_filter_data(raw_data, 3)
        self.assertEqual(result, [-3, 0])

    def test_empty_input(self):
        # 邊角案例：輸入空串列
        raw_data = []
        result = clean_and_filter_data(raw_data, 3)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
