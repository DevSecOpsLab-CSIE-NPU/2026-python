import io
import unittest
from unittest.mock import patch

from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(3, 5), 8)

    def test_returns_original_result_different_types(self):
        @timeit
        def greet(name):
            return f"Hello, {name}!"
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_preserves_function_metadata(self):
        @timeit
        def sample():
            """Doc."""
            return 42
        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "Doc.")

    def test_repeat_records_and_average(self):
        @timeit(repeat=4)
        def short_sleep():
            import time
            time.sleep(0.01)

        short_sleep()
        self.assertEqual(len(short_sleep.records), 4)
        for rec in short_sleep.records:
            self.assertIsInstance(rec, float)
            self.assertGreater(rec, 0)
        self.assertIsInstance(short_sleep.last_elapsed, float)

    def test_records_reset_on_each_call(self):
        @timeit(repeat=2)
        def short_sleep():
            import time
            time.sleep(0.01)

        short_sleep()
        first = short_sleep.records.copy()
        short_sleep()
        self.assertNotEqual(short_sleep.records, first)
        self.assertEqual(len(short_sleep.records), 2)

    def test_repeat_one(self):
        @timeit(repeat=1)
        def short_sleep():
            import time
            time.sleep(0.01)

        short_sleep()
        self.assertEqual(len(short_sleep.records), 1)
        self.assertAlmostEqual(short_sleep.last_elapsed, short_sleep.records[0])

    def test_works_without_parentheses(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)

    def test_repeat_below_one_raises_valueerror(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f():
                pass
        with self.assertRaises(ValueError):
            @timeit(repeat=-1)
            def g():
                pass

    def test_rejects_float_repeat(self):
        with self.assertRaises(TypeError):
            @timeit(repeat=2.5)
            def f():
                pass

    def test_no_print_in_decorator(self):
        @timeit(repeat=2)
        def f():
            return 1

        with patch("sys.stdout", new_callable=io.StringIO) as mock:
            f()
            self.assertEqual(mock.getvalue(), "")

    def test_exception_propagation(self):
        @timeit(repeat=3)
        def will_raise():
            raise RuntimeError("boom")

        with self.assertRaises(RuntimeError):
            will_raise()


if __name__ == "__main__":
    unittest.main()
