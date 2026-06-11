"""Stage 1 tests for the @timeit decorator.

These tests are intentionally written before timing.py exists, so the first
unittest run should be red. After committing the red test, implement timing.py.
"""

import builtins
import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            """Return a plus b."""
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit
        def sample_function():
            """Original docstring."""
            return "ok"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Original docstring.")

    def test_records_elapsed_time_for_each_call(self):
        @timeit
        def echo(value):
            return value

        self.assertFalse(hasattr(echo, "last_elapsed"))
        self.assertEqual(echo.records, [])

        self.assertEqual(echo("first"), "first")
        first_elapsed = echo.last_elapsed

        self.assertIsInstance(first_elapsed, float)
        self.assertGreaterEqual(first_elapsed, 0.0)
        self.assertEqual(len(echo.records), 1)
        self.assertIs(echo.records[0], first_elapsed)

        self.assertEqual(echo("second"), "second")
        self.assertIsInstance(echo.last_elapsed, float)
        self.assertGreaterEqual(echo.last_elapsed, 0.0)
        self.assertEqual(len(echo.records), 2)
        self.assertIs(echo.records[-1], echo.last_elapsed)

    def test_decorator_does_not_print(self):
        printed = []
        original_print = builtins.print

        def fake_print(*args, **kwargs):
            printed.append((args, kwargs))

        builtins.print = fake_print
        try:
            @timeit
            def quiet_function():
                return "quiet"

            self.assertEqual(quiet_function(), "quiet")
        finally:
            builtins.print = original_print

        self.assertEqual(printed, [])


if __name__ == "__main__":
    unittest.main()
