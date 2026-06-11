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
from timing import timeit  # 測試階段如果沒有 timing.py 會噴錯，這也是一種紅燈


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        
        self.assertEqual(add(3, 5), 8)

    def test_preserves_function_metadata(self):
        @timeit
        def dummy_func():
            """This is a dummy function."""
            pass

        self.assertEqual(dummy_func.__name__, "dummy_func")
        self.assertEqual(dummy_func.__doc__, "This is a dummy function.")

    def test_records_elapsed_time(self):
        @timeit
        def delay_func():
            time.sleep(0.01)
            return "done"

        # 呼叫第一次
        result = delay_func()
        self.assertEqual(result, "done")
        self.assertTrue(hasattr(delay_func, "last_elapsed"))
        self.assertTrue(hasattr(delay_func, "records"))
        self.assertIsInstance(delay_func.last_elapsed, float)
        self.assertGreater(delay_func.last_elapsed, 0)
        self.assertEqual(len(delay_func.records), 1)
        self.assertEqual(delay_func.records[-1], delay_func.last_elapsed)

        # 呼叫第二次
        delay_func()
        self.assertEqual(len(delay_func.records), 2)
        self.assertEqual(delay_func.records[-1], delay_func.last_elapsed)

    def test_edge_case_exception_propagates(self):
        """Edge Case: 確保被裝飾的函式發生例外時，例外能被正確拋出。"""
        @timeit
        def error_func():
            raise ValueError("Something went wrong")

        with self.assertRaises(ValueError) as context:
            error_func()
        self.assertEqual(str(context.exception), "Something went wrong")


if __name__ == "__main__":
    unittest.main()
