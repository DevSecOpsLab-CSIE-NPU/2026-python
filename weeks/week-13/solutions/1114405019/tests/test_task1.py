import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"


class TestTask1(unittest.TestCase):

    def setUp(self):
        from task1_grouped_bar import load_year, get_top_depts
        self.load_year = load_year
        self.get_top_depts = get_top_depts

    def test_load_year_returns_dict(self):
        data = self.load_year(114, DATA_DIR)
        self.assertIsInstance(data, dict)
        for key in data:
            self.assertIsInstance(key, str)

    def test_load_year_counts_correct(self):
        data = self.load_year(114, DATA_DIR)
        self.assertIn("觀光休閒系", data)
        self.assertEqual(data["觀光休閒系"], 58)

    def test_load_year_total_positive(self):
        data = self.load_year(112, DATA_DIR)
        total = sum(data.values())
        self.assertGreater(total, 0)

    def test_get_top_depts_length(self):
        year_data = {
            112: self.load_year(112, DATA_DIR),
            113: self.load_year(113, DATA_DIR),
            114: self.load_year(114, DATA_DIR),
        }
        top = self.get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(top), 8)

    def test_get_top_depts_includes_popular(self):
        year_data = {
            112: self.load_year(112, DATA_DIR),
            113: self.load_year(113, DATA_DIR),
            114: self.load_year(114, DATA_DIR),
        }
        top = self.get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", top)


if __name__ == "__main__":
    unittest.main()
