import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from task2_zipcode_heatmap import get_top_counties, load_county_counts, zip_to_county


class Task2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        base = Path(__file__).resolve()
        candidates = [
            base.parent.parent.parent.parent.parent / "assets" / "stu-data",
            base.parent.parent.parent.parent.parent.parent / "assets" / "stu-data",
        ]
        cls.data_dir = next((p for p in candidates if p.exists()), candidates[0])

    def test_zip_to_county_penghu(self) -> None:
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self) -> None:
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self) -> None:
        result = load_county_counts(109, self.data_dir)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self) -> None:
        result = load_county_counts(114, self.data_dir)
        self.assertGreater(result.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self) -> None:
        all_years = {year: load_county_counts(year, self.data_dir) for year in range(109, 115)}
        top = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top), 10)


if __name__ == "__main__":
    unittest.main()
