import unittest

from benchmark import make_data, run_benchmark


class TestBenchmark(unittest.TestCase):
    def test_make_data_reproducible(self):
        self.assertEqual(make_data(8, seed=7), make_data(8, seed=7))

    def test_run_benchmark_shape(self):
        result = run_benchmark(sizes=(10, 20), repeats=2)
        self.assertEqual(result["sizes"], [10, 20])
        self.assertIn("bubble_sort", result["algorithms"])
        self.assertIn("quick_sort", result["algorithms"])
        self.assertIn("merge_sort", result["algorithms"])


if __name__ == "__main__":
    unittest.main()
