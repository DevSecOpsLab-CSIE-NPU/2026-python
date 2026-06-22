import unittest
from clean_data import clean_data


class TestCleanData(unittest.TestCase):

    def test_basic_functionality(self):
        # 測試基本流程：去重 -> 篩選(D=4) -> 排序
        self.assertEqual(clean_data([4, 7, 4, 8, 12, 2, 16, 7], 4), [4, 8, 12, 16])

    def test_all_filtered_out(self):
        # 測試所有數字都被篩掉
        self.assertEqual(clean_data([1, 2, 3], 4), "NONE")

    def test_empty_list(self):
        # 測試空 list
        self.assertEqual(clean_data([], 4), "NONE")

    def test_d_zero_returns_none(self):
        # 測試 d=0 時回傳 "NONE"
        self.assertEqual(clean_data([1, 2, 3], 0), "NONE")

    def test_preserves_first_occurrence_then_sorts(self):
        # 測試去重保序後再排序
        # [10, 2, 10, 4] -> 去重 [10, 2, 4] -> 篩選(D=2) [10, 2, 4] -> 排序 [2, 4, 10]
        self.assertEqual(clean_data([10, 2, 10, 4], 2), [2, 4, 10])


if __name__ == "__main__":
    unittest.main()
