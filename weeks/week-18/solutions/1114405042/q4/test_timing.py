"""Stage 1 — timeit 裝飾器測試骨架

規格: timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時(float 秒)append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不准 print
  6. repeat < 1 → raise ValueError(用 raise,不准 assert)

待辦:
  1. 補齊下面的測試(可再加);規格每條都要有覆蓋
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest
import time
import functools
from timing import timeit


class TestTimeit(unittest.TestCase):
    """timeit 裝飾器的單元測試"""

    def test_returns_original_result(self):
        """被裝飾函式的回傳值不變"""
        @timeit
        def add(a, b):
            return a + b

        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_preserves_function_metadata(self):
        """用 functools.wraps 保留 __name__ / __doc__"""
        @timeit
        def func_with_doc():
            """這是文檔字串"""
            return 42

        self.assertEqual(func_with_doc.__name__, "func_with_doc")
        self.assertEqual(func_with_doc.__doc__, "這是文檔字串")

    def test_repeat_records_and_average(self):
        """測試 timeit 的 repeat 參數"""
        @timeit(repeat=3)
        def slow_func(n):
            total = 0
            for i in range(n):
                total += i
            return total

        result = slow_func(1000)
        self.assertEqual(result, 499500)
        self.assertIsNotNone(slow_func.last_elapsed)
        self.assertIsInstance(slow_func.last_elapsed, float)
        self.assertEqual(len(slow_func.records), 3)

    def test_repeat_below_one_raises_valueerror(self):
        """repeat < 1 → raise ValueError"""
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def func():
                return 1
            func()

    def test_no_print_in_decorator(self):
        """裝飾器內不准 print"""
        import io
        import sys

        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            @timeit
            def silent_func():
                return "ok"

            result = silent_func()
            output = sys.stdout.getvalue()
            self.assertEqual(output, "")
        finally:
            sys.stdout = old_stdout


if __name__ == "__main__":
    unittest.main()
