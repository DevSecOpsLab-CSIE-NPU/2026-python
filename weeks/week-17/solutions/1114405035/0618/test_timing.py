"""Stage 1 — @timeit 裝飾器測試骨架

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時(float 秒)append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不准 print
  6. repeat < 1 → raise ValueError(用 raise,不准 assert)

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面的測試(可再加);規格每條都要有覆蓋
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest

from timing import timeit
import time


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit(repeat=2)
        def dummy_add(a, b):
            return a + b
        res = dummy_add(3, 5)
        self.assertEqual(res, 8)

    def test_preserves_function_metadata(self):
        @timeit(repeat=1)
        def dummy_func():
            """This is docstring"""
            pass
        self.assertEqual(dummy_func.__name__, "dummy_func")
        self.assertEqual(dummy_func.__doc__, "This is docstring")

    def test_repeat_records_and_average(self):
        @timeit(repeat=3)
        def dummy_sleep():
            time.sleep(0.001)
            return "ok"

        # 第一次呼叫
        res = dummy_sleep()
        self.assertEqual(res, "ok")
        self.assertEqual(len(dummy_sleep.records), 3)
        self.assertAlmostEqual(dummy_sleep.last_elapsed, sum(dummy_sleep.records) / 3, places=5)

        # 第二次呼叫，驗證累積與 last_elapsed 更新
        dummy_sleep()
        self.assertEqual(len(dummy_sleep.records), 6)
        last_three_avg = sum(dummy_sleep.records[-3:]) / 3
        self.assertAlmostEqual(dummy_sleep.last_elapsed, last_three_avg, places=5)

    def test_repeat_below_one_raises_valueerror(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f1():
                pass
        with self.assertRaises(ValueError):
            @timeit(repeat=-2)
            def f2():
                pass


if __name__ == "__main__":
    unittest.main()
