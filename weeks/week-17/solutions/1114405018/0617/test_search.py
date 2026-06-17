import unittest

from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def test_found_at_beginning(self):
        data = [3, 1, 4, 1, 5]
        self.assertEqual(linear_search(data, 3), 0)

    def test_found_at_end(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(data, 5), 4)

    def test_not_found_returns_minus_one(self):
        data = [10, 20, 30]
        self.assertEqual(linear_search(data, 99), -1)

    def test_empty_list_returns_minus_one(self):
        self.assertEqual(linear_search([], 42), -1)

    def test_single_element_found(self):
        self.assertEqual(linear_search([7], 7), 0)

    def test_single_element_not_found(self):
        self.assertEqual(linear_search([7], 5), -1)

    def test_does_not_mutate_data(self):
        data = [3, 1, 2]
        original = data.copy()
        linear_search(data, 1)
        self.assertEqual(data, original)


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 5), 2)

    def test_found_first_element(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 1), 0)

    def test_found_last_element(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 9), 4)

    def test_not_found_returns_minus_one(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 4), -1)

    def test_empty_list_returns_minus_one(self):
        self.assertEqual(binary_search([], 42), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([7], 7), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([7], 5), -1)

    def test_does_not_mutate_data(self):
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        binary_search(data, 3)
        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
