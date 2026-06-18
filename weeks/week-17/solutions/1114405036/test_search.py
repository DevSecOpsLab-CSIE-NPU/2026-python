
"""Stage 2 — 搜尋正確性測試。
 
三個搜尋函式共用一組測試（迴圈 + subTest），但因回傳型別不一致，先在
subTest 內把結果轉成共同基準（found: bool）再比對：
  - linear_search / binary_search：找到 → index >= 0
  - set_search：找到 → True
 
binary_search 的前提是 data 已排序，故測試一律使用已排序的 data。
"""
 
import unittest
 
from benchmark import bisect_search, builtin_in
from search import binary_search, linear_search, set_search
 
# 回傳 bool 的函式（其餘回傳 index）
_BOOL_FUNCS = {set_search, builtin_in}
 
 
def _found(func, result) -> bool:
    """把不同回傳型別正規化成「是否找到」。"""
    if func in _BOOL_FUNCS:
        return result is True
    return result >= 0
 
 
# Stage 2 三搜 + Stage 3 加速版 baseline 共用同一組正確性測試
SEARCH_FUNCTIONS = [
    linear_search,
    binary_search,
    set_search,
    builtin_in,
    bisect_search,
]
 
 
class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        data = [1, 3, 5, 7, 9, 11]
        for func in SEARCH_FUNCTIONS:
            for target in (1, 7, 11):
                with self.subTest(func=func.__name__, target=target):
                    self.assertTrue(_found(func, func(data, target)))
 
    def test_not_found_cases(self):
        data = [1, 3, 5, 7, 9, 11]
        for func in SEARCH_FUNCTIONS:
            for target in (0, 4, 99):
                with self.subTest(func=func.__name__, target=target):
                    self.assertFalse(_found(func, func(data, target)))
 
    def test_empty_data(self):
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                self.assertFalse(_found(func, func([], 1)))
 
    def test_input_not_mutated(self):
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                data = [1, 2, 3, 4, 5]
                snapshot = list(data)
                func(data, 3)
                self.assertEqual(data, snapshot)
 
 
class TestIndexSearchSpecifics(unittest.TestCase):
    """linear / binary 回傳的是 index，這裡額外驗證 index 正確。"""
 
    def test_linear_returns_first_match(self):
        self.assertEqual(linear_search([4, 7, 7, 4], 7), 1)
 
    def test_linear_returns_index(self):
        self.assertEqual(linear_search([5, 3, 9, 1], 9), 2)
 
    def test_binary_returns_index(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 7), 3)
 
    def test_binary_first_and_last(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 9), 4)
 
    def test_not_found_returns_minus_one(self):
        self.assertEqual(linear_search([1, 2, 3], 99), -1)
        self.assertEqual(binary_search([1, 2, 3], 99), -1)
 
 
if __name__ == "__main__":
    unittest.main()