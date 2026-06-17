from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from task1_grouped_bar import get_top_depts, load_year


DATA_DIR = Path(__file__).resolve().parents[5] / "assets" / "stu-data"


class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self):
        result = load_year(112, DATA_DIR)
        self.assertIsInstance(result, dict)
        self.assertTrue(all(isinstance(key, str) for key in result))

    def test_load_year_counts_correct(self):
        result = load_year(112, DATA_DIR)
        self.assertEqual(result["資訊工程系"], 53)

    def test_load_year_total_positive(self):
        result = load_year(114, DATA_DIR)
        self.assertGreater(sum(result.values()), 0)

    def test_get_top_depts_length(self):
        year_data = {
            112: load_year(112, DATA_DIR),
            113: load_year(113, DATA_DIR),
            114: load_year(114, DATA_DIR),
        }
        result = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self):
        year_data = {
            112: load_year(112, DATA_DIR),
            113: load_year(113, DATA_DIR),
            114: load_year(114, DATA_DIR),
        }
        result = get_top_depts(year_data, top_n=8)
        self.assertIn("觀光休閒系", result)
        self.assertIn("資訊工程系", result)


if __name__ == "__main__":
    unittest.main()