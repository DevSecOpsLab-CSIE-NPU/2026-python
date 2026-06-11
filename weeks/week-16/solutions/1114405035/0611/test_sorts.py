"""Stage 2 — 排序正確性測試骨架

規格:sorts.py 的 bubble_sort / quick_sort / merge_sort 必須
  1. 回傳新的排序後 list,不可修改傳入的 list
  2. 禁用內建 sorted() / list.sort()(那是 Stage 3 的對照組;
     測試裡拿 sorted() 當驗證標準則可以)

設計要求:三個函式共用同一組測試——用迴圈 + subTest,不要複製貼上三份。

待辦:
  1. 自己打提示詞跟 AI 討論,補齊測試——一般案例、edge case、
     「不可修改傳入 list」都要覆蓋;AI 給的齊不齊,自己驗收
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage2 排序正確性測試"
  4. 寫 sorts.py,全綠後 commit: "feat: stage2 實作三種排序與 benchmark"
"""

import unittest
import random
from sorts import bubble_sort, quick_sort, merge_sort, quick_sort_optimized

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort, quick_sort_optimized]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        # 測試基本與邊緣情況：空 list、單一元素、已排序、反向排序、重複元素
        cases = [
            ([], []),
            ([42], [42]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
            ([5, 5, 5, 5], [5, 5, 5, 5]),
        ]
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                for inp, expected in cases:
                    with self.subTest(case=inp):
                        self.assertEqual(sort_fn(inp), expected)

    def test_random_data_matches_builtin(self):
        # 隨機數測試對照組
        random.seed(42)
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                for size in [10, 50, 100]:
                    data = [random.randint(-1000, 1000) for _ in range(size)]
                    expected = sorted(data)
                    self.assertEqual(sort_fn(data), expected)

    def test_input_not_mutated(self):
        # 驗證輸入的原 list 沒有被修改
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                original = [3, 1, 2]
                copy_of_original = list(original)
                _ = sort_fn(original)
                self.assertEqual(original, copy_of_original, f"{sort_fn.__name__} mutated the input list!")

    def test_invalid_inputs(self):
        # 驗證例外行為：傳入 None 或非 list 型態應拋出 TypeError
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                with self.assertRaises(TypeError):
                    sort_fn(None)
                with self.assertRaises(TypeError):
                    sort_fn("not a list")
                with self.assertRaises(TypeError):
                    sort_fn({"key": "val"})


if __name__ == "__main__":
    unittest.main()

