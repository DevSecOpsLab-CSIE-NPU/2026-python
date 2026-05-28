from __future__ import annotations

import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from task1_grouped_bar import DATA_DIR, get_top_depts, load_year


class Task1Tests(unittest.TestCase):
    def test_load_year_returns_dict(self) -> None:
        counts = load_year(114, DATA_DIR)
        self.assertIsInstance(counts, dict)
        self.assertTrue(all(isinstance(key, str) for key in counts))

    def test_load_year_counts_correct(self) -> None:
        counts = load_year(114, DATA_DIR)
        self.assertEqual(counts["觀光休閒系"], 58)

    def test_load_year_total_positive(self) -> None:
        counts = load_year(113, DATA_DIR)
        self.assertGreater(sum(counts.values()), 0)

    def test_get_top_depts_length(self) -> None:
        year_data = {year: load_year(year, DATA_DIR) for year in (112, 113, 114)}
        top_departments = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(top_departments), 8)

    def test_get_top_depts_includes_popular(self) -> None:
        year_data = {year: load_year(year, DATA_DIR) for year in (112, 113, 114)}
        top_departments = get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", top_departments)
        self.assertIn("資訊工程系", top_departments)


if __name__ == "__main__":
    unittest.main()