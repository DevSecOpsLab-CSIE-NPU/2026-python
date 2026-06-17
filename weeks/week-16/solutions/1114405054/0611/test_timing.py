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

import time
import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit
        def hello():
            """Say hello"""
            return "hello"

        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "Say hello")

    def test_records_elapsed_time(self):
        @timeit
        def snooze(secs):
            return time.sleep(secs)

        snooze(0.05)
        self.assertIsInstance(snooze.last_elapsed, float)
        self.assertGreater(snooze.last_elapsed, 0.01)
        self.assertEqual(len(snooze.records), 1)

        snooze(0.03)
        self.assertEqual(len(snooze.records), 2)

    def test_records_on_exception(self):
        @timeit
        def crash():
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            crash()
        self.assertEqual(len(crash.records), 1)
        self.assertIsInstance(crash.last_elapsed, float)


if __name__ == "__main__":
    unittest.main()
