import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results_reads_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "results.json"
            source.write_text(
                '{"sizes": [1], "repeats": 1, "results": {"sorted": {"1": 0.001}}}',
                encoding="utf-8",
            )

            results = load_results(str(source))
            self.assertEqual(results["sizes"], [1])
            self.assertEqual(results["results"]["sorted"]["1"], 0.001)

    def test_plot_results_writes_png(self):
        results = {
            "sizes": [10, 20],
            "repeats": 2,
            "results": {
                "sorted": {"10": 0.001, "20": 0.002},
                "quick_sort": {"10": 0.01, "20": 0.02},
            },
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            out_path = Path(temp_dir) / "benchmark.png"
            plot_results(results, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()