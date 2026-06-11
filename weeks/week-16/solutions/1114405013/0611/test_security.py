import os
import tempfile
import unittest

from benchmark import make_data, run_benchmark
from plot import load_results


class TestSecurityRules(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_run_benchmark_rejects_zero_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(1,), repeats=0)

    def test_load_results_rejects_non_json_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = os.path.join(temp_dir, "results.txt")
            with open(path, "w", encoding="utf-8") as file:
                file.write('{"quick_sort": {"1": 0.1}}')

            with self.assertRaises(ValueError):
                load_results(path)


if __name__ == "__main__":
    unittest.main()
