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
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """被裝飾函式的回傳值不變"""
        @timeit(repeat=3)
        def add(a, b):
            return a + b
        
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_preserves_function_metadata(self):
        """用 functools.wraps 保留 __name__ / __doc__"""
        @timeit(repeat=3)
        def my_function():
            """這是文件字串"""
            pass
        
        self.assertEqual(my_function.__name__, "my_function")
        self.assertEqual(my_function.__doc__, "這是文件字串")
    
    def test_records_each_repeat_and_average(self):
        """每次呼叫實際跑 repeat 次，記錄每次耗時，計算平均"""
        @timeit(repeat=3)
        def slow_func():
            time.sleep(0.01)
            return "done"
        
        result = slow_func()
        self.assertEqual(result, "done")
        self.assertEqual(len(slow_func.records), 3)
        self.assertIsInstance(slow_func.last_elapsed, float)
        self.assertAlmostEqual(slow_func.last_elapsed, sum(slow_func.records) / 3, places=5)
    
    def test_rejects_invalid_repeat(self):
        """repeat < 1 應 raise ValueError(不准 assert)"""
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def func():
                pass
        
        with self.assertRaises(ValueError):
            @timeit(repeat=-1)
            def func():
                pass
    
    def test_repeat_default_is_three(self):
        """預設 repeat=3"""
        @timeit()
        def func():
            pass
        
        func()
        self.assertEqual(len(func.records), 3)
    
    def test_repeat_one_works(self):
        """repeat=1 也能正常運作"""
        @timeit(repeat=1)
        def func():
            return 42
        
        result = func()
        self.assertEqual(result, 42)
        self.assertEqual(len(func.records), 1)
        self.assertEqual(func.last_elapsed, func.records[0])
    
    def test_side_effects_called_multiple_times(self):
        """被裝飾函式有副作用會被呼叫 repeat 次"""
        counter = {"count": 0}
        
        @timeit(repeat=3)
        def increment():
            counter["count"] += 1
            return counter["count"]
        
        result = increment()
        self.assertEqual(result, 3)  # 最後一次呼叫的結果
        self.assertEqual(counter["count"], 3)  # 被呼叫了 3 次


if __name__ == "__main__":
    unittest.main()