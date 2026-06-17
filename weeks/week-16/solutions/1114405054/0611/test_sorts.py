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
from sorts import bubble_sort, quick_sort, merge_sort


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 1, 1], [1, 1, 1]),
            ([5, 1, 4, 2, 3], [1, 2, 3, 4, 5]),
            ([-3, -1, -2, 0, 2, 1], [-3, -2, -1, 0, 1, 2]),
        ]
        for sort_fn in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort=sort_fn.__name__, data=data):
                    self.assertEqual(sort_fn(data), expected)

    def test_random_data_matches_builtin(self):
        import random
        random.seed(42)
        for _ in range(5):
            data = random.sample(range(-1000, 1000), 200)
            expected = sorted(data)
            for sort_fn in SORT_FUNCTIONS:
                with self.subTest(sort=sort_fn.__name__):
                    self.assertEqual(sort_fn(data), expected)

    def test_input_not_mutated(self):
        for sort_fn in SORT_FUNCTIONS:
            original = [3, 1, 4, 1, 5, 9, 2, 6]
            copy_before = original[:]
            result = sort_fn(original)
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(original, copy_before)
                self.assertIsNot(result, original)


if __name__ == "__main__":
    unittest.main()
