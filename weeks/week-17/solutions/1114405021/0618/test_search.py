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

from search import linear_search, binary_search, set_search

# 三個搜尋函式都放進這個 list,每個測試用 subTest 跑一輪;
# 注意回傳型別不一致,subTest 內要先轉成共同判準再比較。
SEARCH_FUNCTIONS = [linear_search, binary_search, set_search]


class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        test_data = [
            ([1, 2, 3, 4, 5], 3, True),  # 線性搜尋找到 (index 2)
            ([1, 2, 3, 4, 5], 6, False),  # 線性搜尋找不到
            ([], 1, False),  # 空列表
            ([5], 5, True),  # 單元素列表
            ([1, 3, 5, 7, 9], 5, True),  # 奇數序列
        ]

        for data, target, expected_found in test_data:
            for search_func in SEARCH_FUNCTIONS:
                with self.subTest(data=data, target=target, search_func=search_func):
                    result = search_func(data, target)
                    found = (
                        (result != -1)
                        if search_func in [linear_search, binary_search]
                        else result
                    )
                    self.assertEqual(found, expected_found)

    def test_not_found_cases(self):
        test_data = [
            ([10, 20, 30, 40], 15),  # 不存在的目標
            ([], 999),  # 空列表
            ([5], 3),  # 單元素列表，目標不存在
        ]

        for data, target in test_data:
            for search_func in SEARCH_FUNCTIONS:
                with self.subTest(data=data, target=target, search_func=search_func):
                    result = search_func(data, target)
                    found = (
                        (result != -1)
                        if search_func in [linear_search, binary_search]
                        else result
                    )
                    self.assertFalse(found)

    def test_input_not_mutated(self):
        original_data = [1, 3, 5, 7, 9]
        # 創建一個副本，驗證輸入不會被修改
        for search_func in SEARCH_FUNCTIONS:
            with self.subTest(search_func=search_func):
                data_copy = original_data.copy()
                result = search_func(data_copy, 5)
                # 驗證輸入數據是否被修改
                self.assertEqual(data_copy, original_data)


if __name__ == "__main__":
    unittest.main()
