"""0617 任務一 — timeit 裝飾器完整測試

涵蓋規格：
  1. 回傳值不變
  2. functools.wraps 保留 __name__ / __doc__
  3. records 累積、last_elapsed = 平均耗時
  4. 裝飾器內不 print（無法直接驗證，但結構上保證）
  5. repeat < 1 → raise ValueError（安全測試，用 raise 不用 assert）

Edge case：
  - repeat=1：records 長度正確，last_elapsed 即單次耗時
  - 有副作用的函式：repeat=3 時副作用被多算 3 次（已記錄在文件）
  - 多次呼叫：records 累積、last_elapsed 只反映最後一次呼叫
"""

import unittest
import time
from timing import timeit


# ── 被測試用的輔助函式 ──────────────────────────────────────────────

@timeit
def add(a, b):
    """把兩個數字相加。"""
    return a + b


@timeit(repeat=1)
def slow_fn():
    """刻意稍微 sleep 的函式，方便量測非零耗時。"""
    time.sleep(0.01)
    return 42


# ── 測試類別 ────────────────────────────────────────────────────────

class TestTimeit(unittest.TestCase):

    # 每個 test method 開始前，重設 records 避免互相污染
    def setUp(self):
        add.records.clear()
        add.last_elapsed = 0.0
        slow_fn.records.clear()
        slow_fn.last_elapsed = 0.0

    # ── 規格 1：回傳值不變 ──────────────────────────────────────────
    def test_returns_original_result(self):
        """被裝飾函式的回傳值必須完全不變。"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add("hello", " world"), "hello world")

    # ── 規格 2：保留 metadata ───────────────────────────────────────
    def test_preserves_function_metadata(self):
        """functools.wraps 需保留 __name__ 與 __doc__。"""
        self.assertEqual(add.__name__, "add")
        self.assertIn("相加", add.__doc__)

    # ── 規格 3a：records 累積每次 repeat 的耗時 ────────────────────
    def test_records_appended_per_call(self):
        """每次呼叫後，records 長度增加 repeat 筆（預設 3）。"""
        add(1, 2)
        self.assertEqual(len(add.records), 3)
        add(1, 2)
        self.assertEqual(len(add.records), 6)  # 第二次呼叫再加 3

    # ── 規格 3b：last_elapsed = 平均耗時 ───────────────────────────
    def test_last_elapsed_is_average(self):
        """last_elapsed 必須等於本次 repeat 的耗時平均值。"""
        slow_fn()  # repeat=1
        self.assertAlmostEqual(slow_fn.last_elapsed, slow_fn.records[-1], places=9)
        # last_elapsed ≈ 0.01s（sleep）
        self.assertGreater(slow_fn.last_elapsed, 0.005)

    # ── 規格 3c：last_elapsed 只反映最後一次呼叫 ───────────────────
    def test_last_elapsed_reflects_latest_call(self):
        """多次呼叫後，last_elapsed 只反映最新一次，records 持續累積。"""
        add(0, 0)
        add(0, 0)
        # last_elapsed 可能不同（OS jitter），但 records 要有 6 筆
        self.assertEqual(len(add.records), 6)
        self.assertGreaterEqual(add.last_elapsed, 0.0)

    # ── 規格 5（安全測試）：repeat < 1 → raise ValueError ──────────
    def test_rejects_invalid_repeat_zero(self):
        """repeat=0 必須 raise ValueError，不能 assert（assert 在 -O 模式消失）。"""
        with self.assertRaises(ValueError):
            timeit(repeat=0)(lambda: None)

    def test_rejects_invalid_repeat_negative(self):
        """repeat=-1 同樣必須 raise ValueError。"""
        with self.assertRaises(ValueError):
            timeit(repeat=-1)(lambda: None)

    # ── Edge case：repeat=1 ─────────────────────────────────────────
    def test_repeat_one(self):
        """repeat=1 時 records 每次呼叫只加 1 筆，last_elapsed = 那筆耗時。"""
        slow_fn()
        self.assertEqual(len(slow_fn.records), 1)
        self.assertAlmostEqual(slow_fn.last_elapsed, slow_fn.records[0], places=9)

    # ── Edge case：有副作用的函式 ──────────────────────────────────
    def test_side_effects_run_repeat_times(self):
        """有副作用的函式在 repeat=3 時，副作用確實執行 3 次（這是預期行為，文件已說明）。"""
        counter = {"n": 0}

        @timeit  # repeat=3
        def inc():
            counter["n"] += 1
            return counter["n"]

        result = inc()
        # 被呼叫 3 次，副作用執行 3 次；回傳值是最後一次執行的結果
        self.assertEqual(counter["n"], 3)
        self.assertEqual(result, 3)
        self.assertEqual(len(inc.records), 3)

    # ── records 每次耗時均為非負數 ─────────────────────────────────
    def test_all_records_are_non_negative(self):
        """records 裡的每個耗時都應 >= 0。"""
        add(10, 20)
        for t in add.records:
            self.assertGreaterEqual(t, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
