"""0617 任務一 — timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)
  6. repeat 非 int → raise TypeError
"""

import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit(repeat=3)
        def add(a, b):
            return a + b

        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_preserves_function_metadata(self):
        @timeit(repeat=3)
        def my_function():
            """My custom docstring."""
            return 42

        self.assertEqual(my_function.__name__, "my_function")
        self.assertEqual(my_function.__doc__, "My custom docstring.")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=4)
        def do_nothing():
            return None

        do_nothing()
        self.assertEqual(len(do_nothing.records), 4)
        for t in do_nothing.records:
            self.assertIsInstance(t, float)
        self.assertIsInstance(do_nothing.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f():
                pass

        with self.assertRaises(ValueError):
            @timeit(repeat=-1)
            def g():
                pass

    def test_rejects_non_int_repeat(self):
        with self.assertRaises(TypeError):
            @timeit(repeat=2.5)
            def f():
                pass

        with self.assertRaises(TypeError):
            @timeit(repeat="3")
            def g():
                pass

    def test_repeat_one_boundary(self):
        @timeit(repeat=1)
        def add(a, b):
            return a + b

        result = add(3, 4)
        self.assertEqual(result, 7)
        self.assertEqual(len(add.records), 1)
        self.assertEqual(add.last_elapsed, add.records[0])

    def test_propagates_wrapped_exception(self):
        @timeit(repeat=3)
        def will_raise():
            raise RuntimeError("oops")

        with self.assertRaises(RuntimeError):
            will_raise()


if __name__ == "__main__":
    unittest.main()
