import os
import unittest
from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def test_load_results_returns_dict(self):
        data = load_results("results.json")
        self.assertIsInstance(data, dict)
        self.assertIn("quick", data)

    def test_plot_output_exists_and_nonempty(self):
        out_path = "assets/benchmark.png"
        if os.path.exists(out_path):
            os.remove(out_path)
        data = load_results("results.json")
        plot_results(data, out_path)
        self.assertTrue(os.path.exists(out_path))
        self.assertGreater(os.path.getsize(out_path), 0)

    def test_load_results_invalid_path_raises(self):
        with self.assertRaises(FileNotFoundError):
            load_results("nonexistent.json")
