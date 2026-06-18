
"""Stage 1 — @timeit 裝飾器測試。
 
規格：timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次（預設 3），把每次耗時（float 秒）append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不可 print
  6. repeat < 1 → raise ValueError（用 raise，不用 assert）
"""
 
import io
import unittest
from contextlib import redirect_stdout
 
from timing import timeit
 
 
class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """規格 1：回傳值不變。"""
 
        @timeit
        def add(a, b):
            return a + b
 
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, -4), 6)
 
    def test_preserves_function_metadata(self):
        """規格 2：functools.wraps 保留 __name__ / __doc__。"""
 
        @timeit
        def greet():
            """say hi"""
            return "hi"
 
        self.assertEqual(greet.__name__, "greet")
        self.assertEqual(greet.__doc__, "say hi")
 
    def test_repeat_records_and_average(self):
        """規格 3、4：每次呼叫跑 repeat 次，records 累積、last_elapsed 為平均。"""
 
        @timeit  # 預設 repeat=3
        def noop():
            return 42
 
        self.assertEqual(noop(), 42)
        self.assertEqual(len(noop.records), 3)
        for elapsed in noop.records:
            self.assertIsInstance(elapsed, float)
            self.assertGreaterEqual(elapsed, 0.0)
        self.assertAlmostEqual(noop.last_elapsed, sum(noop.records) / 3)
 
        # 再呼叫一次：records 持續累積（3 + 3），last_elapsed 只反映本次平均
        noop()
        self.assertEqual(len(noop.records), 6)
        self.assertAlmostEqual(noop.last_elapsed, sum(noop.records[-3:]) / 3)
 
    def test_custom_repeat_runs_function_n_times(self):
        """edge case：repeat 可自訂，副作用次數 = repeat。"""
 
        calls = []
 
        @timeit(repeat=1)
        def with_side_effect():
            calls.append(1)
            return len(calls)
 
        with_side_effect()
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(with_side_effect.records), 1)
        with_side_effect()
        self.assertEqual(len(calls), 2)
 
    def test_decorator_does_not_print(self):
        """規格 5：裝飾器內不可 print。"""
 
        @timeit
        def f():
            return 1
 
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            f()
        self.assertEqual(buffer.getvalue(), "")
 
    def test_repeat_below_one_raises_valueerror(self):
        """規格 6：repeat < 1 應 raise ValueError（不可用 assert）。"""
 
        with self.assertRaises(ValueError):
 
            @timeit(repeat=0)
            def f():
                return 1
 
        with self.assertRaises(ValueError):
 
            @timeit(repeat=-3)
            def g():
                return 1
 
 
if __name__ == "__main__":
    unittest.main()