from __future__ import annotations

import unittest

from task1_grouped_bar import DATA_DIR, get_top_depts, load_year


class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self) -> None:
        data = load_year(112, DATA_DIR)
        self.assertIsInstance(data, dict)
        self.assertTrue(all(isinstance(key, str) for key in data))

    def test_load_year_counts_correct(self) -> None:
        data = load_year(112, DATA_DIR)
        self.assertEqual(data["觀光休閒系"], 61)

    def test_load_year_total_positive(self) -> None:
        data = load_year(113, DATA_DIR)
        self.assertGreater(sum(data.values()), 0)

    def test_get_top_depts_length(self) -> None:
        year_data = {year: load_year(year, DATA_DIR) for year in [112, 113, 114]}
        result = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self) -> None:
        year_data = {year: load_year(year, DATA_DIR) for year in [112, 113, 114]}
        result = get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", result)
        self.assertIn("資訊工程系", result)


if __name__ == "__main__":
    unittest.main()