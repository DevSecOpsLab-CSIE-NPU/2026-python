"""Stage 2 — 排序正確性測試

規格:sorts.py 的 bubble_sort / quick_sort / merge_sort 必須
  1. 回傳新的排序後 list,不可修改傳入的 list
  2. 禁用內建 sorted() / list.sort()(那是 Stage 3 的對照組;
     測試裡拿 sorted() 當驗證標準則可以)

設計要求:三個函式共用同一組測試——用迴圈 + subTest,不要複製貼上三份。

AI 提示詞:
- 需要測試排序演算法是否正確地對列表進行排序
- 需要驗證排序演算法不會修改輸入列表
- 需要測試各種輸入情況：空列表、單元素列表、已排序列表、逆序列表、重複元素
"""

import unittest
import random
from sorts import bubble_sort, quick_sort, merge_sort

# 三個排序函式都放進這個 list,每個測試用 subTest 跑一輪;
# Stage 3 的加速版 append 進來就能吃到同一組測試。
SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        """測試基本排序案例"""
        test_cases = [
            [],
            [1],
            [1, 2, 3],
            [3, 2, 1],
            [5, 2, 8, 1, 9],
            [2, 2, 2, 2],
            [-1, 0, 1],
            [10, -5, 0, 15, -10]
        ]
        
        for sort_func in SORT_FUNCTIONS:
            for test_case in test_cases:
                with self.subTest(sort_func=sort_func.__name__, test_case=test_case):
                    result = sort_func(test_case)
                    expected = sorted(test_case)
                    self.assertEqual(result, expected)

    def test_random_data_matches_builtin(self):
        """測試隨機數據是否與內建 sorted 結果一致"""
        random.seed(42)
        test_cases = [
            [random.randint(-100, 100) for _ in range(10)],
            [random.randint(-100, 100) for _ in range(50)],
            [random.randint(-100, 100) for _ in range(100)]
        ]
        
        for sort_func in SORT_FUNCTIONS:
            for test_case in test_cases:
                with self.subTest(sort_func=sort_func.__name__, test_case=test_case):
                    result = sort_func(test_case)
                    expected = sorted(test_case)
                    self.assertEqual(result, expected)

    def test_input_not_mutated(self):
        """測試排序演算法不會修改輸入列表"""
        test_cases = [
            [3, 1, 4, 1, 5],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5],
            [2, 2, 1, 1]
        ]
        
        for sort_func in SORT_FUNCTIONS:
            for test_case in test_cases:
                original = test_case.copy()
                with self.subTest(sort_func=sort_func.__name__, test_case=test_case):
                    result = sort_func(test_case)
                    self.assertEqual(test_case, original)
                    self.assertEqual(result, sorted(original))


if __name__ == "__main__":
    unittest.main()
