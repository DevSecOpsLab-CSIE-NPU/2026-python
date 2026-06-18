"""0617 任務一: timeit 裝飾器測試。"""

import unittest
from unittest.mock import patch

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit
        def hello(name):
            """測試 docstring。"""
            return f"Hi, {name}"

        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "測試 docstring。")

    def test_records_each_repeat_and_average(self):
        perf_values = [
            1.0, 1.1,
            2.0, 2.5,
            3.0, 3.2,
        ]

        @timeit(repeat=3)
        def work(x):
            return x * 2

        with patch("timing.time.perf_counter", side_effect=perf_values):
            result = work(7)

        self.assertEqual(result, 14)
        self.assertEqual(len(work.records), 3)
        expected = [0.1, 0.5, 0.2]
        for actual, exp in zip(work.records, expected):
            self.assertAlmostEqual(actual, exp)
        self.assertAlmostEqual(work.last_elapsed, (0.1 + 0.5 + 0.2) / 3)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f1():
                return 1

        with self.assertRaises(ValueError):
            @timeit(repeat=-2)
            def f2():
                return 2


if __name__ == "__main__":
    unittest.main()
