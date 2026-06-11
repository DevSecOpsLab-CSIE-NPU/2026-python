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

from timing import timeit  # 完成 timing.py 後解除註解


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(3, 5), 8)
        self.assertIsNone(add(1, 2))

    def test_preserves_function_metadata(self):
        @timeit
        def my_func():
            """docstring"""
        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "docstring")

    def test_none_return(self):
        @timeit
        def noop():
            pass
        self.assertIsNone(noop())

    def test_records_elapsed_time(self):
        @timeit
        def sleep_a_bit():
            import time
            time.sleep(0.01)
        sleep_a_bit()
        self.assertIsInstance(sleep_a_bit.last_elapsed, float)
        self.assertGreater(sleep_a_bit.last_elapsed, 0)

    def test_records_multiple_calls(self):
        @timeit
        def do_nothing():
            pass
        do_nothing()
        do_nothing()
        self.assertEqual(len(do_nothing.records), 2)
        for t in do_nothing.records:
            self.assertIsInstance(t, float)


if __name__ == "__main__":
    unittest.main()
