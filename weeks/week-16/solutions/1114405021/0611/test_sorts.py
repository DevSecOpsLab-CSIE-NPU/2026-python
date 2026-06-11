import random
import unittest

from sorts import bubble_sort, merge_sort, quick_sort

try:
    from sorts_fast import bubble_sort_fast, merge_sort_fast, quick_sort_fast
except ImportError:
    bubble_sort_fast = None
    merge_sort_fast = None
    quick_sort_fast = None


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]
if bubble_sort_fast is not None:
    SORT_FUNCTIONS.extend([bubble_sort_fast, quick_sort_fast, merge_sort_fast])


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [],
            [1],
            [2, 1],
            [3, 1, 2],
            [5, 5, 2, 8, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
        ]
        for sort_func in SORT_FUNCTIONS:
            for case in cases:
                with self.subTest(sort_func=sort_func.__name__, case=case):
                    self.assertEqual(sort_func(case), sorted(case))

    def test_random_data_matches_builtin(self):
        rng = random.Random(1234)
        cases = [
            [rng.randint(-100, 100) for _ in range(0)],
            [rng.randint(-100, 100) for _ in range(1)],
            [rng.randint(-100, 100) for _ in range(10)],
            [rng.randint(-100, 100) for _ in range(25)],
        ]
        for sort_func in SORT_FUNCTIONS:
            for case in cases:
                with self.subTest(sort_func=sort_func.__name__, case_size=len(case)):
                    self.assertEqual(sort_func(case), sorted(case))

    def test_input_not_mutated(self):
        cases = [
            [3, 1, 2],
            [5, 4, 3, 2, 1],
            [2, 2, 1, 1, 3],
        ]
        for sort_func in SORT_FUNCTIONS:
            for case in cases:
                original = list(case)
                with self.subTest(sort_func=sort_func.__name__, case=case):
                    result = sort_func(case)
                    self.assertEqual(case, original)
                    self.assertIsNot(result, case)
                    self.assertEqual(result, sorted(original))


if __name__ == "__main__":
    unittest.main()