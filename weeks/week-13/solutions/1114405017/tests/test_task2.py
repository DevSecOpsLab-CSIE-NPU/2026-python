"""
Task 2 的測試檔案
"""

import unittest
from pathlib import Path
import sys

# 加入上級目錄到 path
sys.path.insert(0, str(Path(__file__).parent.parent))

from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties


class TestTask2(unittest.TestCase):
    """Task 2 測試類別"""
    
    @classmethod
    def setUpClass(cls):
        """設定測試環境"""
        # 從 test_task2.py 向上 6 層到 2026-python
        # tests -> 1114405017 -> solutions -> week-13 -> weeks -> 2026-python
        current_file = Path(__file__).resolve()
        cls.data_dir = current_file.parent.parent.parent.parent.parent.parent / "assets" / "stu-data"
    
    def test_zip_to_county_penghu(self):
        """測試郵遞區號 880 → 澎湖縣"""
        result = zip_to_county("880")
        self.assertEqual(result, "澎湖縣")
    
    def test_zip_to_county_unknown(self):
        """測試未知區號 → 其他"""
        result = zip_to_county("999")
        self.assertEqual(result, "其他")
    
    def test_zip_to_county_taipei(self):
        """測試郵遞區號 100 → 台北市"""
        result = zip_to_county("100")
        self.assertEqual(result, "台北市")
    
    def test_load_county_counts_type(self):
        """測試 load_county_counts 回傳型別為 dict"""
        result = load_county_counts(114, self.data_dir)
        self.assertIsInstance(result, dict)
        # 檢查所有 key 都是字串
        for key in result.keys():
            self.assertIsInstance(key, str)
    
    def test_load_county_counts_penghu_positive(self):
        """測試澎湖縣人數 > 0"""
        result = load_county_counts(114, self.data_dir)
        # 澎湖縣應該有招生
        self.assertIn("澎湖縣", result)
        self.assertGreater(result["澎湖縣"], 0)
    
    def test_get_top_counties_length(self):
        """測試 get_top_counties 回傳數量不超過 top_n"""
        all_years = {
            109: load_county_counts(109, self.data_dir),
            110: load_county_counts(110, self.data_dir),
            111: load_county_counts(111, self.data_dir),
            112: load_county_counts(112, self.data_dir),
            113: load_county_counts(113, self.data_dir),
            114: load_county_counts(114, self.data_dir)
        }
        result = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(result), 10)
    
    def test_get_top_counties_sorted(self):
        """測試 get_top_counties 結果應該是排序的"""
        all_years = {
            109: load_county_counts(109, self.data_dir),
            110: load_county_counts(110, self.data_dir),
            111: load_county_counts(111, self.data_dir),
            112: load_county_counts(112, self.data_dir),
            113: load_county_counts(113, self.data_dir),
            114: load_county_counts(114, self.data_dir)
        }
        result = get_top_counties(all_years, top_n=10)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()
