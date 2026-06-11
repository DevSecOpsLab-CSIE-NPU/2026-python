import unittest
import random

from stage2 import sorts


class TestSorts(unittest.TestCase):
    def setUp(self):
        self.funcs = [
            sorts.bubble_sort,
            sorts.quick_sort,
            sorts.merge_sort,
        ]

    def test_sort_correctness_and_no_modify(self):
        data = [5, 3, 1, 4, 2]
        expected = sorted(data)
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                arr = list(data)
                result = func(arr)
                self.assertEqual(result, expected)
                self.assertEqual(arr, data)  # input not modified
                self.assertIsNot(result, arr)  # returned new list

    def test_edge_empty_list(self):
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                arr = []
                res = func(arr)
                self.assertEqual(res, [])
                self.assertEqual(arr, [])

    def test_repeats_and_negatives(self):
        data = [3, -1, 2, 3, -5, 0]
        expected = sorted(data)
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                arr = list(data)
                res = func(arr)
                self.assertEqual(res, expected)
                self.assertEqual(arr, data)


if __name__ == '__main__':
    unittest.main()
