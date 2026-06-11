import unittest

from sorts import bubble_sort, merge_sort, quick_sort


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def assert_all_sort_functions(self, data, expected):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__, data=data):
                original = list(data)
                result = sort_func(original)
                self.assertEqual(result, expected)
                self.assertEqual(original, data)
                self.assertIsInstance(result, list)

    def test_basic_unsorted_list(self):
        self.assert_all_sort_functions([3, 1, 2], [1, 2, 3])

    def test_duplicates_and_negatives(self):
        self.assert_all_sort_functions([0, -1, 3, 3, -2], [-2, -1, 0, 3, 3])

    def test_already_sorted_list(self):
        self.assert_all_sort_functions([1, 2, 3, 4], [1, 2, 3, 4])

    def test_edge_case_empty_list(self):
        self.assert_all_sort_functions([], [])


if __name__ == "__main__":
    unittest.main()
