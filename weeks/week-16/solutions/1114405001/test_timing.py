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

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit
        def greet(name):
            """say hi"""
            return f"hi, {name}"

        self.assertEqual(greet.__name__, "greet")
        self.assertEqual(greet.__doc__, "say hi")

    def test_records_elapsed_time(self):
        @timeit
        def multiply(a, b):
            return a * b

        first = multiply(3, 4)
        second = multiply(5, 6)

        self.assertEqual(first, 12)
        self.assertEqual(second, 30)
        self.assertTrue(hasattr(multiply, "last_elapsed"))
        self.assertTrue(hasattr(multiply, "records"))
        self.assertIsInstance(multiply.last_elapsed, float)
        self.assertIsInstance(multiply.records, list)
        self.assertGreaterEqual(len(multiply.records), 2)


if __name__ == "__main__":
    unittest.main()
