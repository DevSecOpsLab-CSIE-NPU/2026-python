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

# 我們在測試階段先定義 mock function 或者直接 import（會引發 ModuleNotFoundError 達成紅燈）
from sorts import bubble_sort, quick_sort, merge_sort  

# 三個排序函式都放進這個 list,每個測試用 subTest 跑一輪;
# Stage 3 的加速版 append 進來就能吃到同一組測試。
SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]  


class TestSortFunctions(unittest.TestCase):
    def test_basic_and_edge_cases(self):
        """測試一般情境與邊界條件 (空 list、單一元素、已排序、反向、重複元素)"""
        cases = {
            "empty": [],
            "single": [42],
            "sorted": [1, 2, 3, 4, 5],
            "reversed": [5, 4, 3, 2, 1],
            "duplicates": [3, 1, 4, 1, 5, 9, 2, 6, 5],
            "negative": [-5, 3, -1, 0, 8, -2],
        }
        
        for sort_func in SORT_FUNCTIONS:
            for name, data in cases.items():
                with self.subTest(func=sort_func.__name__, case=name):
                    expected = sorted(data)
                    result = sort_func(data)
                    self.assertEqual(result, expected)

    def test_random_data_matches_builtin(self):
        """測試較大的隨機陣列是否與內建 sorted 結果一致"""
        random.seed(42)  # 固定 seed 確保測試可重現
        data = [random.randint(-100, 100) for _ in range(100)]
        expected = sorted(data)
        
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(func=sort_func.__name__):
                result = sort_func(data)
                self.assertEqual(result, expected)

    def test_input_not_mutated(self):
        """測試必須回傳新的 list，且原本傳入的 list 內容不被修改"""
        original_data = [3, 1, 4, 1, 5, 9]
        original_copy = list(original_data) # 深拷貝備份
        
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(func=sort_func.__name__):
                # 傳入 original_data 的一份拷貝，確保不會因為上一個函式改到而影響下一個
                test_input = list(original_data)
                result = sort_func(test_input)
                
                # 確認回傳的是新物件
                self.assertIsNot(result, test_input)
                # 確認原本的 test_input 沒被改到
                self.assertEqual(test_input, original_copy)


if __name__ == "__main__":
    unittest.main()
