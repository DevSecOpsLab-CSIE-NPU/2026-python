from pathlib import Path
import sys
import unittest


ROOT = next(
    parent
    for parent in Path(__file__).resolve().parents
    if (parent / "assets" / "stu-data").exists()
)
SOLUTION_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOLUTION_DIR))

import task1_grouped_bar as task1  # noqa: E402


def load_year_data(year: int) -> dict[str, int]:
    return task1.load_year(year, ROOT / "assets" / "stu-data")


class Task1Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.years = {year: load_year_data(year) for year in (112, 113, 114)}

    def test_load_year_returns_dict(self) -> None:
        data = load_year_data(114)

        self.assertIsInstance(data, dict)
        self.assertTrue(data)
        self.assertTrue(all(isinstance(key, str) for key in data))

    def test_load_year_counts_correct(self) -> None:
        data = load_year_data(114)

        self.assertEqual(data["觀光休閒系"], 58)

    def test_load_year_total_positive(self) -> None:
        data = load_year_data(113)

        self.assertGreater(sum(data.values()), 0)

    def test_get_top_depts_length(self) -> None:
        result = task1.get_top_depts(self.years, top_n=8)

        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self) -> None:
        result = task1.get_top_depts(self.years, top_n=8)

        self.assertIn("觀光休閒系", result)
        self.assertIn("資訊工程系", result)


if __name__ == "__main__":
    unittest.main()