import random
import unittest

from sorts import bubble_sort, quick_sort, merge_sort


SORT_FUNCTIONS = [
    bubble_sort,
    quick_sort,
    merge_sort,
]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [],
            [1],
            [3, 1, 2],
            [3, 1, 3, 2],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [5, 5, 5, 5],
            [0, -1, 8, 3, -2],
        ]

        for sort_fn in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort=sort_fn.__name__, data=data):
                    self.assertEqual(sort_fn(data), sorted(data))

    def test_random_data_matches_builtin(self):
        random.seed(42)
        random_cases = [
            [random.randint(-100, 100) for _ in range(size)]
            for size in (5, 10, 20)
        ]

        for sort_fn in SORT_FUNCTIONS:
            for data in random_cases:
                with self.subTest(sort=sort_fn.__name__, data=data):
                    self.assertEqual(sort_fn(data), sorted(data))

    def test_input_not_mutated(self):
        original = [7, 3, 9, 1, 7, 2]

        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                data = list(original)
                result = sort_fn(data)
                self.assertEqual(data, original)
                self.assertIsNot(result, data)

    def test_non_list_input_raises_type_error(self):
        bad_inputs = (
            None,
            "123",
            (3, 2, 1),
            {"a": 1},
        )

        for sort_fn in SORT_FUNCTIONS:
            for bad in bad_inputs:
                with self.subTest(sort=sort_fn.__name__, bad=bad):
                    with self.assertRaises(TypeError):
                        sort_fn(bad)


if __name__ == "__main__":
    unittest.main()
