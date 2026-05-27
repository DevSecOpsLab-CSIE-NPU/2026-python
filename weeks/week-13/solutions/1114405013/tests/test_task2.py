from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import task2_zipcode_heatmap as task2


class TestTask2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = task2.resolve_data_dir(task2.DATA_DIR)

    def test_zip_to_county_penghu(self):
        self.assertEqual(task2.zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(task2.zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        data = task2.load_county_counts(114, self.data_dir)
        self.assertIsInstance(data, dict)

    def test_load_county_counts_penghu_positive(self):
        data = task2.load_county_counts(114, self.data_dir)
        self.assertGreater(data.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self):
        all_years = {year: task2.load_county_counts(year, self.data_dir) for year in (109, 110, 111, 112, 113, 114)}
        result = task2.get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()
