import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results_returns_dict(self):
        results = load_results("results.json")

        self.assertIsInstance(results, dict)
        self.assertIn("500", results)
        self.assertIn("bubble_sort", results["500"])

    def test_plot_results_creates_non_empty_png(self):
        results = load_results("results.json")

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"
            plot_results(results, str(output_path))

            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()