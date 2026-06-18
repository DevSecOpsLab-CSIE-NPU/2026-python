"""Stage 2 — 搜尋正確性測試骨架

規格:search.py 的 linear_search / binary_search / set_search 必須
  1. 一律不可修改傳入的 data(測試要驗)
  2. 回傳型別「不一致」,共用測試時要小心:
       - linear_search(data, target) -> int   找到回 index,找不到回 -1
       - binary_search(data, target) -> int   找到回 index,找不到回 -1
       - set_search(data, target)    -> bool  回傳是否存在
  3. binary_search 的前提是 data 已排序;收到未排序 data 的行為,
     自己定義並在 docstring 寫清楚,測試也要對得上你的定義

設計要求:三個函式共用同一組測試——用迴圈 + subTest,不要複製貼上三份。
  因為回傳型別不同,subTest 裡要把「找到/找不到」轉成可比較的共同判準
  (例:linear/binary 看 index 是否 >= 0,set 看 bool)——怎麼轉自己想。

待辦:
  1. 自己打提示詞跟 AI 討論,補齊測試——一般案例、edge case(空 list?重複值?
     目標不存在?)、「不可修改傳入 data」都要覆蓋;AI 給的齊不齊,自己驗收
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage2 搜尋正確性測試"
  4. 寫 search.py,全綠後 commit: "feat: stage2 實作三種搜尋"
"""

import unittest

from search import (
    linear_search, binary_search, set_search,
    builtin_linear_search, builtin_binary_search
)

SEARCH_FUNCTIONS = [
    linear_search, binary_search, set_search,
    builtin_linear_search, builtin_binary_search
]


class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        data = [1, 3, 5, 7, 9]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "set_search":
                    self.assertTrue(func(data, 5))
                    self.assertTrue(func(data, 1))
                    self.assertTrue(func(data, 9))
                else:
                    self.assertEqual(func(data, 5), 2)
                    self.assertEqual(func(data, 1), 0)
                    self.assertEqual(func(data, 9), 4)

    def test_not_found_cases(self):
        data = [1, 3, 5, 7, 9]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "set_search":
                    self.assertFalse(func(data, 0))
                    self.assertFalse(func(data, 6))
                    self.assertFalse(func(data, 10))
                    self.assertFalse(func([], 5))
                else:
                    self.assertEqual(func(data, 0), -1)
                    self.assertEqual(func(data, 6), -1)
                    self.assertEqual(func(data, 10), -1)
                    self.assertEqual(func([], 5), -1)

    def test_duplicates(self):
        dup_data = [1, 2, 2, 3]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "set_search":
                    self.assertTrue(func(dup_data, 2))
                elif func.__name__ == "linear_search":
                    self.assertEqual(func(dup_data, 2), 1)  # 必須是第一個
                elif func.__name__ == "binary_search":
                    res = func(dup_data, 2)
                    self.assertIn(res, [1, 2])  # 可以是任一符合的索引

    def test_input_not_mutated(self):
        sorted_data = [1, 3, 5, 9]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                test_data = sorted_data.copy()
                func(test_data, 5)
                self.assertEqual(test_data, sorted_data)

                test_data = sorted_data.copy()
                func(test_data, 100)
                self.assertEqual(test_data, sorted_data)

    def test_invalid_input_type(self):
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                with self.assertRaises(TypeError):
                    func("not a list", 5)


if __name__ == "__main__":
    unittest.main()
