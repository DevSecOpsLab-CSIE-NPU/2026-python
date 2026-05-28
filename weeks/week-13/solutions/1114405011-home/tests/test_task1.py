from __future__ import annotations

import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from task1_grouped_bar import get_top_depts, load_year, resolve_data_dir


class TestTask1(unittest.TestCase):
    def setUp(self) -> None:
        self.data_dir = resolve_data_dir()

    def test_load_year_returns_dict(self) -> None:
        data = load_year(114, self.data_dir)
        self.assertIsInstance(data, dict)
        self.assertTrue(all(isinstance(k, str) for k in data.keys()))

    def test_load_year_counts_correct(self) -> None:
        data = load_year(114, self.data_dir)
        self.assertEqual(data.get("資訊工程系"), 46)

    def test_load_year_total_positive(self) -> None:
        data = load_year(114, self.data_dir)
        self.assertGreater(sum(data.values()), 0)

    def test_get_top_depts_length(self) -> None:
        year_data = {
            112: load_year(112, self.data_dir),
            113: load_year(113, self.data_dir),
            114: load_year(114, self.data_dir),
        }
        top = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(top), 8)

    def test_get_top_depts_includes_popular(self) -> None:
        year_data = {
            112: load_year(112, self.data_dir),
            113: load_year(113, self.data_dir),
            114: load_year(114, self.data_dir),
        }
        top = get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", top)


if __name__ == "__main__":
    unittest.main()
