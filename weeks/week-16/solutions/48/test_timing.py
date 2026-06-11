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

import io
import sys
import time
import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_preserves_function_metadata(self):
        @timeit
        def hello():
            """Say hello"""
            return "hello"

        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "Say hello")

    def test_records_elapsed_time(self):
        @timeit
        def slow():
            time.sleep(0.05)
            return "done"

        self.assertIsNone(slow.last_elapsed)
        self.assertEqual(slow.records, [])

        slow()
        self.assertIsInstance(slow.last_elapsed, float)
        self.assertGreaterEqual(slow.last_elapsed, 0.05)
        self.assertEqual(len(slow.records), 1)

        slow()
        self.assertEqual(len(slow.records), 2)

    def test_exception_propagates(self):
        @timeit
        def crash():
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            crash()

    def test_does_not_print(self):
        @timeit
        def noisy():
            pass

        captured = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured
        try:
            noisy()
        finally:
            sys.stdout = old_stdout
        self.assertEqual(captured.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
