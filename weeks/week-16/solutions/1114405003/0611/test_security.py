import unittest
import tempfile
import os
import json
from benchmark import make_data, run_benchmark
from plot import load_results


class TestSecurity(unittest.TestCase):
    def test_make_data_rejects_negative(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_rejects_zero(self):
        with self.assertRaises(ValueError):
            make_data(0)

    def test_run_benchmark_rejects_invalid_sizes(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(500, -1000, 2000))

    def test_load_results_handles_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_results("nonexistent.json")

    def test_load_results_handles_invalid_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("not valid json")
            temp_path = f.name
        try:
            with self.assertRaises(json.JSONDecodeError):
                load_results(temp_path)
        finally:
            os.unlink(temp_path)


if __name__ == "__main__":
    unittest.main()
