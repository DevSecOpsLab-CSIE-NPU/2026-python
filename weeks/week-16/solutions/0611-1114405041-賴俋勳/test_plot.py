import json
import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results_reads_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            payload = {
                "sizes": [10, 20],
                "algorithms": {
                    "bubble_sort": [0.2, 0.8],
                    "quick_sort": [0.05, 0.09],
                },
            }
            path.write_text(json.dumps(payload), encoding="utf-8")
            loaded = load_results(str(path))
            self.assertEqual(loaded, payload)

    def test_plot_results_creates_non_empty_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "benchmark.png"
            results = {
                "sizes": [10, 20, 40],
                "algorithms": {
                    "bubble_sort": [0.1, 0.4, 1.6],
                    "quick_sort": [0.02, 0.03, 0.05],
                    "sorted_builtin": [0.01, 0.02, 0.03],
                },
            }
            plot_results(results, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
