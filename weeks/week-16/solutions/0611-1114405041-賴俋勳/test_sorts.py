import unittest

from sorts import bubble_sort, merge_sort, quick_sort
from sorts_fast import quick_sort_median


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort, quick_sort_median]


class TestSorts(unittest.TestCase):
    def test_shared_cases(self):
        cases = [
            ([3, 1, 2], [1, 2, 3]),
            ([], []),
            ([4, 4, 1], [1, 4, 4]),
        ]
        for fn in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort=fn.__name__, data=data):
                    self.assertEqual(fn(data), expected)

    def test_input_list_not_modified(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(sort=fn.__name__):
                data = [5, 2, 3, 1]
                snap = data[:]
                _ = fn(data)
                self.assertEqual(data, snap)


if __name__ == "__main__":
    unittest.main()
