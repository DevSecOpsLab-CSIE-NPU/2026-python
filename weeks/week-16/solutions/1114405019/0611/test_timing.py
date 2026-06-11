"""Stage 1 — @timeit 裝飾器測試"""
import io
import sys
import time
import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add("hello", " world"), "hello world")

        @timeit
        def identity(x):
            return x

        self.assertIsNone(identity(None))

    def test_preserves_function_metadata(self):
        @timeit
        def my_func():
            """My docstring"""
            pass

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "My docstring")

    def test_records_elapsed_time(self):
        @timeit
        def slow():
            time.sleep(0.01)

        slow()
        self.assertIsInstance(slow.last_elapsed, float)
        self.assertGreater(slow.last_elapsed, 0.005)
        self.assertEqual(len(slow.records), 1)

        slow()
        self.assertEqual(len(slow.records), 2)
        self.assertEqual(slow.last_elapsed, slow.records[-1])

    def test_records_accumulate_over_multiple_calls(self):
        @timeit
        def noop():
            pass

        for _ in range(5):
            noop()

        self.assertEqual(len(noop.records), 5)
        self.assertEqual(noop.last_elapsed, noop.records[-1])

    def test_no_print_output(self):
        @timeit
        def func():
            return 42

        captured = io.StringIO()
        sys.stdout = captured
        try:
            func()
        finally:
            sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
