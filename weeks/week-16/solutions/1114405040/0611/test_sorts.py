import random
import unittest

from sorts import bubble_sort, merge_sort, quick_sort
from sorts_fast import optimized_quick_sort

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort, optimized_quick_sort]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [],
            [1],
            [3, 2, 1],
            [5, -1, 5, 0, 2],
            [1, 1, 1, 1],
            ["banana", "apple", "cherry"],
        ]
        for sorter in SORT_FUNCTIONS:
            for case in cases:
                with self.subTest(sorter=sorter.__name__, case=case):
                    self.assertEqual(sorter(case), sorted(case))

    def test_random_data_matches_builtin(self):
        rng = random.Random(20260611)
        for sorter in SORT_FUNCTIONS:
            for size in (2, 10, 50, 101):
                data = [rng.randint(-500, 500) for _ in range(size)]
                with self.subTest(sorter=sorter.__name__, size=size):
                    self.assertEqual(sorter(data), sorted(data))

    def test_input_not_mutated(self):
        original = [4, 2, 9, 1, 4]
        for sorter in SORT_FUNCTIONS:
            data = original.copy()
            with self.subTest(sorter=sorter.__name__):
                self.assertEqual(sorter(data), sorted(original))
                self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
