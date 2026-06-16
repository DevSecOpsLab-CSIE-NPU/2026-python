from pathlib import Path
import unittest

from task2_zipcode_heatmap import get_top_counties, load_county_counts, zip_to_county


DATA_DIR = Path(__file__).resolve().parents[5] / "assets" / "stu-data"


class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        result = load_county_counts(109, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(109, DATA_DIR)
        self.assertGreater(result["澎湖縣"], 0)

    def test_get_top_counties_length(self):
        all_years = {year: load_county_counts(year, DATA_DIR) for year in [109, 110, 111, 112, 113, 114]}
        result = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()