"""Stage 4 — 繪圖輸出測試"""
import json
import os
import shutil
import tempfile
import unittest

from plot import load_results, plot_results


class TestLoadResults(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_load_valid_json(self):
        sample = {"algo": {"500": 0.1, "1000": 0.4}}
        path = os.path.join(self.tmp, "r.json")
        with open(path, "w") as f:
            json.dump(sample, f)
        self.assertEqual(load_results(path), sample)

    def test_load_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_results(os.path.join(self.tmp, "nope.json"))

    def test_load_raises_on_invalid_json(self):
        path = os.path.join(self.tmp, "bad.json")
        with open(path, "w") as f:
            f.write("{{not json}}")
        with self.assertRaises(json.JSONDecodeError):
            load_results(path)


class TestPlotResults(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.sample = {
            "algo_a": {"500": 0.1, "1000": 0.4, "2000": 1.6},
            "algo_b": {"500": 0.05, "1000": 0.2, "2000": 0.8},
        }

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_png_is_created(self):
        out = os.path.join(self.tmp, "out.png")
        plot_results(self.sample, out)
        self.assertTrue(os.path.exists(out))

    def test_png_is_not_empty(self):
        out = os.path.join(self.tmp, "out.png")
        plot_results(self.sample, out)
        self.assertGreater(os.path.getsize(out), 100)

    def test_output_dir_created_automatically(self):
        out = os.path.join(self.tmp, "subdir", "chart.png")
        plot_results(self.sample, out)
        self.assertTrue(os.path.exists(out))


if __name__ == "__main__":
    unittest.main()
