"""Stage 1 — @timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
   1. 不改變被裝飾函式的回傳值
   2. 用 functools.wraps 保留 __name__ / __doc__
   3. 每次呼叫後更新 f.last_elapsed(float 秒)並 append 到 f.records
   4. 裝飾器內不准 print
"""

import time
import unittest

# from timing import timeit  # 完成 timing.py 後解除註解


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_preserves_function_metadata(self):
        @timeit
        def greet(name):
            """Say hello to someone."""
            return f"Hello, {name}!"

        self.assertEqual(greet.__name__, "greet")
        self.assertEqual(greet.__doc__, "Say hello to someone.")

    def test_records_elapsed_time(self):
        @timeit
        def slow_add(a, b):
            time.sleep(0.01)
            return a + b

        r1 = slow_add(1, 2)
        self.assertEqual(r1, 3)
        self.assertIsInstance(slow_add.last_elapsed, float)
        self.assertGreater(slow_add.last_elapsed, 0)

        r2 = slow_add(3, 4)
        self.assertEqual(r2, 7)
        self.assertEqual(len(slow_add.records), 2)
        for t in slow_add.records:
            self.assertIsInstance(t, float)
            self.assertGreater(t, 0)


if __name__ == "__main__":
    unittest.main()
