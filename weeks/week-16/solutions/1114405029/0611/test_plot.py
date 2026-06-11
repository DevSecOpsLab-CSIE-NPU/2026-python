"""Stage 4 tests for benchmark result plotting."""

import json
import os
import tempfile
import unittest

from plot import load_results, plot_results


class TestPlotResults(unittest.TestCase):
    def test_load_results_reads_json_file(self):
        sample = {
            "quick_sort": {
                "10": 0.001,
                "20": 0.002,
            }
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "results.json")
            with open(path, "w", encoding="utf-8") as file:
                json.dump(sample, file)

            self.assertEqual(load_results(path), sample)

    def test_plot_results_creates_non_empty_png(self):
        sample = {
            "quick_sort": {
                "10": 0.001,
                "20": 0.002,
            },
            "merge_sort": {
                "10": 0.0015,
                "20": 0.003,
            },
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, "benchmark.png")
            plot_results(sample, out_path)

            self.assertTrue(os.path.exists(out_path))
            self.assertGreater(os.path.getsize(out_path), 0)


if __name__ == "__main__":
    unittest.main()
