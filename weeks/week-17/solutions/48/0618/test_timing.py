"""Stage 1 — @timeit 裝飾器測試"""

import unittest
import time

from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit(repeat=3)
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit(repeat=3)
        def greet(name):
            """Say hello to name."""
            return f"Hello, {name}"
        self.assertEqual(greet.__name__, "greet")
        self.assertEqual(greet.__doc__, "Say hello to name.")

    def test_repeat_records_and_average(self):
        @timeit(repeat=5)
        def add(a, b):
            return a + b
        for _ in range(3):
            add(1, 2)
        self.assertEqual(len(add.records), 5 * 3)
        self.assertIsInstance(add.last_elapsed, float)
        self.assertGreater(add.last_elapsed, 0)

    def test_repeat_below_one_raises_valueerror(self):
        for invalid in (0, -1, -100):
            with self.subTest(repeat=invalid):
                with self.assertRaises(ValueError):
                    @timeit(repeat=invalid)
                    def _dummy():
                        pass

    def test_default_repeat_is_three(self):
        @timeit()
        def dummy():
            pass
        dummy()
        self.assertEqual(len(dummy.records), 3)

    def test_non_integer_repeat_type_error(self):
        for invalid in ("3", 2.5, [1, 2]):
            with self.subTest(repeat=invalid):
                with self.assertRaises(TypeError):
                    @timeit(repeat=invalid)
                    def _dummy():
                        pass

    def test_exception_pass_through(self):
        @timeit(repeat=3)
        def crash():
            raise ZeroDivisionError("oops")
        with self.assertRaises(ZeroDivisionError):
            crash()

    def test_timing_records_positive(self):
        @timeit(repeat=3)
        def snooze():
            time.sleep(0.05)
        snooze()
        for t in snooze.records:
            self.assertGreater(t, 0)
        self.assertGreater(snooze.last_elapsed, 0)


if __name__ == "__main__":
    unittest.main()
