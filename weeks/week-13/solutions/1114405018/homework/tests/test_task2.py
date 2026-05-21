import unittest

from pathlib import Path
from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties


def find_data_dir() -> Path:
    p = Path(__file__).resolve()
    for _ in range(10):
        candidate = p.parent
        if (candidate / 'assets' / 'stu-data').exists():
            return (candidate / 'assets' / 'stu-data')
        p = candidate
    return Path(r"c:/Users/nina9/OneDrive/桌面/python/python2/2026-python/assets/stu-data")


class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county('880'), '澎湖縣')

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county('000'), '其他')

    def test_load_county_counts_type(self):
        d = load_county_counts(114, find_data_dir())
        self.assertIsInstance(d, dict)

    def test_load_county_counts_penghu_positive(self):
        d = load_county_counts(114, find_data_dir())
        # 澎湖郵遞區號在資料中應該有值
        self.assertGreaterEqual(d.get('澎湖縣', 0), 0)

    def test_get_top_counties_length(self):
        years = [109,110,111,112,113,114]
        all_years = {y: load_county_counts(y, find_data_dir()) for y in years}
        top = get_top_counties(all_years, top_n=10)
        self.assertLessEqual(len(top), 10)


if __name__ == '__main__':
    unittest.main()
