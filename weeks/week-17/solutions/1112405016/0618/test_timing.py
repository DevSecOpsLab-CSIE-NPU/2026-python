"""Stage 1 — @timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時(float 秒)append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不准 print
  6. repeat < 1 → raise ValueError(用 raise,不准 assert)
"""

import unittest
import time
import io
import sys
from unittest.mock import patch

# 匯入待測的裝飾器
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """測試 1: 裝飾器不改變被裝飾函式的回傳值"""
        @timeit(repeat=3)
        def add(a, b):
            return a + b

        result = add(5, 7)
        self.assertEqual(result, 12)

    def test_preserves_function_metadata(self):
        """測試 2: 裝飾器保留原函式的 __name__ 與 __doc__"""
        @timeit(repeat=3)
        def my_func():
            """This is a docstring."""
            pass

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "This is a docstring.")

    def test_repeat_records_and_average(self):
        """測試 3: 記錄每次執行的耗時與平均耗時"""
        @timeit(repeat=4)
        def dummy_sleep():
            time.sleep(0.01)
            return "done"

        res = dummy_sleep()
        self.assertEqual(res, "done")
        
        # 驗證記錄屬性存在且正確
        self.assertTrue(has_attr := hasattr(dummy_sleep, "records"), "應該要有 records 屬性")
        self.assertTrue(has_elapsed := hasattr(dummy_sleep, "last_elapsed"), "應該要有 last_elapsed 屬性")
        
        if has_attr:
            self.assertEqual(len(dummy_sleep.records), 4)
            for t in dummy_sleep.records:
                self.assertIsInstance(t, float)
                self.assertGreaterEqual(t, 0.0)
                
        if has_attr and has_elapsed:
            expected_avg = sum(dummy_sleep.records) / len(dummy_sleep.records)
            self.assertAlmostEqual(dummy_sleep.last_elapsed, expected_avg, places=5)

    def test_repeat_below_one_raises_valueerror(self):
        """測試 4: 當 repeat < 1 時拋出 ValueError，不可使用 assert 驗證"""
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def test_func():
                pass

        with self.assertRaises(ValueError):
            @timeit(repeat=-5)
            def test_func2():
                pass

    def test_no_print_called(self):
        """測試 5: 裝飾器內部不准呼叫 print 輸出任何內容"""
        @timeit(repeat=2)
        def target_func():
            return 42

        # 擷取 stdout 檢查是否有 print
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            target_func()
        finally:
            sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "", "裝飾器內部不可有任何 print 輸出")

    def test_decorator_without_arguments(self):
        """測試 6: 支援無參數的 @timeit 寫法，預設 repeat=3"""
        @timeit
        def default_func():
            time.sleep(0.005)
            return "default"

        res = default_func()
        self.assertEqual(res, "default")
        self.assertEqual(len(default_func.records), 3)


if __name__ == "__main__":
    unittest.main()
