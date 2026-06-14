from __future__ import annotations

import unittest

from task2_zipcode_heatmap import DATA_DIR, get_top_counties, load_county_counts, zip_to_county


class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self) -> None:
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self) -> None:
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self) -> None:
        data = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(data, dict)

    def test_load_county_counts_penghu_positive(self) -> None:
        data = load_county_counts(112, DATA_DIR)
        self.assertGreater(data.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self) -> None:
        all_years = {year: load_county_counts(year, DATA_DIR) for year in [109, 110, 111, 112, 113, 114]}
        result = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()