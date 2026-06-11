"""Stage 3 tests for baseline and optimized sorting."""

import unittest

from benchmark import run_benchmark
from sorts import optimized_bubble_sort, optimized_quick_sort


class TestStage3Optimization(unittest.TestCase):
    def test_optimized_bubble_sort_matches_expected_order(self):
        cases = [
            [],
            [1],
            [3, 2, 1],
            [5, -2, 5, 0, 1],
            [1, 2, 3, 4],
        ]

        for sort_func in (optimized_bubble_sort, optimized_quick_sort):
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    original = data[:]
                    result = sort_func(data)
                    self.assertEqual(result, sorted(data))
                    self.assertEqual(data, original)
                    self.assertIsNot(result, data)

    def test_benchmark_includes_baseline_and_optimized_results(self):
        results = run_benchmark(sizes=(10,), repeats=1)

        self.assertIn("built_in_sorted", results)
        self.assertIn("optimized_bubble_sort", results)
        self.assertIn("optimized_quick_sort", results)
        self.assertIn("10", results["built_in_sorted"])
        self.assertIn("10", results["optimized_bubble_sort"])
        self.assertIn("10", results["optimized_quick_sort"])
        self.assertIsInstance(results["built_in_sorted"]["10"], float)
        self.assertIsInstance(results["optimized_bubble_sort"]["10"], float)
        self.assertIsInstance(results["optimized_quick_sort"]["10"], float)


if __name__ == "__main__":
    unittest.main()
