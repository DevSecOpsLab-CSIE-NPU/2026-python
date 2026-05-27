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

import task2_zipcode_heatmap as task2  # noqa: E402


def load_county_data(year: int) -> dict[str, int]:
    return task2.load_county_counts(year, ROOT / "assets" / "stu-data")


class Task2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.years = {year: load_county_data(year) for year in range(109, 115)}

    def test_zip_to_county_penghu(self) -> None:
        self.assertEqual(task2.zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self) -> None:
        self.assertEqual(task2.zip_to_county("999"), "其他")

    def test_load_county_counts_type(self) -> None:
        data = load_county_data(114)

        self.assertIsInstance(data, dict)
        self.assertTrue(all(isinstance(key, str) for key in data))

    def test_load_county_counts_penghu_positive(self) -> None:
        data = load_county_data(114)

        self.assertGreater(data["澎湖縣"], 0)

    def test_get_top_counties_length(self) -> None:
        result = task2.get_top_counties(self.years, top_n=10)

        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()