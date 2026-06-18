"""Stage 1 — @timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時(float 秒)append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不准 print
  6. repeat < 1 → raise ValueError(用 raise,不准 assert)

AI 反問紀錄：
  Q: f.records 應存什麼值？
  A: 選項 A — 每一次重複的個別耗時都 append 進去

待辦:
  1. ✅ 用戶確認規格
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest
import time

# from timing import timeit  # 完成後解除註解


class TestTimeit(unittest.TestCase):
    """@timeit 裝飾器測試，≥3 個 test case 含 ≥1 edge case"""

    def test_returns_original_result(self):
        """Normal case：正常使用預設 repeat=3，驗證回傳值不變"""
        @timeit
        def sample_func(x, y):
            return x + y

        result = sample_func(2, 3)
        self.assertEqual(result, 5, "回傳值應不變")

    def test_records_individual_timings_default_repeat(self):
        """Normal case：預設 repeat=3，f.records 應有 3 個耗時值"""
        @timeit
        def slow_func():
            time.sleep(0.01)

        slow_func()
        self.assertEqual(
            len(slow_func.records),
            3,
            "預設 repeat=3，records 應有 3 筆耗時"
        )
        self.assertTrue(
            all(isinstance(t, float) for t in slow_func.records),
            "records 內應全為 float（秒數）"
        )

    def test_last_elapsed_is_average(self):
        """Normal case：驗證 f.last_elapsed = 本次 repeat 的平均耗時"""
        @timeit
        def quick_func():
            return "done"

        quick_func(repeat=2)
        avg_expected = sum(quick_func.records) / len(quick_func.records)
        self.assertAlmostEqual(
            quick_func.last_elapsed,
            avg_expected,
            places=6,
            msg="last_elapsed 應等於本次平均耗時"
        )

    def test_repeat_one_edge_case(self):
        """Edge case 1：repeat=1（最小有效值），records 應有 1 筆"""
        @timeit
        def func_one():
            return "x"

        func_one(repeat=1)
        self.assertEqual(len(func_one.records), 1, "repeat=1 時 records 應有 1 筆")
        self.assertEqual(func_one.last_elapsed, func_one.records[0],
                         "repeat=1 時平均 = 唯一的耗時")

    def test_repeat_zero_raises_valueerror(self):
        """Edge case 2：repeat=0 應拋 ValueError"""
        @timeit
        def func_zero():
            pass

        with self.assertRaises(ValueError):
            func_zero(repeat=0)

    def test_repeat_negative_raises_valueerror(self):
        """Edge case 3：repeat=-1 應拋 ValueError"""
        @timeit
        def func_neg():
            pass

        with self.assertRaises(ValueError):
            func_neg(repeat=-1)

    def test_preserves_function_metadata(self):
        """驗證 functools.wraps 保留 __name__ 和 __doc__"""
        @timeit
        def documented_func():
            """This is a test function."""
            return 42

        self.assertEqual(documented_func.__name__, "documented_func",
                         "__name__ 應被保留")
        self.assertEqual(documented_func.__doc__, "This is a test function.",
                         "__doc__ 應被保留")


if __name__ == "__main__":
    unittest.main()
