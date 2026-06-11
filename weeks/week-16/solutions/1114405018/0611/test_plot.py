"""Stage 4 — 繪圖輸出測試"""

import unittest
import json
import os
import tempfile

from plot import load_results, plot_results


SAMPLE_RESULTS = {
    "bubble_sort": {500: 0.12, 1000: 0.48},
    "quick_sort": {500: 0.002, 1000: 0.004},
    "sorted": {500: 0.0005, 1000: 0.001},
    "quick_sort_fast": {500: 0.001, 1000: 0.003},
}


class TestPlot(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.json_path = os.path.join(self.tmpdir.name, "results.json")
        self.out_dir = os.path.join(self.tmpdir.name, "assets")
        os.makedirs(self.out_dir, exist_ok=True)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_load_results_valid_json(self):
        with open(self.json_path, "w") as f:
            json.dump(SAMPLE_RESULTS, f)
        result = load_results(self.json_path)
        self.assertEqual(result, SAMPLE_RESULTS)

    def test_load_results_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_results(os.path.join(self.tmpdir.name, "nonexistent.json"))

    def test_plot_results_creates_png(self):
        out_path = os.path.join(self.out_dir, "benchmark.png")
        plot_results(SAMPLE_RESULTS, out_path)
        self.assertTrue(os.path.isfile(out_path))
        self.assertGreater(os.path.getsize(out_path), 0)

    def test_edge_case_empty_results(self):
        out_path = os.path.join(self.out_dir, "empty.png")
        plot_results({}, out_path)
        self.assertTrue(os.path.isfile(out_path))


if __name__ == "__main__":
    unittest.main()
