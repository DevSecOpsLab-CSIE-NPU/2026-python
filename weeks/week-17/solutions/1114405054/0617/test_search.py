import unittest

from search import binary_search, linear_search


class TestLinearSearch(unittest.TestCase):

    def test_found_first_element(self):
        data = [10, 20, 30, 40, 50]
        self.assertEqual(linear_search(data, 10), 0)

    def test_found_last_element(self):
        data = [10, 20, 30, 40, 50]
        self.assertEqual(linear_search(data, 50), 4)

    def test_found_middle_element(self):
        data = [10, 20, 30, 40, 50]
        self.assertEqual(linear_search(data, 30), 2)

    def test_not_found(self):
        data = [10, 20, 30, 40, 50]
        self.assertEqual(linear_search(data, 99), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(linear_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(linear_search([5], 3), -1)

    def test_returns_first_occurrence_for_duplicates(self):
        data = [1, 3, 3, 3, 5]
        self.assertEqual(linear_search(data, 3), 1)

    def test_target_none(self):
        data = [1, None, 2]
        self.assertEqual(linear_search(data, None), 1)

    def test_does_not_mutate_data(self):
        data = [3, 1, 2]
        original = data.copy()
        linear_search(data, 2)
        self.assertEqual(data, original)

    def test_rejects_non_list_data(self):
        with self.assertRaises(TypeError):
            linear_search(None, 1)
        with self.assertRaises(TypeError):
            linear_search(42, 1)
        with self.assertRaises(TypeError):
            linear_search("abc", 1)


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.sorted_data = [10, 20, 30, 40, 50, 60, 70]

    def test_found_first_element(self):
        self.assertEqual(binary_search(self.sorted_data, 10), 0)

    def test_found_last_element(self):
        self.assertEqual(binary_search(self.sorted_data, 70), 6)

    def test_found_middle_element(self):
        self.assertEqual(binary_search(self.sorted_data, 40), 3)

    def test_not_found(self):
        self.assertEqual(binary_search(self.sorted_data, 99), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([5], 3), -1)

    def test_does_not_mutate_data(self):
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        binary_search(data, 3)
        self.assertEqual(data, original)

    def test_unsorted_data_returns_minus_one(self):
        data = [5, 3, 1, 2, 4]
        self.assertEqual(binary_search(data, 3), -1)

    def test_rejects_non_list_data(self):
        with self.assertRaises(TypeError):
            binary_search(None, 1)
        with self.assertRaises(TypeError):
            binary_search(42, 1)
        with self.assertRaises(TypeError):
            binary_search("abc", 1)


if __name__ == "__main__":
    unittest.main()
