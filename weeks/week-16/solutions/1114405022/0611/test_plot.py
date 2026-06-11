"""Stage 4 — 繪圖測試"""

import os
import unittest

try:
    from plot import plot_results
    HAS_PLOT = True
except (ImportError, ModuleNotFoundError):
    HAS_PLOT = False
    plot_results = None


class TestPlot(unittest.TestCase):
    def test_plot_creates_png(self):
        if not HAS_PLOT:
            self.fail("plot module not available")
        plot_results()
        self.assertTrue(os.path.exists("assets/benchmark.png"))

    def test_png_not_empty(self):
        if not HAS_PLOT:
            self.fail("plot module not available")
        path = "assets/benchmark.png"
        self.assertTrue(os.path.exists(path))
        self.assertGreater(os.path.getsize(path), 0)

    def test_plot_missing_file_raises(self):
        if not HAS_PLOT:
            self.fail("plot module not available")
        with self.assertRaises(FileNotFoundError):
            plot_results(data_path="nonexistent.json")


if __name__ == "__main__":
    unittest.main()
