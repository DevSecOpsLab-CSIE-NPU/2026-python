import unittest

from search import binary_search, linear_search, set_search


INDEX_SEARCHES = (linear_search, binary_search)


class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        data = [1, 3, 5, 7, 9]
        for func in INDEX_SEARCHES:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(data, 7), 3)
        self.assertIs(set_search(data, 7), True)

    def test_not_found_cases(self):
        data = [1, 3, 5, 7, 9]
        for func in INDEX_SEARCHES:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(data, 6), -1)
        self.assertIs(set_search(data, 6), False)

    def test_input_not_mutated(self):
        data = [1, 3, 5, 7, 9]
        original = list(data)
        linear_search(data, 5)
        binary_search(data, 5)
        set_search(data, 5)
        self.assertEqual(data, original)

    def test_edge_cases(self):
        self.assertEqual(linear_search([], 10), -1)
        self.assertEqual(binary_search([], 10), -1)
        self.assertIs(set_search([], 10), False)
        self.assertEqual(linear_search([4, 4, 4], 4), 0)
        self.assertEqual(binary_search([4, 4, 4], 4), 1)


if __name__ == "__main__":
    unittest.main()
