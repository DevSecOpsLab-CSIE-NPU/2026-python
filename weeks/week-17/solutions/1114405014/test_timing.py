"""0617 任務一 — timeit 裝飾器測試

規格: timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)

本測試採用:
  - @timeit(repeat=3) 作為主要使用方式
  - repeat 必須是 int 且 >= 1
  - repeat=0、負數、浮點數、字串都應 raise ValueError
  - records 跨呼叫累積
  - 被裝飾函式有副作用時，會實際執行 repeat 次
"""

import io
import unittest
from contextlib import redirect_stdout

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """裝飾後不可改變原函式的回傳值。"""

        @timeit(repeat=3)
        def add(a, b):
            return a + b

        result = add(2, 5)

        self.assertEqual(result, 7)

    def test_preserves_function_metadata(self):
        """應使用 functools.wraps 保留 __name__ 與 __doc__。"""

        @timeit(repeat=3)
        def sample_function():
            """這是測試用函式文件字串。"""
            return "ok"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "這是測試用函式文件字串。")

    def test_records_each_repeat_and_average(self):
        """每次呼叫應執行 repeat 次，記錄每次耗時，並計算平均耗時。"""

        counter = {"count": 0}

        @timeit(repeat=3)
        def side_effect_function():
            counter["count"] += 1
            return counter["count"]

        first_result = side_effect_function()

        self.assertEqual(first_result, 3)
        self.assertEqual(counter["count"], 3)
        self.assertEqual(len(side_effect_function.records), 3)
        self.assertIsInstance(side_effect_function.last_elapsed, float)
        self.assertGreaterEqual(side_effect_function.last_elapsed, 0.0)

        second_result = side_effect_function()

        self.assertEqual(second_result, 6)
        self.assertEqual(counter["count"], 6)
        self.assertEqual(len(side_effect_function.records), 6)
        self.assertIsInstance(side_effect_function.last_elapsed, float)
        self.assertGreaterEqual(side_effect_function.last_elapsed, 0.0)

    def test_repeat_one_runs_once(self):
        """repeat=1 是合法邊界值，且函式只會執行一次。"""

        counter = {"count": 0}

        @timeit(repeat=1)
        def run_once():
            counter["count"] += 1
            return "done"

        result = run_once()

        self.assertEqual(result, "done")
        self.assertEqual(counter["count"], 1)
        self.assertEqual(len(run_once.records), 1)
        self.assertIsInstance(run_once.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        """repeat 必須是 int 且 >= 1；錯誤時應 raise ValueError。"""

        invalid_repeats = [0, -1, 1.5, "3"]

        for invalid_repeat in invalid_repeats:
            with self.subTest(repeat=invalid_repeat):
                with self.assertRaises(ValueError):

                    @timeit(repeat=invalid_repeat)
                    def sample():
                        return "should not run"

    def test_decorator_does_not_print(self):
        """裝飾器內不應該 print。"""

        @timeit(repeat=3)
        def silent_function():
            return "silent"

        output = io.StringIO()

        with redirect_stdout(output):
            result = silent_function()

        self.assertEqual(result, "silent")
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()