"""Stage 2 — 搜尋正確性測試

規格:search.py 的 linear_search / binary_search / set_search 必須
  1. 一律不可修改傳入的 data
  2. 回傳型別不一致：
       - linear_search(data, target) -> int   找到回 index,找不到回 -1
       - binary_search(data, target) -> int   找到回 index,找不到回 -1
       - set_search(data, target)    -> bool  回傳是否存在
  3. binary_search 前提為 data 已排序。若傳入未排序 data，為保持 O(log n)
     效能，本實作不做排序驗證，不保證其正確性（可能找不到而回傳 -1）。
"""

import unittest
from search import (
    linear_search,
    binary_search,
    set_search,
    linear_search_builtin,
    binary_search_bisect,
    set_search_optimized,
)

# 將所有搜尋函式放進 list，包含基線與優化版，用同一套正確性測試驗收
SEARCH_FUNCTIONS = [
    linear_search,
    binary_search,
    set_search,
    linear_search_builtin,
    binary_search_bisect,
    set_search_optimized,
]


class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        """測試 1: 正常找到目標時的情況"""
        # data 為已排序數列
        data = [1, 3, 5, 7, 9, 11]
        
        # 測試目標與其對應的 index
        test_cases = [
            (1, 0),   # 極左邊界
            (7, 3),   # 中間
            (11, 5),  # 極右邊界
        ]

        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                for target, expected_idx in test_cases:
                    res = func(data, target)
                    if "set" in func.__name__:
                        self.assertIs(res, True, f"{func.__name__} 找不到存在的 {target}")
                    else:
                        # 由於可能有重複值（雖然此例無），我們驗證該位置的值是否確實為 target
                        self.assertEqual(data[res], target, f"{func.__name__} 回傳的 index {res} 對應值不為 {target}")

    def test_not_found_cases(self):
        """測試 2: 找不到目標時的情況"""
        data = [1, 3, 5, 7, 9, 11]
        targets = [0, 4, 12]  # 小於最小值、中間不存在的值、大於最大值

        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                for target in targets:
                    res = func(data, target)
                    if "set" in func.__name__:
                        self.assertIs(res, False, f"{func.__name__} 誤報不存在的 {target}")
                    else:
                        self.assertEqual(res, -1, f"{func.__name__} 找不到應回傳 -1")

    def test_empty_input(self):
        """測試 3: Edge Case — 輸入空 list"""
        data = []
        target = 5

        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                res = func(data, target)
                if "set" in func.__name__:
                    self.assertIs(res, False, f"空 list 時 {func.__name__} 應回傳 False")
                else:
                    self.assertEqual(res, -1, f"空 list 時 {func.__name__} 應回傳 -1")

    def test_input_not_mutated(self):
        """測試 4: 一律不可修改/污染傳入的原始 data"""
        original_data = [5, 3, 9, 1, 7]
        # 複製一份做對比
        data_copy = original_data.copy()
        target = 9

        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                # 測試 search 是否會修改傳入的 data
                func(data_copy, target)
                self.assertEqual(data_copy, original_data, f"{func.__name__} 修改了原始傳入的 data")

    def test_binary_search_unsorted_data(self):
        """測試 5: binary_search 收到未排序 data 的特定預期行為
        依據設計規格，未排序時 binary_search 為了不退化效能，不做內部排序。
        在此我們特定設計一組測試，當二分搜尋在未排序數列中搜尋時，可能因搜尋區間錯亂而返回 -1。
        """
        # 未排序資料中搜尋 3 （其實 3 存在於 index 0）
        unsorted_data = [3, 1, 2]
        res = binary_search(unsorted_data, 3)
        # 應為 -1（因其沒有經過排序，照二分搜尋邏輯會搜尋失敗）
        self.assertEqual(res, -1, "未排序資料進行 binary_search 應搜尋失敗返回 -1")


if __name__ == "__main__":
    unittest.main()
