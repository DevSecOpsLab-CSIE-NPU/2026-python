"""0617 任務一 — timeit 裝飾器測試骨架

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面四個測試(可再加)
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: 0617 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: 0617 實作 timeit 裝飾器"

提醒:
  - test_rejects_invalid_repeat 就是本日的安全測試(raise 而非 assert)。
  - edge case 自己想(repeat=1?被裝飾函式有副作用會被多算嗎?)。
"""

import time
import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """1. 被裝飾函式的回傳值不變"""
        @timeit(repeat=2)
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        """2. 用 functools.wraps 保留 __name__ / __doc__"""
        @timeit(repeat=3)
        def dummy_func():
            """This is a dummy docstring for testing metadata preservation."""
            return 42
        self.assertEqual(dummy_func.__name__, "dummy_func")
        self.assertEqual(dummy_func.__doc__, "This is a dummy docstring for testing metadata preservation.")

    def test_records_each_repeat_and_average(self):
        """3. 每次呼叫實際跑 repeat 次，把每次耗時記錄在 f.records，f.last_elapsed 為平均耗時"""
        @timeit(repeat=3)
        def sample_sleep():
            time.sleep(0.01)
            return "done"

        # 第一次呼叫
        res = sample_sleep()
        self.assertEqual(res, "done")
        self.assertEqual(len(sample_sleep.records), 3)
        self.assertGreater(sample_sleep.last_elapsed, 0)
        expected_avg = sum(sample_sleep.records) / 3
        self.assertAlmostEqual(sample_sleep.last_elapsed, expected_avg, places=6)

        # 第二次呼叫，累積 records
        sample_sleep()
        self.assertEqual(len(sample_sleep.records), 6)

    def test_rejects_invalid_repeat(self):
        """5. repeat < 1 應 raise ValueError (用 raise，不准 assert)"""
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f0():
                pass

        with self.assertRaises(ValueError):
            @timeit(repeat=-2)
            def f_neg():
                pass

        with self.assertRaises(ValueError):
            @timeit(repeat="not-an-integer")
            def f_str():
                pass

    def test_default_repeat_value(self):
        """測試預設 repeat 參數為 3"""
        @timeit()
        def sample_default():
            return "default"
        sample_default()
        self.assertEqual(len(sample_default.records), 3)


if __name__ == "__main__":
    unittest.main()

