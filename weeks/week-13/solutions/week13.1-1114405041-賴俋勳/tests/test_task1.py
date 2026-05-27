import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from task1_grouped_bar import load_year, get_top_depts, DATA_DIR


class Task1Tests(unittest.TestCase):
    def test_load_year_returns_dict(self):
        result = load_year(114, DATA_DIR)
        self.assertIsInstance(result, dict)
        self.assertTrue(all(isinstance(k, str) for k in result.keys()))

    def test_load_year_counts_correct(self):
        result = load_year(114, DATA_DIR)
        self.assertIn("觀光休閒系", result)
        self.assertGreater(result["觀光休閒系"], 0)

    def test_load_year_total_positive(self):
        result = load_year(114, DATA_DIR)
        self.assertGreater(sum(result.values()), 0)

    def test_get_top_depts_length(self):
        year_data = {y: load_year(y, DATA_DIR) for y in [112, 113, 114]}
        result = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self):
        year_data = {y: load_year(y, DATA_DIR) for y in [112, 113, 114]}
        result = get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", result)


if __name__ == "__main__":
    unittest.main()
