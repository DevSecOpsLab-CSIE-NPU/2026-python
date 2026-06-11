"""Stage 1 — @timeit 裝飾器測試"""

import unittest
import time

# from timing import timeit  # 完成 timing.py 後解除註解


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_preserves_function_metadata(self):
        @timeit
        def my_func():
            """my doc"""
            return 42

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "my doc")

    def test_records_elapsed_time(self):
        @timeit
        def wait(sec):
            time.sleep(sec)
            return sec

        r1 = wait(0.01)
        self.assertIsInstance(r1, float)
        self.assertGreater(wait.last_elapsed, 0)

        r2 = wait(0.02)
        self.assertIsInstance(wait.records, list)
        self.assertEqual(len(wait.records), 2)
        self.assertAlmostEqual(wait.last_elapsed, wait.records[-1])

    def test_edge_case_no_args_returns_none(self):
        @timeit
        def noop():
            pass

        result = noop()
        self.assertIsNone(result)
        self.assertIsInstance(noop.last_elapsed, float)
        self.assertEqual(len(noop.records), 1)


if __name__ == "__main__":
    unittest.main()
