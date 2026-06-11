import unittest
import random
from sorts import bubble_sort, quick_sort, merge_sort


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [],
            [1],
            [2, 1],
            [3, 2, 1],
            [1, 2, 3],
            [5, 3, 4, 1, 2],
        ]
        for fn in SORT_FUNCTIONS:
            for case in cases:
                with self.subTest(fn=fn.__name__, case=case):
                    expected = sorted(case)
                    out = fn(list(case))
                    self.assertEqual(out, expected)

    def test_random_data_matches_builtin(self):
        random.seed(42)
        for fn in SORT_FUNCTIONS:
            for _ in range(5):
                arr = [random.randint(0, 1000) for _ in range(50)]
                with self.subTest(fn=fn.__name__):
                    self.assertEqual(fn(list(arr)), sorted(arr))

    def test_input_not_mutated(self):
        for fn in SORT_FUNCTIONS:
            arr = [3, 1, 2]
            arr_copy = list(arr)
            _ = fn(arr)
            self.assertEqual(arr, arr_copy)


if __name__ == "__main__":
    unittest.main()
