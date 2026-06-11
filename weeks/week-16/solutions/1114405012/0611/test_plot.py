import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_plot_creates_non_empty_png(self):
        with TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            results_path = temp_path / "results.json"
            output_path = temp_path / "benchmark.png"
            results_path.write_text(
                '{"500": {"bubble_sort": 1.0, "quick_sort": 0.2, "merge_sort": 0.15, "sorted": 0.01}}',
                encoding="utf-8",
            )
            results = load_results(str(results_path))
            plot_results(results, str(output_path))
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
