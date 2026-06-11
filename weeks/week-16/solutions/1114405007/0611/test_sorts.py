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

from sorts import bubble_sort, quick_sort, merge_sort

# 三個排序函式都放進這個 list,每個測試用 subTest 跑一輪;
# Stage 3 的加速版 append 進來就能吃到同一組測試。
SORT_FUNCTIONS = [
    ("bubble_sort", bubble_sort),
    ("quick_sort", quick_sort),
    ("merge_sort", merge_sort),
]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            ([5, 1, 4, 2, 8, 5], [1, 2, 4, 5, 5, 8]),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([], []),
            ([42], [42]),
        ]
        for name, sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort=name, data=data):
                    self.assertEqual(sort_func(data), expected)

    def test_random_data_matches_builtin(self):
        rng = random.Random(123)
        data = [rng.randint(-100, 100) for _ in range(100)]
        expected = sorted(data)

        for name, sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=name):
                self.assertEqual(sort_func(data), expected)

    def test_input_not_mutated(self):
        for name, sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=name):
                original = [3, 1, 2, 1]
                snapshot = original.copy()
                result = sort_func(original)
                self.assertEqual(original, snapshot)
                self.assertIsNot(result, original)


if __name__ == "__main__":
    unittest.main()
