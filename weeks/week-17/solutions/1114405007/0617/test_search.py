import unittest
from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):

    def test_found_first(self):
        data = [10, 20, 30, 40]
        self.assertEqual(linear_search(data, 10), 0)

    def test_found_last(self):
        data = [10, 20, 30, 40]
        self.assertEqual(linear_search(data, 40), 3)

    def test_not_found(self):
        data = [10, 20, 30, 40]
        self.assertEqual(linear_search(data, 99), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_duplicates_returns_first(self):
        data = [5, 5, 5, 5]
        self.assertEqual(linear_search(data, 5), 0)

    def test_single_element_found(self):
        self.assertEqual(linear_search([7], 7), 0)

    def test_single_element_not_found(self):
        self.assertEqual(linear_search([7], 8), -1)

    def test_does_not_mutate_data(self):
        data = [3, 1, 2]
        original = data.copy()
        linear_search(data, 1)
        self.assertEqual(data, original)


class TestBinarySearch(unittest.TestCase):

    def test_found_first(self):
        data = [10, 20, 30, 40]
        self.assertEqual(binary_search(data, 10), 0)

    def test_found_last(self):
        data = [10, 20, 30, 40]
        self.assertEqual(binary_search(data, 40), 3)

    def test_found_middle(self):
        data = [10, 20, 30, 40]
        self.assertEqual(binary_search(data, 30), 2)

    def test_not_found(self):
        data = [10, 20, 30, 40]
        self.assertEqual(binary_search(data, 99), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([7], 7), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([7], 8), -1)

    def test_duplicates(self):
        data = [5, 5, 5, 5]
        self.assertEqual(binary_search(data, 5), 0)

    def test_does_not_mutate_data(self):
        data = [1, 2, 3]
        original = data.copy()
        binary_search(data, 2)
        self.assertEqual(data, original)

    def test_odd_length(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 5), 2)
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 9), 4)

    def test_even_length(self):
        data = [1, 3, 5, 7]
        self.assertEqual(binary_search(data, 3), 1)
        self.assertEqual(binary_search(data, 7), 3)


if __name__ == "__main__":
    unittest.main()
