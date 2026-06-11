"""Stage 4 — 繪圖功能測試

plot.py 必須:
  1. 讀 results.json 畫折線圖(y 軸 log scale)
  2. 輸出 assets/benchmark.png
  3. matplotlib.use("Agg") 開頭
"""

import os
import unittest

from plot import generate_plot


class TestPlotOutput(unittest.TestCase):
    def test_png_file_created(self):
        if os.path.isfile("assets/benchmark.png"):
            os.remove("assets/benchmark.png")
        generate_plot("results.json", "assets/benchmark.png")
        self.assertTrue(os.path.isfile("assets/benchmark.png"))

    def test_png_not_empty(self):
        generate_plot("results.json", "assets/benchmark.png")
        size = os.path.getsize("assets/benchmark.png")
        self.assertGreater(size, 0)

    def test_missing_json_raises(self):
        with self.assertRaises(FileNotFoundError):
            generate_plot("nonexistent.json", "assets/benchmark.png")


if __name__ == "__main__":
    unittest.main()
