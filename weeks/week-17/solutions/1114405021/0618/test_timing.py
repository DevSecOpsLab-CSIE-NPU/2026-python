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
from time import sleep

from timing import timeit


class TestTimeit(unittest.TestCase):
    """timeit 裝飾器測試"""

    def test_returns_original_result(self):
        """測試回傳值是否保持完全不變"""

        @timeit
        def add(a, b):
            return a + b

        result = add(2, 3)
        self.assertEqual(result, 5)  # 回傳值與原始函式相同

    def test_preserves_function_metadata(self):
        """測試是否保留 __name__ / __doc__"""

        @timeit
        def multiply(x, y):
            """這個函式將兩個數字相乘"""
            return x * y

        self.assertEqual(multiply.__name__, "multiply")
        self.assertEqual(multiply.__doc__, "這個函式將兩個數字相乘")

    def test_repeat_records_and_average(self):
        """測試 repeat 取平均紀錄功能"""

        @timeit(repeat=5)
        def slow_function():
            sleep(0.01)
            return "ok"

        result = slow_function()
        self.assertEqual(result, "ok")
        self.assertTrue(hasattr(slow_function, "records"))
        self.assertTrue(hasattr(slow_function, "last_elapsed"))
        self.assertIsInstance(slow_function.records, list)
        self.assertGreaterEqual(len(slow_function.records), 1)

    def test_repeat_below_one_raises_valueerror(self):
        """測試 repeat < 1 時要 raise ValueError"""
        with self.assertRaises(ValueError):
            timeit(repeat=0)(lambda: None)

    def test_function_exception_propagates(self):
        """測試被裝飾函式拋出例外時裝飾器重新拋擲"""

        @timeit
        def raise_exception():
            raise ValueError("test error")

        with self.assertRaises(ValueError):
            raise_exception()

    def test_repeat_parameter_default(self):
        """測試 repeat 預設值"""

        @timeit
        def test():
            pass

        # 預設 repeat=3，應該有記錄
        # 呼叫一次後，wrapper 應該有 records 屬性
        test()
        self.assertTrue(hasattr(test, "records"))
        self.assertEqual(len(test.records), 3)


if __name__ == "__main__":
    unittest.main()
