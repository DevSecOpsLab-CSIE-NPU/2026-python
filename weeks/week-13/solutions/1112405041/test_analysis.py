"""Stage 2: analysis 測試"""
import unittest
from pathlib import Path
from data_loader import load_year, load_county_counts

DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"

# 預載資料供測試使用（只載一次）
YEAR_DATA = {y: load_year(y, DATA_DIR) for y in range(109, 115)}
COUNTY_DATA = {y: load_county_counts(y, DATA_DIR) for y in range(109, 115)}


class TestGetTopDepts(unittest.TestCase):
    def test_get_top_depts_length(self):
        from analysis import get_top_depts
        result = get_top_depts(YEAR_DATA, top_n=8)
        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self):
        from analysis import get_top_depts
        result = get_top_depts(YEAR_DATA, top_n=8)
        self.assertIn("資訊工程系", result)

    def test_get_top_depts_empty_year_data(self):
        from analysis import get_top_depts
        result = get_top_depts({}, top_n=8)
        self.assertEqual(result, [])

    def test_get_top_depts_top_n_zero(self):
        from analysis import get_top_depts
        result = get_top_depts(YEAR_DATA, top_n=0)
        self.assertEqual(result, [])


class TestGetTopCounties(unittest.TestCase):
    def test_get_top_counties_length(self):
        from analysis import get_top_counties
        result = get_top_counties(COUNTY_DATA, top_n=10)
        self.assertLessEqual(len(result), 10)

    def test_get_top_counties_includes_penghu(self):
        from analysis import get_top_counties
        result = get_top_counties(COUNTY_DATA, top_n=10)
        self.assertIn("澎湖縣", result)

    def test_get_top_counties_empty_data(self):
        from analysis import get_top_counties
        result = get_top_counties({}, top_n=10)
        self.assertEqual(result, [])

    def test_get_top_counties_top_n_zero(self):
        from analysis import get_top_counties
        result = get_top_counties(COUNTY_DATA, top_n=0)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
