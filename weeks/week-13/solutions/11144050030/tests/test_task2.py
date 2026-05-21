import unittest
from pathlib import Path
from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"


class TestTask2(unittest.TestCase):

    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        result = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(112, DATA_DIR)
        self.assertGreater(result.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self):
        years = [109, 110, 111, 112, 113, 114]
        all_years = {y: load_county_counts(y, DATA_DIR) for y in years}
        top = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top), 10)


if __name__ == "__main__":
    unittest.main()
