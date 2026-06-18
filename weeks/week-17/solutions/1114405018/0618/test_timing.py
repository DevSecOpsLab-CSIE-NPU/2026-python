"""Stage 1 — @timeit 裝飾器測試"""

import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit
        def my_func():
            """docs"""
            pass
        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "docs")

    def test_repeat_records_and_average(self):
        @timeit(repeat=3)
        def do_nothing():
            pass
        do_nothing()
        self.assertEqual(len(do_nothing.records), 3)
        self.assertIsInstance(do_nothing.last_elapsed, float)

    def test_repeat_below_one_raises_valueerror(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f():
                pass

    def test_repeat_one_edge_case(self):
        @timeit(repeat=1)
        def do_nothing():
            pass
        do_nothing()
        self.assertEqual(len(do_nothing.records), 1)
        self.assertAlmostEqual(do_nothing.last_elapsed, do_nothing.records[0])

    def test_accumulated_records_across_calls(self):
        @timeit(repeat=2)
        def do_nothing():
            pass
        do_nothing()
        do_nothing()
        self.assertEqual(len(do_nothing.records), 4)


if __name__ == "__main__":
    unittest.main()
