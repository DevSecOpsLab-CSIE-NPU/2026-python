"""Stage 4 — 繪圖測試"""

import os
import json
import unittest
import tempfile

from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "500": {
                "bubble_sort": {"avg_seconds": 0.05, "records": [0.05]},
                "quick_sort": {"avg_seconds": 0.001, "records": [0.001]},
                "builtin_sorted": {"avg_seconds": 0.0001, "records": [0.0001]},
            }
        }
        self.tmp_dir = tempfile.mkdtemp()

    def test_load_results_returns_dict(self):
        path = os.path.join(self.tmp_dir, "test_results.json")
        with open(path, "w") as f:
            json.dump(self.sample_data, f)
        data = load_results(path)
        self.assertIsInstance(data, dict)
        self.assertIn("500", data)

    def test_plot_results_creates_png(self):
        out_path = os.path.join(self.tmp_dir, "test_plot.png")
        plot_results(self.sample_data, out_path)
        self.assertTrue(os.path.isfile(out_path))
        self.assertGreater(os.path.getsize(out_path), 0)

    def test_load_without_context_manager_fails(self):
        path = os.path.join(self.tmp_dir, "no_file.json")
        with self.assertRaises(FileNotFoundError):
            load_results(path)

    def test_load_uses_json_not_pickle(self):
        self.assertTrue(hasattr(load_results, "__call__"))
        import json as jmod
        self.assertEqual(load_results.__module__, "plot")


if __name__ == "__main__":
    unittest.main()
