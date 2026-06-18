# -*- coding: utf-8 -*-
import unittest
from pathlib import Path
import os
import sys

# 將上一層目錄加入 sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from task1_grouped_bar import load_year, get_top_depts

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
    # 備用路徑
    DATA_DIR = Path(parent_dir).parent.parent.parent / "assets" / "stu-data"

class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self):
        data = load_year(112, DATA_DIR)
        self.assertIsInstance(data, dict)
        for k, v in data.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, int)
            
    def test_load_year_counts_correct(self):
        data = load_year(112, DATA_DIR)
        # 112年 資訊工程系 人數應為 53 人，觀光休閒系人數應為 61 人
        self.assertEqual(data.get("資訊工程系"), 53)
        self.assertEqual(data.get("觀光休閒系"), 61)
        
    def test_load_year_total_positive(self):
        data = load_year(112, DATA_DIR)
        total = sum(data.values())
        self.assertGreater(total, 0)
        
    def test_get_top_depts_length(self):
        # 傳入單一年份資料，回傳數量不應超過 top_n
        single_year_data = {112: load_year(112, DATA_DIR)}
        top_3 = get_top_depts(single_year_data, top_n=3)
        self.assertLessEqual(len(top_3), 3)
        
        top_8 = get_top_depts(single_year_data, top_n=8)
        self.assertLessEqual(len(top_8), 8)
        
    def test_get_top_depts_includes_popular(self):
        # 資訊工程系、觀光休閒系、食品科學系是熱門系所，應在結果中
        single_year_data = {112: load_year(112, DATA_DIR)}
        top_8 = get_top_depts(single_year_data, top_n=8)
        self.assertIn("資訊工程系", top_8)
        self.assertIn("觀光休閒系", top_8)
        self.assertIn("食品科學系", top_8)

if __name__ == "__main__":
    unittest.main()
