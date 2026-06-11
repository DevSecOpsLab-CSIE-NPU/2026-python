import unittest

from stage3 import benchmark


class TestBenchmark(unittest.TestCase):
    def test_make_data_reproducible_and_empty(self):
        zero_data = benchmark.make_data(0, seed=42)
        self.assertEqual(zero_data, [])

        first = benchmark.make_data(5, seed=42)
        second = benchmark.make_data(5, seed=42)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 5)
        self.assertNotEqual(first, benchmark.make_data(5, seed=43))

    def test_run_benchmark_result_structure(self):
        results = benchmark.run_benchmark(sizes=(5, 10), repeats=1)
        self.assertIsInstance(results, dict)

        for algorithm in ('bubble_sort', 'quick_sort', 'merge_sort', 'sorted'):
            with self.subTest(algorithm=algorithm):
                self.assertIn(algorithm, results)
                self.assertIsInstance(results[algorithm], dict)
                self.assertEqual(sorted(results[algorithm].keys()), [5, 10])
                for avg in results[algorithm].values():
                    self.assertIsInstance(avg, float)
                    self.assertGreaterEqual(avg, 0.0)

    def test_run_benchmark_handles_zero_size(self):
        results = benchmark.run_benchmark(sizes=(0,), repeats=1)
        for algorithm in ('bubble_sort', 'quick_sort', 'merge_sort', 'sorted'):
            with self.subTest(algorithm=algorithm):
                self.assertIn(algorithm, results)
                self.assertIn(0, results[algorithm])
                self.assertIsInstance(results[algorithm][0], float)
                self.assertGreaterEqual(results[algorithm][0], 0.0)


if __name__ == '__main__':
    unittest.main()
