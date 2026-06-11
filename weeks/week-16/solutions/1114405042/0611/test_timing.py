"""Stage 1 — @timeit 裝飾器測試"""

import io
import sys
import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit
        def my_func():
            """docstring"""
            pass

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "docstring")

    def test_records_elapsed_time(self):
        @timeit
        def slow_func():
            total = 0
            for i in range(1000000):
                total += i
            return total

        slow_func()
        self.assertIsInstance(slow_func.last_elapsed, float)
        self.assertGreater(slow_func.last_elapsed, 0)

        slow_func()
        self.assertEqual(len(slow_func.records), 2)
        self.assertIsInstance(slow_func.records[0], float)

    def test_no_print(self):
        @timeit
        def quiet():
            return 42

        captured = io.StringIO()
        sys.stdout = captured
        quiet()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertEqual(output, "")


if __name__ == "__main__":
    unittest.main()
