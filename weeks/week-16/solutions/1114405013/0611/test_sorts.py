import random
import unittest

from sorts import bubble_sort, merge_sort, quick_sort


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def test_basic_and_edge_cases(self):
        cases = [
            [],
            [1],
            [3, 1, 2],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [3, 1, 2, 3, 1],
            [-1, 5, 0, -3, 2],
        ]

        for sort_function in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort_function=sort_function.__name__, data=data):
                    self.assertEqual(sort_function(data), sorted(data))

    def test_random_data_matches_builtin(self):
        rng = random.Random(42)
        data = [rng.randint(-100, 100) for _ in range(50)]

        for sort_function in SORT_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function(data), sorted(data))

    def test_input_not_mutated(self):
        original = [5, 1, 4, 1, 3]

        for sort_function in SORT_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                data = original.copy()
                result = sort_function(data)

                self.assertEqual(data, original)
                self.assertIsNot(result, data)


if __name__ == "__main__":
    unittest.main()
