import inspect
import unittest

import benchmark
import plot
from benchmark import make_data, run_benchmark


class TestSecurityPractices(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_run_benchmark_rejects_non_positive_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(1,), repeats=0)

    def test_json_is_used_instead_of_pickle(self):
        source = inspect.getsource(plot) + inspect.getsource(benchmark)
        self.assertIn("json.load", source)
        self.assertIn("json.dump", source)
        self.assertNotIn("pickle", source)


if __name__ == "__main__":
    unittest.main()
