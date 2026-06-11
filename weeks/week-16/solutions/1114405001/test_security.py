import json
import os
import tempfile
import unittest

from benchmark import make_data, run_benchmark
from plot import load_results


class TestSecurityRules(unittest.TestCase):
    def test_make_data_rejects_bool_n(self):
        with self.assertRaises(TypeError):
            make_data(True)

    def test_run_benchmark_rejects_non_positive_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), repeats=0)

    def test_load_results_rejects_non_json_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            pkl_path = os.path.join(tmp, "results.pkl")
            with open(pkl_path, "w", encoding="utf-8") as f:
                json.dump({"k": 1}, f)
            with self.assertRaises(ValueError):
                load_results(pkl_path)

    def test_load_results_rejects_non_dict_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            json_path = os.path.join(tmp, "bad_results.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump([1, 2, 3], f)
            with self.assertRaises(ValueError):
                load_results(json_path)


if __name__ == "__main__":
    unittest.main()
