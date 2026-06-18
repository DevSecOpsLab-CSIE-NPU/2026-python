"""Stage 4 - plot tests."""

import json
import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


class TestPlotFunctions(unittest.TestCase):
    def test_load_results_reads_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            results_file = temp_path / "results.json"
            sample_results = {"rows": [{"n": 10, "linear_search_seconds": 0.1}]}
            results_file.write_text(json.dumps(sample_results), encoding="utf-8")

            loaded = load_results(str(results_file))

        self.assertEqual(loaded, sample_results)

    def test_plot_results_creates_non_empty_png(self):
        sample_results = {
            "rows": [
                {
                    "n": 10,
                    "linear_search_seconds": 0.1,
                    "builtin_in_seconds": 0.05,
                    "binary_search_seconds": 0.02,
                    "bisect_left_seconds": 0.01,
                    "set_search_seconds": 0.03,
                    "set_contains_seconds": 0.005,
                    "binary_with_sort_seconds": 0.025,
                    "bisect_with_sort_seconds": 0.015,
                    "set_with_build_seconds": 0.008,
                }
            ]
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            out_path = temp_path / "radar.png"

            plot_results(sample_results, str(out_path))

            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()