import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"


class TestTask2(unittest.TestCase):

    def setUp(self):
        from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties
        self.zip_to_county = zip_to_county
        self.load_county_counts = load_county_counts
        self.get_top_counties = get_top_counties

    def test_zip_to_county_penghu(self):
        self.assertEqual(self.zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(self.zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        data = self.load_county_counts(114, DATA_DIR)
        self.assertIsInstance(data, dict)

    def test_load_county_counts_penghu_positive(self):
        data = self.load_county_counts(114, DATA_DIR)
        self.assertIn("澎湖縣", data)
        self.assertGreater(data["澎湖縣"], 0)

    def test_get_top_counties_length(self):
        all_years = {y: self.load_county_counts(y, DATA_DIR) for y in range(109, 115)}
        top = self.get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top), 10)


if __name__ == "__main__":
    unittest.main()
