import tempfile
import unittest
from pathlib import Path

from benchmark import run_benchmark, save_results
from plot import create_plot


class TestPlot(unittest.TestCase):
    def test_create_plot_writes_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            results_path = tmp_path / "results.json"
            output_path = tmp_path / "assets" / "radar.png"
            save_results(run_benchmark(sizes=(10, 20), queries=4, repeat=1), results_path)

            result = create_plot(results_path, output_path)

            self.assertEqual(result, output_path)
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)
            self.assertEqual(output_path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")


if __name__ == "__main__":
    unittest.main()
