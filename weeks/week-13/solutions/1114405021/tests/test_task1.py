import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from task1_grouped_bar import get_top_depts, load_year


class Task1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        base = Path(__file__).resolve()
        candidates = [
            base.parent.parent.parent.parent.parent / "assets" / "stu-data",
            base.parent.parent.parent.parent.parent.parent / "assets" / "stu-data",
        ]
        cls.data_dir = next((p for p in candidates if p.exists()), candidates[0])

    def test_load_year_returns_dict(self) -> None:
        result = load_year(112, self.data_dir)
        self.assertIsInstance(result, dict)
        self.assertTrue(all(isinstance(k, str) for k in result.keys()))

    def test_load_year_counts_correct(self) -> None:
        result = load_year(112, self.data_dir)
        self.assertEqual(result.get("資訊工程系"), 53)

    def test_load_year_total_positive(self) -> None:
        result = load_year(114, self.data_dir)
        self.assertGreater(sum(result.values()), 0)

    def test_get_top_depts_length(self) -> None:
        year_data = {
            112: load_year(112, self.data_dir),
            113: load_year(113, self.data_dir),
            114: load_year(114, self.data_dir),
        }
        top = get_top_depts(year_data, top_n=8)
        self.assertLessEqual(len(top), 24)

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
