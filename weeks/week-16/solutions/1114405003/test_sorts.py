import unittest
from sorts import bubble_sort, quick_sort, merge_sort

SORTS = [bubble_sort, quick_sort, merge_sort]


class TestSorts(unittest.TestCase):

    def _check(self, sort_func, input_list, expected):
        original = input_list.copy()
        result = sort_func(input_list)
        self.assertEqual(result, expected)
        self.assertEqual(input_list, original, f"{sort_func.__name__} mutated input!")

    def test_empty_list(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                self._check(s, [], [])

    def test_single_element(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                self._check(s, [1], [1])

    def test_already_sorted(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                self._check(s, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                self._check(s, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5])

    def test_duplicates(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                self._check(s, [3, 1, 2, 1, 3], [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                self._check(s, [-1, 3, -5, 0], [-5, -1, 0, 3])

    def test_does_not_mutate_input(self):
        for s in SORTS:
            with self.subTest(sort=s.__name__):
                original = [3, 1, 2]
                s(original)
                self.assertEqual(original, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
