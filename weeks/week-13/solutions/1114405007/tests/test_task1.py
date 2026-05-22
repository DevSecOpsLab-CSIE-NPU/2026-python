from __future__ import annotations

import csv
import unittest
from collections import Counter
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from task1_grouped_bar import DATA_DIR, get_top_depts, load_year


class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self) -> None:
        data = load_year(114, DATA_DIR)
        self.assertIsInstance(data, dict)
        self.assertTrue(all(isinstance(k, str) for k in data.keys()))

    def test_load_year_counts_correct(self) -> None:
        year = 114
        csv_path = DATA_DIR / f"{year}年新生資料庫.csv"
        with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))

        expected = Counter((r.get("系所名稱") or "").strip() for r in rows if (r.get("系所名稱") or "").strip())
        result = load_year(year, DATA_DIR)

        self.assertEqual(result.get("資訊工程系", 0), expected.get("資訊工程系", 0))

    def test_load_year_total_positive(self) -> None:
        data = load_year(114, DATA_DIR)
        self.assertGreater(sum(data.values()), 0)

    def test_get_top_depts_length(self) -> None:
        year_data = {year: load_year(year, DATA_DIR) for year in (112, 113, 114)}
        top = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(top), 24)

    def test_get_top_depts_includes_popular(self) -> None:
        year_data = {year: load_year(year, DATA_DIR) for year in (112, 113, 114)}
        popular = max(year_data[114].items(), key=lambda item: item[1])[0]
        top = get_top_depts(year_data, top_n=8)
        self.assertIn(popular, top)


if __name__ == "__main__":
    unittest.main()
