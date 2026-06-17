"""0617 任務一 — timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)

紅燈 commit: test: 0617 timeit 裝飾器測試
綠燈 commit: feat: 0617 實作 timeit 裝飾器
"""

import unittest
import time

from timing import timeit


def slow_add(a, b):
    """回傳 a + b,但故意慢一點"""
    time.sleep(0.01)
    return a + b


def side_effect_counter():
    """有副作用的函式,用來測 repeat 會被多調幾次"""
    side_effect_counter.count += 1
    return side_effect_counter.count


side_effect_counter.count = 0


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """被裝飾函式的回傳值不變"""
        decorated = timeit(slow_add)
        result = decorated(1, 2)
        self.assertEqual(result, 3)

    def test_preserves_function_metadata(self):
        """用 functools.wraps 保留 __name__ / __doc__"""
        decorated = timeit(slow_add)
        self.assertEqual(decorated.__name__, "slow_add")
        self.assertEqual(decorated.__doc__, "回傳 a + b,但故意慢一點")

    def test_records_each_repeat_and_average(self):
        """每次呼叫跑 repeat 次,每次耗時記錄在 records,last_elapsed 是平均"""
        decorated = timeit(slow_add)
        decorated(1, 2)
        # 預設 repeat=3,所以 records 應有 3 筆
        self.assertEqual(len(decorated.records), 3)
        # 每筆都是 float 秒
        for t in decorated.records:
            self.assertIsInstance(t, float)
        # last_elapsed 是平均
        expected_avg = sum(decorated.records) / len(decorated.records)
        self.assertAlmostEqual(decorated.last_elapsed, expected_avg, places=6)

    def test_rejects_invalid_repeat(self):
        """repeat < 1 應 raise ValueError(不准 assert)"""
        with self.assertRaises(ValueError):
            timeit(slow_add, repeat=0)
        with self.assertRaises(ValueError):
            timeit(slow_add, repeat=-1)


if __name__ == "__main__":
    unittest.main()
