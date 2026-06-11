"""Stage 2 — 排序正確性測試

規格:sorts.py 的 bubble_sort / quick_sort / merge_sort 必須
  1. 回傳新的排序後 list,不可修改傳入的 list
  2. 禁用內建 sorted() / list.sort()(測試中用 sorted() 當驗證標準則可以)

設計:三個函式共用同一組測試——用迴圈 + subTest,不複製貼上三份。

TDD 流程:
  - 此時 sorts.py 尚未建立 → 全紅
  - commit: "test: stage2 排序正確性測試"
  - 實作 sorts.py 後全綠 → commit: "feat: stage2 實作三種排序與 benchmark"
"""

import random
import unittest

from sorts import bubble_sort, quick_sort, merge_sort  # sorts.py 尚未建立 → 全紅

# Stage 3 的加速版 append 進來就能吃到同一組測試
SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    # ── 測試 1:一般正整數清單 ──────────────────────────────────────────────
    def test_basic_cases(self):
        """一般正整數清單,三個函式皆應回傳正確排序結果。"""
        data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
        expected = sorted(data)
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn(data), expected)

    # ── 測試 2:隨機資料與內建 sorted() 比對 ──────────────────────────────
    def test_random_data_matches_builtin(self):
        """隨機產生的清單,結果必須與 sorted() 完全一致(fixed seed 可重現)。"""
        rng = random.Random(42)
        for _ in range(5):
            data = [rng.randint(-100, 100) for _ in range(50)]
            for fn in SORT_FUNCTIONS:
                with self.subTest(fn=fn.__name__):
                    self.assertEqual(fn(data), sorted(data))

    # ── 測試 3:傳入的 list 不可被修改 ────────────────────────────────────
    def test_input_not_mutated(self):
        """排序後原始 list 的內容與順序必須與呼叫前完全相同。"""
        original = [4, 2, 7, 1, 5]
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                copy_before = original[:]
                fn(original)
                self.assertEqual(original, copy_before)

    # ── 測試 4:空 list ─────────────────────────────────────────────────────
    def test_edge_case_empty_list(self):
        """空 list 應回傳空 list。"""
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn([]), [])

    # ── 測試 5:單一元素 ────────────────────────────────────────────────────
    def test_edge_case_single_element(self):
        """單一元素的 list 應直接回傳該元素。"""
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn([42]), [42])

    # ── 測試 6:含重複元素 ──────────────────────────────────────────────────
    def test_edge_case_duplicates(self):
        """含重複元素的 list,結果必須與 sorted() 一致。"""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn(data), sorted(data))

    # ── 測試 7:逆序(bubble sort 最壞情況) ──────────────────────────────
    def test_edge_case_reverse_sorted(self):
        """完全逆序的 list,仍必須正確排序。"""
        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn(data), sorted(data))


if __name__ == "__main__":
    unittest.main()
