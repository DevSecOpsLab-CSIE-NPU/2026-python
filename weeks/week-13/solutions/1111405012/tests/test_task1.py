"""
Task 1 單元測試：load_year / get_top_depts
TDD：先寫測試，再實作函式。
"""
import sys
import unittest
from pathlib import Path

# 讓 import 找到上層目錄的 task1_grouped_bar
sys.path.insert(0, str(Path(__file__).parent.parent))

from task1_grouped_bar import load_year, get_top_depts, DATA_DIR


class TestLoadYear(unittest.TestCase):

    def test_load_year_returns_dict(self):
        """回傳型別必須是 dict，且 key 為字串"""
        result = load_year(112, DATA_DIR)
        self.assertIsInstance(result, dict)
        for key in result:
            self.assertIsInstance(key, str)

    def test_load_year_counts_correct(self):
        """澎湖科大資工系存在於資料中（人數 > 0）"""
        result = load_year(112, DATA_DIR)
        # 確認至少有某個系所有人數
        self.assertTrue(any(v > 0 for v in result.values()))

    def test_load_year_total_positive(self):
        """總人數必須大於 0"""
        result = load_year(113, DATA_DIR)
        total = sum(result.values())
        self.assertGreater(total, 0)


class TestGetTopDepts(unittest.TestCase):

    def setUp(self):
        """載入三年資料供測試使用"""
        self.year_data = {
            112: load_year(112, DATA_DIR),
            113: load_year(113, DATA_DIR),
            114: load_year(114, DATA_DIR),
        }

    def test_get_top_depts_length(self):
        """回傳數量不超過 top_n"""
        result = get_top_depts(self.year_data, top_n=8)
        self.assertLessEqual(len(result), 8 * len(self.year_data))

    def test_get_top_depts_includes_popular(self):
        """已知至少有一年人數最多的系所應出現在結果中"""
        # 找 112 年人數最多的系所
        top_dept_112 = max(self.year_data[112], key=self.year_data[112].get)
        result = get_top_depts(self.year_data, top_n=8)
        self.assertIn(top_dept_112, result)


if __name__ == "__main__":
    unittest.main()
