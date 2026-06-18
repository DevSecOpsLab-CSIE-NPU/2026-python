import unittest
from sorts import bubble_sort, quick_sort, merge_sort

class TestSorts(unittest.TestCase):
    def setUp(self):
        self.sort_funcs = [bubble_sort, quick_sort, merge_sort]
        self.test_data = [
            ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([2, 2, 2], [2, 2, 2])
        ]

    def test_correctness_and_side_effects(self):
        for sort_func in self.sort_funcs:
            for data, expected in self.test_data:
                with self.subTest(sort=sort_func.__name__, data=data):
                    original = list(data)
                    result = sort_func(data)
                    # 驗證結果正確
                    self.assertEqual(result, expected)
                    # 驗證無副作用 (原 list 未被修改)
                    self.assertEqual(data, original)
                    # 驗證回傳的是新 list (除非是空的或特殊處理，通常要求 id 不同)
                    if data:
                        self.assertIsNot(result, data)

if __name__ == "__main__":
    unittest.main()

