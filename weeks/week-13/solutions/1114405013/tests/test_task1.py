from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import task1_grouped_bar as task1


class TestTask1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = task1.resolve_data_dir(task1.DATA_DIR)

    def test_load_year_returns_dict(self):
        data = task1.load_year(114, self.data_dir)
        self.assertIsInstance(data, dict)
        self.assertTrue(all(isinstance(key, str) for key in data.keys()))

    def test_load_year_counts_correct(self):
        data = task1.load_year(114, self.data_dir)
        dept = "資訊工程系"
        if dept not in data:
            dept = max(data, key=data.get)
        manual_count = sum(
            1 for row in task1.iter_rows_for_year(114, self.data_dir)
            if (task1.get_column(row, task1.DEPT_COLUMN_CANDIDATES) or "").strip() == dept
        )
        self.assertEqual(data[dept], manual_count)

    def test_load_year_total_positive(self):
        data = task1.load_year(114, self.data_dir)
        self.assertGreater(sum(data.values()), 0)

    def test_get_top_depts_length(self):
        year_data = {year: task1.load_year(year, self.data_dir) for year in (112, 113, 114)}
        result = task1.get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self):
        year_data = {year: task1.load_year(year, self.data_dir) for year in (112, 113, 114)}
        result = task1.get_top_depts(year_data, top_n=8)
        most_popular_114 = max(year_data[114], key=year_data[114].get)
        self.assertIn(most_popular_114, result)


if __name__ == "__main__":
    unittest.main()
