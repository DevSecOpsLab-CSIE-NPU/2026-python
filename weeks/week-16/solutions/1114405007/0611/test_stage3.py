import unittest

from benchmark import run_benchmark
from sorts import quick_sort_fast


class TestStage3Acceleration(unittest.TestCase):
    def test_quick_sort_fast_correctness(self):
        data = [9, 1, 5, 3, 9, 2, 0, -1]
        self.assertEqual(quick_sort_fast(data), sorted(data))

    def test_quick_sort_fast_input_not_mutated(self):
        data = [4, 1, 3, 1]
        snapshot = data.copy()
        result = quick_sort_fast(data)
        self.assertEqual(data, snapshot)
        self.assertIsNot(result, data)

    def test_quick_sort_fast_edge_case_empty(self):
        self.assertEqual(quick_sort_fast([]), [])

    def test_benchmark_contains_baseline_and_fast(self):
        report = run_benchmark(sizes=(50, 100), repeats=1)
        names = set(report["results"].keys())
        self.assertIn("builtin_sorted", names)
        self.assertIn("quick_sort_fast", names)


if __name__ == "__main__":
    unittest.main()
