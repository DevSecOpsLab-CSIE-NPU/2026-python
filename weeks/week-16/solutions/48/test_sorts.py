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

from sorts import bubble_sort, merge_sort, quick_sort

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def _check_sorted(self, sort_func, original, expected=None):
        if expected is None:
            expected = sorted(original)
        result = sort_func(original)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [])

    def test_single_element(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [42])

    def test_two_elements(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [2, 1])

    def test_sorted_input(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [1, 2, 3, 4, 5])

    def test_reverse_input(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [5, 4, 3, 2, 1])

    def test_all_equal(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [7, 7, 7, 7])

    def test_with_duplicates(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [3, 1, 3, 2, 1])

    def test_negative_and_zero(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, [-5, 0, -1, 10])

    def test_random_data_matches_builtin(self):
        import random
        random.seed(42)
        data = [random.randint(-1000, 1000) for _ in range(200)]
        expected = sorted(data)
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                self._check_sorted(sort_func, data, expected)

    def test_input_not_mutated(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                original = [3, 1, 4, 1, 5]
                before = original[:]
                sort_func(original)
                self.assertEqual(original, before)

    def test_not_using_builtin_sorted(self):
        import ast
        import inspect
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort=sort_func.__name__):
                source = inspect.getsource(sort_func)
                tree = ast.parse(source)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        if isinstance(node.func, ast.Name) and node.func.id == "sorted":
                            self.fail(f"{sort_func.__name__} 使用了 sorted()")
                        if isinstance(node.func, ast.Attribute) and node.func.attr == "sort":
                            self.fail(f"{sort_func.__name__} 使用了 .sort()")


if __name__ == "__main__":
    unittest.main()
