import unittest
import time
import math
from timing import timeit


class TestTimeitDecorator(unittest.TestCase):

    def test_default_repeat(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 4)
        self.assertEqual(result, 7)
        self.assertTrue(hasattr(add, 'records'))
        self.assertTrue(hasattr(add, 'last_elapsed'))
        self.assertEqual(len(add.records), 3)
        self.assertIsInstance(add.last_elapsed, float)

    def test_custom_repeat(self):
        @timeit(repeat=5)
        def multiply(a, b):
            return a * b

        result = multiply(3, 4)
        self.assertEqual(result, 12)
        self.assertEqual(len(multiply.records), 5)

    def test_repeat_one(self):
        @timeit(repeat=1)
        def identity(x):
            return x

        result = identity(42)
        self.assertEqual(result, 42)
        self.assertEqual(len(identity.records), 1)

    def test_repeat_less_than_one_raises(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def dummy():
                pass

        with self.assertRaises(ValueError):
            @timeit(repeat=-1)
            def dummy2():
                pass

    def test_last_elapsed_is_average(self):
        @timeit(repeat=3)
        def slow():
            time.sleep(0.01)

        slow()
        total = sum(slow.records)
        avg = total / 3
        self.assertAlmostEqual(slow.last_elapsed, avg, places=6)

    def test_functools_wraps_preserved(self):
        @timeit(repeat=2)
        def my_func():
            """docstring"""
            pass

        self.assertEqual(my_func.__name__, 'my_func')
        self.assertEqual(my_func.__doc__, 'docstring')

    def test_multiple_calls_accumulate_records(self):
        @timeit(repeat=2)
        def inc(x):
            return x + 1

        inc(1)
        inc(10)
        inc(100)
        self.assertEqual(len(inc.records), 6)

    def test_function_with_no_return(self):
        @timeit(repeat=2)
        def no_return():
            pass

        result = no_return()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
