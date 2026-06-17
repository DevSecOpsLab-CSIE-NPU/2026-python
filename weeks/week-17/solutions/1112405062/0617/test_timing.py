"""0617 任務一 — timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)
"""

import unittest
import math

from timing import timeit


def dummy() -> int:
    """Return 42."""
    return 42


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit
        def dummy() -> int:
            """Return 42."""
            return 42
        self.assertEqual(dummy.__name__, "dummy")
        self.assertEqual(dummy.__doc__, "Return 42.")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=4)
        def sleep_a_bit():
            import time
            time.sleep(0.01)
        result = sleep_a_bit()
        self.assertEqual(result, None)
        self.assertEqual(len(sleep_a_bit.records), 4)
        self.assertIsInstance(sleep_a_bit.last_elapsed, float)
        self.assertGreater(sleep_a_bit.last_elapsed, 0)

    def test_rejects_invalid_repeat(self):
        for bad in (0, -1, -100):
            with self.subTest(repeat=bad):
                with self.assertRaises(ValueError):
                    @timeit(repeat=bad)
                    def f():
                        pass

    def test_repeat_one_is_valid(self):
        @timeit(repeat=1)
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(len(add.records), 1)
        self.assertIsInstance(add.last_elapsed, float)

    def test_no_print_in_decorator(self):
        import io
        import sys
        @timeit
        def f():
            pass
        captured = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured
        try:
            f()
        finally:
            sys.stdout = old_stdout
        self.assertEqual(captured.getvalue(), "")

    def test_exception_leaves_records_unchanged(self):
        records_before = []
        @timeit(repeat=3)
        def crash():
            raise RuntimeError("boom")
        crash.records = [0.1, 0.2]
        records_before = list(crash.records)
        with self.assertRaises(RuntimeError):
            crash()
        self.assertEqual(crash.records, records_before)

    def test_default_repeat_is_three(self):
        @timeit
        def f():
            pass
        f()
        self.assertEqual(len(f.records), 3)

    def test_last_elapsed_is_average(self):
        @timeit(repeat=2)
        def f():
            import time
            time.sleep(0.01)
        f()
        expected = sum(f.records) / len(f.records)
        self.assertAlmostEqual(f.last_elapsed, expected)


if __name__ == "__main__":
    unittest.main()
