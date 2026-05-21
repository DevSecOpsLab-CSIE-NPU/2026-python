import unittest
from pathlib import Path
from task1_grouped_bar import load_year, get_top_depts


def find_data_dir() -> Path:
    p = Path(__file__).resolve()
    for _ in range(10):
        candidate = p.parent
        if (candidate / 'assets' / 'stu-data').exists():
            return (candidate / 'assets' / 'stu-data')
        p = candidate
    return Path(r"c:/Users/nina9/OneDrive/桌面/python/python2/2026-python/assets/stu-data")


class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self):
        d = load_year(114, find_data_dir())
        self.assertIsInstance(d, dict)

    def test_load_year_total_positive(self):
        d = load_year(114, find_data_dir())
        self.assertGreater(sum(d.values()), 0)

    def test_get_top_depts_length(self):
        years = [112,113,114]
        all_years = {y: load_year(y, find_data_dir()) for y in years}
        top = get_top_depts(all_years, top_n=8)
        self.assertLessEqual(len(top), 8*3)

    def test_get_top_depts_includes_popular(self):
        years = [114]
        all_years = {y: load_year(y, find_data_dir()) for y in years}
        # pick top dept of year 114
        d = all_years[114]
        top1 = sorted(d.items(), key=lambda kv: kv[1], reverse=True)[0][0]
        top = get_top_depts(all_years, top_n=8)
        self.assertIn(top1, top)


if __name__ == '__main__':
    unittest.main()
