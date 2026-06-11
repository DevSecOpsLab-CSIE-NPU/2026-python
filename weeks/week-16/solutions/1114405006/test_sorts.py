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

# from sorts import bubble_sort, quick_sort, merge_sort  # 完成 sorts.py 後解除註解

# 三個排序函式都放進這個 list,每個測試用 subTest 跑一輪;
# Stage 3 的加速版 append 進來就能吃到同一組測試。


def _not_implemented(data):
    raise NotImplementedError("sorts.py not yet implemented")


SORT_FUNCTIONS = [_not_implemented]  # 實作後換成 [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def _run_on_all(self, data):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                result = sort_fn(data)
                self.assertEqual(result, sorted(data))

    def test_sorted_elements(self):
        self._run_on_all([1, 2, 3, 4, 5])

    def test_reversed_elements(self):
        self._run_on_all([5, 4, 3, 2, 1])

    def test_random_data_matches_builtin(self):
        import random
        data = [random.randint(-100, 100) for _ in range(50)]
        self._run_on_all(data)

    def test_all_same(self):
        self._run_on_all([7, 7, 7, 7, 7])

    def test_single_element(self):
        self._run_on_all([42])

    def test_negative_numbers(self):
        self._run_on_all([-5, 3, -10, 0, 8, -1])

    def test_float_values(self):
        self._run_on_all([3.14, 1.41, 2.72, 0.0, -1.5])

    def test_empty_list_raises(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                with self.assertRaises(ValueError):
                    sort_fn([])

    def test_input_not_mutated(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                original = [3, 1, 2]
                copy_before = original[:]
                sort_fn(original)
                self.assertEqual(original, copy_before)


if __name__ == "__main__":
    unittest.main()
