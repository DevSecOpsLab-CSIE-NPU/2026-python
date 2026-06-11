import os
import unittest

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results_returns_dict(self):
        results = load_results("results.json")
        self.assertIsInstance(results, dict)
        self.assertTrue(results)

    def test_plot_generates_non_empty_png(self):
        out_path = os.path.join("assets", "benchmark.png")
        if os.path.exists(out_path):
            os.remove(out_path)

        results = load_results("results.json")
        plot_results(results, out_path)

        self.assertTrue(os.path.exists(out_path))
        self.assertGreater(os.path.getsize(out_path), 0)


if __name__ == "__main__":
    unittest.main()
