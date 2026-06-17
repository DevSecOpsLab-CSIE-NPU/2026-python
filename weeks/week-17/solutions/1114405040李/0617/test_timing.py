"""Tests for the 0617 timeit assignment."""

import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit()
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit()
        def sample():
            """sample docstring"""
            return "ok"

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "sample docstring")

    def test_records_each_repeat_and_average(self):
        calls = []

        @timeit(repeat=3)
        def count_calls():
            calls.append("called")
            return len(calls)

        self.assertEqual(count_calls(), 3)
        self.assertEqual(len(calls), 3)
        self.assertEqual(len(count_calls.records), 3)
        self.assertTrue(all(isinstance(item, float) for item in count_calls.records))
        self.assertAlmostEqual(
            count_calls.last_elapsed,
            sum(count_calls.records) / len(count_calls.records),
        )

    def test_repeat_one_runs_once(self):
        calls = []

        @timeit(repeat=1)
        def once():
            calls.append("called")
            return "done"

        self.assertEqual(once(), "done")
        self.assertEqual(calls, ["called"])
        self.assertEqual(len(once.records), 1)
        self.assertIsInstance(once.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            timeit(repeat=0)


if __name__ == "__main__":
    unittest.main()
