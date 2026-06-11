"""Stage 1 — @timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫後更新 f.last_elapsed(float 秒)並 append 到 f.records
  4. 裝飾器內不准 print

TDD 流程:
  - 此時 timing.py 尚未建立 → 全紅
  - commit: "test: stage1 timeit 裝飾器測試"
  - 實作 timing.py 後全綠 → commit: "feat: stage1 實作 timeit 裝飾器"
"""

import io
import sys
import time
import unittest

from timing import timeit  # timing.py 尚未建立,故此處會 ImportError → 全紅


class TestTimeit(unittest.TestCase):
    # ── 測試 1:回傳值不變 ──────────────────────────────────────────────────
    def test_returns_original_result(self):
        """被裝飾函式的回傳值必須與原本完全相同。"""
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add("hello", " world"), "hello world")

        @timeit
        def do_nothing():
            return None

        self.assertIsNone(do_nothing())

    # ── 測試 2:functools.wraps 保留 metadata ──────────────────────────────
    def test_preserves_function_metadata(self):
        """裝飾後 __name__ 與 __doc__ 必須與原函式相同。"""
        @timeit
        def my_func():
            """這是說明文件。"""
            pass

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "這是說明文件。")

    # ── 測試 3:last_elapsed 是正數 float ─────────────────────────────────
    def test_last_elapsed_is_positive_float(self):
        """每次呼叫後 last_elapsed 必須是正數 float(單位:秒)。"""
        @timeit
        def slow():
            time.sleep(0.01)

        slow()
        self.assertIsInstance(slow.last_elapsed, float)
        self.assertGreater(slow.last_elapsed, 0)

    # ── 測試 4:records 隨呼叫次數累積 ────────────────────────────────────
    def test_records_accumulates_across_calls(self):
        """每次呼叫都應 append 一筆 float 到 records,且 last_elapsed == records[-1]。"""
        @timeit
        def noop():
            pass

        self.assertEqual(noop.records, [])
        noop()
        self.assertEqual(len(noop.records), 1)
        noop()
        noop()
        self.assertEqual(len(noop.records), 3)
        self.assertEqual(noop.last_elapsed, noop.records[-1])

    # ── 測試 5:裝飾器不可 print ───────────────────────────────────────────
    def test_no_stdout_output(self):
        """timeit 裝飾器本身不可輸出任何內容到 stdout。"""
        @timeit
        def silent():
            return 42

        captured = io.StringIO()
        sys.stdout = captured
        try:
            silent()
        finally:
            sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
