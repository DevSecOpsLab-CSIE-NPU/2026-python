from __future__ import annotations

import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from task2_zipcode_heatmap import (
    get_top_counties,
    load_county_counts,
    resolve_data_dir,
    zip_to_county,
)


class TestTask2(unittest.TestCase):
    def setUp(self) -> None:
        self.data_dir = resolve_data_dir()

    def test_zip_to_county_penghu(self) -> None:
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self) -> None:
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self) -> None:
        data = load_county_counts(114, self.data_dir)
        self.assertIsInstance(data, dict)

    def test_load_county_counts_penghu_positive(self) -> None:
        data = load_county_counts(114, self.data_dir)
        self.assertGreater(data.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self) -> None:
        all_years = {year: load_county_counts(year, self.data_dir) for year in [109, 110, 111, 112, 113, 114]}
        top = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top), 10)


if __name__ == "__main__":
    unittest.main()
