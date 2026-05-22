import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"

class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")
        self.assertEqual(zip_to_county("88012"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("999"), "其他")
        self.assertEqual(zip_to_county("abc"), "其他")

    def test_load_county_counts_type(self):
        result = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(112, DATA_DIR)
        self.assertIn("澎湖縣", result)
        self.assertGreater(result["澎湖縣"], 0)

    def test_get_top_counties_length(self):
        all_years = {
            112: load_county_counts(112, DATA_DIR),
            113: load_county_counts(113, DATA_DIR)
        }
        top_n = 10
        counties = get_top_counties(all_years, top_n=top_n)
        self.assertLessEqual(len(counties), top_n)

if __name__ == '__main__':
    unittest.main()
