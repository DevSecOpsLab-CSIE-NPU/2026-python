from __future__ import annotations

import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from task1_grouped_bar import DATA_DIR, get_top_depts, load_year


class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self) -> None:
        result = load_year(114, DATA_DIR)
        self.assertIsInstance(result, dict)
        self.assertTrue(result)
        self.assertTrue(all(isinstance(k, str) for k in result.keys()))

    def test_load_year_counts_correct(self) -> None:
        result = load_year(114, DATA_DIR)
        sample_dept = next(iter(result.keys()))

        csv_path = DATA_DIR / "114年新生資料庫.csv"
        with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))

        expected = sum(1 for row in rows if (row.get("系所名稱") or "").strip() == sample_dept)
        self.assertEqual(result[sample_dept], expected)

    def test_load_year_total_positive(self) -> None:
        result = load_year(114, DATA_DIR)
        self.assertGreater(sum(result.values()), 0)

    def test_get_top_depts_length(self) -> None:
        years = {112: load_year(112, DATA_DIR), 113: load_year(113, DATA_DIR), 114: load_year(114, DATA_DIR)}
        result = get_top_depts(years, top_n=8)
        self.assertLessEqual(len(result), 24)
        self.assertGreater(len(result), 0)

    def test_get_top_depts_includes_popular(self) -> None:
        years = {112: load_year(112, DATA_DIR), 113: load_year(113, DATA_DIR), 114: load_year(114, DATA_DIR)}
        top = get_top_depts(years, top_n=8)

        yearly_top1 = []
        for data in years.values():
            dept, _ = sorted(data.items(), key=lambda item: (-item[1], item[0]))[0]
            yearly_top1.append(dept)

        self.assertTrue(any(dept in top for dept in yearly_top1))


if __name__ == "__main__":
    unittest.main()
