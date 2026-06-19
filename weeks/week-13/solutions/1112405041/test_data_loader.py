"""Stage 1: data_loader 測試"""
import unittest
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"


class TestLoadYear(unittest.TestCase):
    def test_load_year_returns_dict(self):
        from data_loader import load_year
        result = load_year(109, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_year_key_is_str(self):
        from data_loader import load_year
        result = load_year(109, DATA_DIR)
        for k in result:
            self.assertIsInstance(k, str)
            break

    def test_load_year_total_positive(self):
        from data_loader import load_year
        result = load_year(109, DATA_DIR)
        self.assertGreater(sum(result.values()), 0)

    def test_load_year_raises_on_invalid_year(self):
        from data_loader import load_year
        with self.assertRaises(ValueError):
            load_year(200, DATA_DIR)


class TestZipToCounty(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        from data_loader import zip_to_county
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        from data_loader import zip_to_county
        self.assertEqual(zip_to_county("999"), "其他")

    def test_zip_to_county_short_string(self):
        from data_loader import zip_to_county
        self.assertEqual(zip_to_county(""), "其他")


class TestLoadCountyCounts(unittest.TestCase):
    def test_load_county_counts_type(self):
        from data_loader import load_county_counts
        result = load_county_counts(109, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        from data_loader import load_county_counts
        result = load_county_counts(109, DATA_DIR)
        penghu = result.get("澎湖縣", 0)
        self.assertGreater(penghu, 0)


if __name__ == "__main__":
    unittest.main()
