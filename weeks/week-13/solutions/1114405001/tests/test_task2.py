from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from task2_zipcode_heatmap import (
    DATA_DIR,
    get_top_counties,
    load_county_counts,
    zip_to_county,
)


class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self) -> None:
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self) -> None:
        self.assertEqual(zip_to_county("000"), "其他")

    def test_load_county_counts_type(self) -> None:
        result = load_county_counts(114, DATA_DIR)
        self.assertIsInstance(result, dict)
        self.assertTrue(result)

    def test_load_county_counts_penghu_positive(self) -> None:
        result = load_county_counts(114, DATA_DIR)
        self.assertGreater(result.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self) -> None:
        all_years = {year: load_county_counts(year, DATA_DIR) for year in range(109, 115)}
        result = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(result), 10)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
