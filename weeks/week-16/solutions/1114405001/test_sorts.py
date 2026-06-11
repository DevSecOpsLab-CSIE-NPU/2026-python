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
from sorts_fast import quick_sort_optimized

# 三個排序函式都放進這個 list,每個測試用 subTest 跑一輪;
# Stage 3 的加速版 append 進來就能吃到同一組測試。
SORT_FUNCTIONS = []  # 解除上面 import 後填入
SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort, quick_sort_optimized]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [],
            [1],
            [2, 1],
            [3, 1, 2],
            [5, 5, 1, 3, 3],
            [-3, 7, 0, -1, 7],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
        ]
        for sort_func in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_random_data_matches_builtin(self):
        rng = random.Random(42)
        for sort_func in SORT_FUNCTIONS:
            for _ in range(20):
                size = rng.randint(0, 60)
                data = [rng.randint(-1000, 1000) for _ in range(size)]
                with self.subTest(sort=sort_func.__name__, size=size):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_input_not_mutated(self):
        for sort_func in SORT_FUNCTIONS:
            data = [4, 1, 3, 2, 2]
            snapshot = list(data)
            result = sort_func(data)
            with self.subTest(sort=sort_func.__name__):
                self.assertEqual(data, snapshot)
                self.assertIsNot(result, data)


if __name__ == "__main__":
    unittest.main()
