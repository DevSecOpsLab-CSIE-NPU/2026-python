"""Stage 3: 圖表繪製測試"""
import unittest
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).resolve().parent


class TestPlotGroupedBar(unittest.TestCase):
    def test_task1_png_created(self):
        from data_loader import load_year
        from analysis import get_top_depts
        from plot import plot_grouped_bar

        years = [112, 113, 114]
        year_data = {y: load_year(y, DATA_DIR) for y in years}
        top_depts = get_top_depts(year_data, top_n=8)

        out_path = OUTPUT_DIR / "task1.png"
        plot_grouped_bar(year_data, top_depts, str(out_path))

        self.assertTrue(out_path.exists())
        self.assertGreater(out_path.stat().st_size, 0)

    def test_task1_top_depts_empty(self):
        from plot import plot_grouped_bar

        out_path = OUTPUT_DIR / "task1_empty.png"
        plot_grouped_bar({}, [], str(out_path))

        self.assertTrue(out_path.exists())


class TestPlotHeatmap(unittest.TestCase):
    def test_task2_png_created(self):
        from data_loader import load_county_counts
        from analysis import get_top_counties
        from plot import plot_heatmap

        years = list(range(109, 115))
        county_data = {y: load_county_counts(y, DATA_DIR) for y in years}
        top_counties = get_top_counties(county_data, top_n=10)

        out_path = OUTPUT_DIR / "task2.png"
        plot_heatmap(county_data, top_counties, str(out_path))

        self.assertTrue(out_path.exists())
        self.assertGreater(out_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
