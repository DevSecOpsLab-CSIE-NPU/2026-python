from __future__ import annotations

import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from task2_zipcode_heatmap import DATA_DIR, get_top_counties, load_county_counts, zip_to_county


class Task2Tests(unittest.TestCase):
    def test_zip_to_county_penghu(self) -> None:
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self) -> None:
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self) -> None:
        counts = load_county_counts(114, DATA_DIR)
        self.assertIsInstance(counts, dict)

    def test_load_county_counts_penghu_positive(self) -> None:
        counts = load_county_counts(114, DATA_DIR)
        self.assertGreater(counts.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self) -> None:
        all_years = {year: load_county_counts(year, DATA_DIR) for year in (109, 110, 111, 112, 113, 114)}
        top_counties = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top_counties), 10)


if __name__ == "__main__":
    unittest.main()