import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task1_grouped_bar import load_year, get_top_depts


class TestTask1(unittest.TestCase):

    def test_load_year_returns_dict(self):
        result = load_year(112)
        self.assertIsInstance(result, dict)
        if result:
            key = list(result.keys())[0]
            self.assertIsInstance(key, str)

    def test_load_year_counts_correct(self):
        result = load_year(112)
        self.assertIn("觀光休閒系", result)
        self.assertGreater(result["觀光休閒系"], 0)

    def test_load_year_total_positive(self):
        result = load_year(112)
        total = sum(result.values())
        self.assertGreater(total, 0)

    def test_get_top_depts_length(self):
        year_data = {
            112: {"A": 10, "B": 8, "C": 6, "D": 4},
            113: {"A": 9, "E": 7, "F": 5},
        }
        result = get_top_depts(year_data, top_n=2)
        self.assertLessEqual(len(result), 4)

    def test_get_top_depts_includes_popular(self):
        year_data = {
            112: {"觀光休閒系": 61, "資訊工程系": 53, "食品科學系": 52},
            113: {"觀光休閒系": 60, "餐旅管理系": 46, "資訊工程系": 41},
        }
        result = get_top_depts(year_data, top_n=2)
        self.assertIn("觀光休閒系", result)


if __name__ == "__main__":
    unittest.main()
