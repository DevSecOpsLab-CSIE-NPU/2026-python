import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties, DATA_DIR


class Task2Tests(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_taitung(self):
        self.assertEqual(zip_to_county("950"), "台東縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        result = load_county_counts(114, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(114, DATA_DIR)
        self.assertIn("澎湖縣", result)
        self.assertGreater(result["澎湖縣"], 0)

    def test_get_top_counties_length(self):
        all_years = {y: load_county_counts(y, DATA_DIR) for y in [109, 110, 111, 112, 113, 114]}
        top = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top), 10)

    def test_get_top_counties_excludes_other(self):
        all_years = {y: load_county_counts(y, DATA_DIR) for y in [109, 110, 111, 112, 113, 114]}
        top = get_top_counties(all_years, top_n=10)
        self.assertNotIn("其他", top)


if __name__ == "__main__":
    unittest.main()
