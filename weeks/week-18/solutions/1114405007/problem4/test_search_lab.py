import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task4_search_lab import binary_search, linear_search, make_sorted_array


class TestBinarySearch(unittest.TestCase):

    def test_found_first(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = binary_search(arr, 1)
        self.assertEqual(idx, 0)

    def test_found_last(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = binary_search(arr, 11)
        self.assertEqual(idx, 5)

    def test_found_mid(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = binary_search(arr, 7)
        self.assertEqual(idx, 3)

    def test_not_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = binary_search(arr, 4)
        self.assertEqual(idx, -1)

    def test_empty_array(self):
        idx, cmp = binary_search([], 5)
        self.assertEqual(idx, -1)
        self.assertEqual(cmp, 0)

    def test_single_element_found(self):
        idx, cmp = binary_search([5], 5)
        self.assertEqual(idx, 0)

    def test_single_element_not_found(self):
        idx, cmp = binary_search([5], 3)
        self.assertEqual(idx, -1)


class TestLinearSearch(unittest.TestCase):

    def test_found_first(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = linear_search(arr, 1)
        self.assertEqual(idx, 0)

    def test_found_last(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = linear_search(arr, 11)
        self.assertEqual(idx, 5)

    def test_not_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        idx, cmp = linear_search(arr, 4)
        self.assertEqual(idx, -1)

    def test_empty_array(self):
        idx, cmp = linear_search([], 5)
        self.assertEqual(idx, -1)
        self.assertEqual(cmp, 0)

    def test_single_element_found(self):
        idx, cmp = linear_search([5], 5)
        self.assertEqual(idx, 0)

    def test_comparison_count_not_found(self):
        arr = [1, 3, 5, 7]
        idx, cmp = linear_search(arr, 6)
        self.assertEqual(cmp, 4)

    def test_comparison_count_found(self):
        arr = [1, 3, 5, 7]
        idx, cmp = linear_search(arr, 5)
        self.assertEqual(cmp, 3)


class TestMakeSortedArray(unittest.TestCase):

    def test_size(self):
        arr = make_sorted_array(100)
        self.assertEqual(len(arr), 100)

    def test_sorted(self):
        arr = make_sorted_array(1000)
        for i in range(len(arr) - 1):
            self.assertLessEqual(arr[i], arr[i + 1])

    def test_size_zero(self):
        arr = make_sorted_array(0)
        self.assertEqual(arr, [])

    def test_size_negative(self):
        arr = make_sorted_array(-5)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
