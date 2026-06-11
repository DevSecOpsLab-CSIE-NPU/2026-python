import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results_reads_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            path.write_text('{"demo": {"runs": []}}', encoding="utf-8")
            self.assertEqual(load_results(str(path)), {"demo": {"runs": []}})

    def test_plot_results_writes_png(self):
        results = {
            "demo_sort": {
                "runs": [
                    {"n": 10, "average": 0.001, "records": [0.001]},
                    {"n": 20, "average": 0.002, "records": [0.002]},
                ]
            }
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "chart.png"
            plot_results(results, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
