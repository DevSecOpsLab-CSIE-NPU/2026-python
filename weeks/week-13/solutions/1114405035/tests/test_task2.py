# -*- coding: utf-8 -*-
import unittest
from pathlib import Path
import os
import sys

# 將上一層目錄加入 sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties

# 動態尋找 assets/stu-data 目錄
curr = Path(__file__).resolve()
DATA_DIR = None
while curr.parent != curr:
    data_dir = curr / "assets" / "stu-data"
    if data_dir.exists():
        DATA_DIR = data_dir
        break
    curr = curr.parent

if DATA_DIR is None:
    DATA_DIR = Path(parent_dir).parent.parent.parent / "assets" / "stu-data"

class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")
        self.assertEqual(zip_to_county("881"), "澎湖縣")
        self.assertEqual(zip_to_county("88411"), "澎湖縣") # 支援 5 碼

    def test_zip_to_county_unknown(self):
        # 測試未知或無效郵遞區號
        self.assertEqual(zip_to_county("999"), "其他")
        self.assertEqual(zip_to_county("abc"), "其他")
        self.assertEqual(zip_to_county(""), "其他")
        
    def test_load_county_counts_type(self):
        data = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(data, dict)
        for k, v in data.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, int)
            
    def test_load_county_counts_penghu_positive(self):
        # 澎湖縣學生人數在 112 年應大於 0
        data = load_county_counts(112, DATA_DIR)
        self.assertGreater(data.get("澎湖縣", 0), 0)
        
    def test_get_top_counties_length(self):
        # 讀取 112 年單年作為測試，限制 top_n 為 5
        single_year_data = {112: load_county_counts(112, DATA_DIR)}
        top_5 = get_top_counties(single_year_data, top_n=5)
        self.assertLessEqual(len(top_5), 5)
        
        # 限制 top_n 為 10
        top_10 = get_top_counties(single_year_data, top_n=10)
        self.assertLessEqual(len(top_10), 10)

if __name__ == "__main__":
    unittest.main()
