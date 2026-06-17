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

import unittest
import time

# from timing import timeit  # 完成 timing.py 後解除註解


def dummy_func(x):
    """测试用的简单函数"""
    return x * 2


def side_effect_func():
    """带副作用的函数"""
    side_effect_func.call_count += 1
    return side_effect_func.call_count


def slow_func():
    """耗时函数"""
    time.sleep(0.001)
    return "slow"


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        from timing import timeit
        decorated = timeit(dummy_func)
        result = decorated(21)
        self.assertEqual(result, 42)

    def test_preserves_function_metadata(self):
        from timing import timeit
        decorated = timeit(dummy_func)
        self.assertEqual(decorated.__name__, "dummy_func")
        self.assertEqual(decorated.__doc__, "测试用的简单函数")

    def test_records_each_repeat_and_average(self):
        from timing import timeit
        decorated = timeit(slow_func)
        result = decorated()
        self.assertEqual(result, "slow")
        self.assertEqual(len(decorated.f.records), 3)
        self.assertAlmostEqual(decorated.f.last_elapsed, sum(decorated.f.records) / 3, places=6)

    def test_rejects_invalid_repeat(self):
        from timing import timeit
        with self.assertRaises(ValueError) as cm:
            timeit(slow_func, repeat=0)
        self.assertIn("repeat 必须 >= 1，收到: 0", str(cm.exception))

    def test_repeat_one(self):
        from timing import timeit
        decorated = timeit(slow_func, repeat=1)
        result = decorated()
        self.assertEqual(result, "slow")
        self.assertEqual(len(decorated.f.records), 1)
        self.assertEqual(decorated.f.last_elapsed, decorated.f.records[0])

    def test_function_with_side_effects(self):
        side_effect_func.call_count = 0
        from timing import timeit
        decorated = timeit(side_effect_func)
        result = decorated()
        self.assertEqual(result, 3)
        self.assertIsInstance(decorated.f.last_elapsed, float)
        self.assertEqual(len(decorated.f.records), 3)


if __name__ == "__main__":
    unittest.main()