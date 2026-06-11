import unittest

from sorts_fast import merge_sort_fast, quick_sort_fast


SORT_FUNCTIONS = [quick_sort_fast, merge_sort_fast]


class TestStage3FastSorts(unittest.TestCase):
    def assert_all_sort_functions(self, data, expected):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__, data=data):
                original = list(data)
                result = sort_func(original)
                self.assertEqual(result, expected)
                self.assertEqual(original, data)
                self.assertIsInstance(result, list)

    def test_fast_sorts_basic_unsorted_list(self):
        self.assert_all_sort_functions([5, 1, 4, 2], [1, 2, 4, 5])

    def test_fast_sorts_duplicates(self):
        self.assert_all_sort_functions([3, 3, 1, 2, 1], [1, 1, 2, 3, 3])

    def test_fast_sorts_edge_case_single_item(self):
        self.assert_all_sort_functions([7], [7])


if __name__ == "__main__":
    unittest.main()
