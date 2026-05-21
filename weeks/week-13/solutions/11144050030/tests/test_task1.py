import unittest
from pathlib import Path
from task1_grouped_bar import load_year, get_top_depts

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"


class TestTask1(unittest.TestCase):

    def test_load_year_returns_dict(self):
        result = load_year(112, DATA_DIR)
        self.assertIsInstance(result, dict)
        if result:
            key = list(result.keys())[0]
            self.assertIsInstance(key, str)

    def test_load_year_counts_correct(self):
        result = load_year(112, DATA_DIR)
        self.assertEqual(result.get("觀光休閒系", 0), 61)

    def test_load_year_total_positive(self):
        result = load_year(112, DATA_DIR)
        total = sum(result.values())
        self.assertGreater(total, 0)

    def test_get_top_depts_length(self):
        year_data = {112: load_year(112, DATA_DIR)}
        depts = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(depts), 8)

    def test_get_top_depts_includes_popular(self):
        year_data = {112: load_year(112, DATA_DIR)}
        depts = get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", depts)


if __name__ == "__main__":
    unittest.main()
