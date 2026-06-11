"""Stage 4 red tests — 繪圖輸出測試

目標:
1. load_results 能正確讀取 results.json
2. plot_results 能輸出 PNG 且檔案非空

說明:
- 本檔為 red test。若 plot.py 尚未實作,測試應失敗。
"""

import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


class TestPlotStage4(unittest.TestCase):
    def test_load_results_returns_dict(self):
        """load_results 應能讀取 results.json 並回傳 dict。"""
        results_path = Path(__file__).with_name("results.json")
        data = load_results(str(results_path))
        self.assertIsInstance(data, dict)
        self.assertIn("timsort", data)

    def test_plot_results_creates_non_empty_png(self):
        """plot_results 應輸出 PNG 檔且檔案大小大於 0。"""
        results_path = Path(__file__).with_name("results.json")
        data = load_results(str(results_path))

        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "benchmark.png"
            plot_results(data, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)

    def test_load_results_keys_are_integers(self):
        """load_results 回傳的 dict，內層 key 必須是 int（而非 str）。"""
        results_path = Path(__file__).with_name("results.json")
        data = load_results(str(results_path))
        for algo, timings in data.items():
            for key in timings:
                with self.subTest(algo=algo, key=key):
                    self.assertIsInstance(key, int)

    def test_load_results_values_are_floats(self):
        """load_results 回傳的 dict，內層 value 必須是 float（秒數）。"""
        results_path = Path(__file__).with_name("results.json")
        data = load_results(str(results_path))
        for algo, timings in data.items():
            for n, t in timings.items():
                with self.subTest(algo=algo, n=n):
                    self.assertIsInstance(t, float)
                    self.assertGreater(t, 0)

    def test_plot_results_creates_parent_dir_if_missing(self):
        """plot_results 若輸出路徑的上層目錄不存在，應自動建立。"""
        results_path = Path(__file__).with_name("results.json")
        data = load_results(str(results_path))

        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "nested" / "deep" / "benchmark.png"
            plot_results(data, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
