"""Stage 1 — @timeit 裝飾器測試骨架

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫後更新 f.last_elapsed(float 秒)並 append 到 f.records
  4. 裝飾器內不准 print

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面三個測試(可再加)
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest
import time
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(a=1, b=4), 5)

    def test_preserves_function_metadata(self):
        @timeit
        def my_func():
            """This is my docstring."""
            pass
        
        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "This is my docstring.")

    def test_records_elapsed_time(self):
        @timeit
        def slow_func():
            time.sleep(0.01)
            return "done"
            
        # Before calling, attributes shouldn't exist, or they can be empty
        # Wait, the spec says: "每次呼叫後" records it, so we can check if they are initialized after first call
        res = slow_func()
        self.assertEqual(res, "done")
        self.assertTrue(hasattr(slow_func, "last_elapsed"))
        self.assertTrue(hasattr(slow_func, "records"))
        self.assertIsInstance(slow_func.last_elapsed, float)
        self.assertGreaterEqual(slow_func.last_elapsed, 0.01)
        self.assertEqual(len(slow_func.records), 1)
        self.assertEqual(slow_func.records[0], slow_func.last_elapsed)
        
        # Second call
        slow_func()
        self.assertEqual(len(slow_func.records), 2)
        self.assertEqual(slow_func.records[-1], slow_func.last_elapsed)

    def test_records_time_on_exception(self):
        @timeit
        def failing_func():
            time.sleep(0.01)
            raise ValueError("Something went wrong")
            
        with self.assertRaises(ValueError):
            failing_func()
            
        self.assertTrue(hasattr(failing_func, "last_elapsed"))
        self.assertTrue(hasattr(failing_func, "records"))
        self.assertIsInstance(failing_func.last_elapsed, float)
        self.assertGreaterEqual(failing_func.last_elapsed, 0.01)
        self.assertEqual(len(failing_func.records), 1)


if __name__ == "__main__":
    unittest.main()

