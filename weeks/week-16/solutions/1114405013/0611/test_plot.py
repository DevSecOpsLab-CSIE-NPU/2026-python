import os
import tempfile
import unittest

from plot import load_results, plot_results


class TestPlotResults(unittest.TestCase):
    def test_load_results_reads_json_file(self):
        results = load_results("results.json")

        self.assertIn("quick_sort", results)
        self.assertIn("4000", results["quick_sort"])

    def test_plot_results_creates_non_empty_png(self):
        results = load_results("results.json")

        with tempfile.TemporaryDirectory() as temp_dir:
            out_path = os.path.join(temp_dir, "benchmark.png")
            plot_results(results, out_path)

            self.assertTrue(os.path.exists(out_path))
            self.assertGreater(os.path.getsize(out_path), 0)


if __name__ == "__main__":
    unittest.main()
