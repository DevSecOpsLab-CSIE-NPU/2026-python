"""Stage 5 - security tests."""

import json
import tempfile
import unittest
from pathlib import Path

from benchmark import make_queries, run_benchmark
from plot import load_results, plot_results


class TestSecurityRules(unittest.TestCase):
    def test_make_queries_rejects_negative_count(self):
        with self.assertRaises(ValueError):
            make_queries(10, -1)

    def test_load_results_rejects_non_mapping_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            results_file = temp_path / "results.json"
            results_file.write_text(json.dumps([1, 2, 3]), encoding="utf-8")

            with self.assertRaises(ValueError):
                load_results(str(results_file))

    def test_plot_results_rejects_missing_measurements(self):
        incomplete_results = {
            "rows": [
                {
                    "n": 10,
                    "linear_search_seconds": 0.1,
                    "builtin_in_seconds": 0.05,
                    "binary_search_seconds": 0.02,
                    "bisect_left_seconds": 0.01,
                    "set_search_seconds": 0.03,
                    "set_contains_seconds": 0.005,
                }
            ]
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            out_path = temp_path / "radar.png"

            with self.assertRaises(ValueError):
                plot_results(incomplete_results, str(out_path))

    def test_run_benchmark_rejects_negative_queries(self):
        with self.assertRaises(ValueError):
            run_benchmark(queries=-1)


if __name__ == "__main__":
    unittest.main()