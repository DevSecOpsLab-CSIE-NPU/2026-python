import unittest
import os
from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results(self):
        results = load_results("results.json")
        self.assertIsInstance(results, dict)
        self.assertIn("500", results)
        self.assertIn("bubble", results["500"])
        self.assertIsInstance(results["500"]["bubble"], (int, float))

    def test_plot_results_creates_png(self):
        results = load_results("results.json")
        out_path = "assets/test_benchmark.png"
        os.makedirs("assets", exist_ok=True)
        plot_results(results, out_path)
        self.assertTrue(os.path.exists(out_path))
        self.assertGreater(os.path.getsize(out_path), 0)


if __name__ == "__main__":
    unittest.main()
