"""Stage 5 security self-scan tests."""

import json
import os
import tempfile
import unittest

from benchmark import make_data, run_benchmark
from plot import load_results


class TestSecuritySelfScan(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_run_benchmark_rejects_non_positive_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), repeats=0)

    def test_load_results_rejects_non_mapping_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "results.json")
            with open(path, "w", encoding="utf-8") as file:
                json.dump(["not", "a", "mapping"], file)

            with self.assertRaises(ValueError):
                load_results(path)


if __name__ == "__main__":
    unittest.main()
