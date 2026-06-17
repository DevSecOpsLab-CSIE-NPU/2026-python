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
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(3, 5), 8)

    def test_preserves_function_metadata(self):
        @timeit
        def hello(name):
            """Greet someone."""
            return f"Hello, {name}!"

        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "Greet someone.")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=4)
        def sleep_a_bit(sec):
            time.sleep(sec)

        sleep_a_bit(0.01)
        self.assertIsInstance(sleep_a_bit.records, list)
        self.assertEqual(len(sleep_a_bit.records), 4)
        self.assertIsInstance(sleep_a_bit.last_elapsed, float)
        self.assertGreater(sleep_a_bit.last_elapsed, 0)

        sleep_a_bit(0.01)
        self.assertEqual(len(sleep_a_bit.records), 8)

    def test_rejects_invalid_repeat(self):
        for invalid in (0, -1, -100):
            with self.subTest(repeat=invalid):
                with self.assertRaises(ValueError):

                    @timeit(repeat=invalid)
                    def f():
                        pass


if __name__ == "__main__":
    unittest.main()
