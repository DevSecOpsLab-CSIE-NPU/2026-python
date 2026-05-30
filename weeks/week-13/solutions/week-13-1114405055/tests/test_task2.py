import unittest
from pathlib import Path
from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties, DATA_DIR

class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        """test_zip_to_county_penghu: 880 → 澎湖縣"""
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        """test_zip_to_county_unknown: 未知區號 → 其他"""
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        """test_load_county_counts_type: 回傳型別為 dict"""
        data = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(data, dict)

    def test_load_county_counts_penghu_positive(self):
        """test_load_county_counts_penghu_positive: 澎湖縣人數 > 0"""
        data = load_county_counts(112, DATA_DIR)
        self.assertTrue(data.get("澎湖縣", 0) > 0)

    def test_get_top_counties_length(self):
        """test_get_top_counties_length: 回傳數量不超過 top_n"""
        year_data = {
            112: {f"County{i}": i for i in range(20)}
        }
        top = get_top_counties(year_data, top_n=10)
        self.assertLessEqual(len(top), 10)

if __name__ == '__main__':
    unittest.main()
