"""0617 任務一 — timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)
  6. repeat 非 int → raise ValueError
  7. 被裝飾函式拋出例外時,例外原樣往外傳,且當次不計入 records
"""

import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_value_unchanged(self):
        # 驗證裝飾器不改變函式的對外行為(回傳值與原函式直接呼叫一致)
        @timeit()
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_repeat_runs_n_times(self):
        # 驗證真的重複執行了指定次數(用 counter 累加呼叫次數)
        counter = {"calls": 0}

        @timeit(repeat=5)
        def touch():
            counter["calls"] += 1
            return counter["calls"]

        touch()
        self.assertEqual(counter["calls"], 5)
        self.assertEqual(len(touch.records), 5)

    def test_repeat_less_than_one_raises(self):
        # repeat < 1 → 應 raise ValueError(用 raise,不准 assert)
        with self.assertRaises(ValueError):
            timeit(repeat=0)

        with self.assertRaises(ValueError):
            timeit(repeat=-1)

    def test_repeat_non_int_raises(self):
        # repeat 不是 int(例如字串、float)→ 應 raise ValueError
        with self.assertRaises(ValueError):
            timeit(repeat="3")

        with self.assertRaises(ValueError):
            timeit(repeat=2.5)

    def test_records_accumulates_across_calls(self):
        # records 是累積的全歷史,呼叫多次不會被清空
        @timeit(repeat=3)
        def noop():
            return None

        noop()
        noop()
        self.assertEqual(len(noop.records), 6)
        self.assertTrue(all(isinstance(t, float) for t in noop.records))

    def test_last_elapsed_is_average_of_this_call(self):
        # last_elapsed 是「本次」repeat 的平均耗時,不是全歷史平均
        @timeit(repeat=4)
        def noop():
            return None

        noop()
        first_records = list(noop.records)
        self.assertAlmostEqual(noop.last_elapsed, sum(first_records) / len(first_records))

    def test_preserves_function_metadata(self):
        # functools.wraps 保留 __name__ / __doc__
        @timeit()
        def documented():
            """這是文件字串。"""
            return 1

        self.assertEqual(documented.__name__, "documented")
        self.assertEqual(documented.__doc__, "這是文件字串。")

    def test_exception_propagates_and_not_recorded(self):
        # 被裝飾函式拋例外時,例外要原樣往外傳,且該次不計入 records
        @timeit(repeat=3)
        def always_fails():
            raise RuntimeError("boom")

        with self.assertRaises(RuntimeError):
            always_fails()

        self.assertEqual(len(always_fails.records), 0)


if __name__ == "__main__":
    unittest.main()
