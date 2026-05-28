"""
Task 2 單元測試：zip_to_county / load_county_counts / get_top_counties
TDD：先寫測試，再實作函式。
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties, DATA_DIR

ALL_YEARS = [109, 110, 111, 112, 113, 114]


class TestZipToCounty(unittest.TestCase):

    def test_zip_to_county_penghu(self):
        """880 → 澎湖縣"""
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        """未知區號 → 其他"""
        self.assertEqual(zip_to_county("000"), "其他")


class TestLoadCountyCounts(unittest.TestCase):

    def test_load_county_counts_type(self):
        """回傳型別必須是 dict"""
        result = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        """澎湖縣學生人數應大於 0（學校位於澎湖）"""
        result = load_county_counts(112, DATA_DIR)
        penghu_count = result.get("澎湖縣", 0)
        self.assertGreater(penghu_count, 0)


class TestGetTopCounties(unittest.TestCase):

    def setUp(self):
        self.all_years = {year: load_county_counts(year, DATA_DIR) for year in ALL_YEARS}

    def test_get_top_counties_length(self):
        """回傳數量不超過 top_n"""
        result = get_top_counties(self.all_years, top_n=10)
        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()