"""0617 任務一 — timeit 裝飾器測試"""

import io
import unittest
from unittest.mock import patch

from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_returns_original_result_different_types(self):
        @timeit
        def greet(name):
            return f"Hello, {name}!"

        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_preserves_function_metadata(self):
        @timeit
        def sample_function():
            """Sample docstring."""
            return 42

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Sample docstring.")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=4)
        def short_sleep():
            import time
            time.sleep(0.01)
            return 0

        short_sleep()
        self.assertEqual(len(short_sleep.records), 4)
        for rec in short_sleep.records:
            self.assertIsInstance(rec, float)
            self.assertGreater(rec, 0)
        self.assertIsInstance(short_sleep.last_elapsed, float)
        self.assertGreater(short_sleep.last_elapsed, 0)

    def test_records_reset_on_each_call(self):
        @timeit(repeat=2)
        def short_sleep():
            import time
            time.sleep(0.01)

        short_sleep()
        first_records = short_sleep.records.copy()
        short_sleep()
        self.assertNotEqual(short_sleep.records, first_records,
                            "records should reset on each call")
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

        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_rejects_invalid_repeat(self):
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

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            f()
            output = mock_stdout.getvalue()
            self.assertEqual(output, "", "decorator should not print")

    def test_exception_propagation(self):
        @timeit(repeat=3)
        def will_raise():
            raise RuntimeError("boom")

        with self.assertRaises(RuntimeError):
            will_raise()

    def test_wraps_class_method(self):
        class MyClass:
            @timeit
            def method(self, x):
                return x * 2

        obj = MyClass()
        result = obj.method(5)
        self.assertEqual(result, 10)

    def test_wraps_static_method(self):
        class MyClass:
            @staticmethod
            @timeit
            def static_method(x):
                return x + 1

        result = MyClass.static_method(3)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
