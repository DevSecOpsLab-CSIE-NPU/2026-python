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
from unittest.mock import patch

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit
        def sample():
            """demo doc"""
            return "ok"

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "demo doc")

    def test_records_elapsed_time(self):
        @timeit
        def work(x):
            return x * 2

        work(1)
        work(2)

        self.assertTrue(hasattr(work, "last_elapsed"))
        self.assertTrue(hasattr(work, "records"))
        self.assertIsInstance(work.last_elapsed, float)
        self.assertIsInstance(work.records, list)
        self.assertEqual(len(work.records), 2)
        self.assertEqual(work.last_elapsed, work.records[-1])

    def test_edge_case_empty_function_body_still_records(self):
        @timeit
        def noop():
            return None

        self.assertIsNone(noop())
        self.assertIsInstance(noop.last_elapsed, float)
        self.assertGreaterEqual(noop.last_elapsed, 0.0)
        self.assertEqual(len(noop.records), 1)

    def test_decorator_does_not_call_print(self):
        @timeit
        def sample():
            return 42

        with patch("builtins.print") as mock_print:
            self.assertEqual(sample(), 42)

        mock_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()
