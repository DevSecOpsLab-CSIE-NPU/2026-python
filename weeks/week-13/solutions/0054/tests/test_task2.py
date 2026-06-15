import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties


class TestTask2(unittest.TestCase):

    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("000"), "其他")

    def test_load_county_counts_type(self):
        result = load_county_counts(112)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(112)
        self.assertIn("澎湖縣", result)
        self.assertGreater(result["澎湖縣"], 0)

    def test_get_top_counties_length(self):
        all_years = {
            112: {"澎湖縣": 50, "台北市": 40, "高雄市": 30, "台中市": 20},
            113: {"澎湖縣": 45, "台北市": 35, "新北市": 25},
        }
        result = get_top_counties(all_years, top_n=2)
        self.assertLessEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
