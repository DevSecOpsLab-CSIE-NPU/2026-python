import unittest

from search import binary_search, linear_search, set_search

SEARCH_FUNCTIONS = [linear_search, binary_search, set_search]


def _found(result) -> bool:
    if isinstance(result, bool):
        return result
    return result >= 0


class TestSearchFunctions(unittest.TestCase):

    def test_found_cases(self):
        data = [10, 20, 30, 40, 50]
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertTrue(_found(fn(data, 10)))
                self.assertTrue(_found(fn(data, 30)))
                self.assertTrue(_found(fn(data, 50)))

    def test_not_found_cases(self):
        data = [10, 20, 30, 40, 50]
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertFalse(_found(fn(data, 99)))
                self.assertFalse(_found(fn(data, -1)))

    def test_empty_list(self):
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertFalse(_found(fn([], 1)))

    def test_single_element_found(self):
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertTrue(_found(fn([5], 5)))

    def test_single_element_not_found(self):
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertFalse(_found(fn([5], 3)))

    def test_input_not_mutated(self):
        data = [3, 1, 2]
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                original = data.copy()
                fn(data, 2)
                self.assertEqual(data, original)

    def test_rejects_non_list_data(self):
        for fn in SEARCH_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                with self.assertRaises(TypeError):
                    fn(None, 1)
                with self.assertRaises(TypeError):
                    fn(42, 1)

    def test_binary_search_unsorted(self):
        data = [5, 3, 1, 2, 4]
        self.assertEqual(binary_search(data, 3), -1)

    def test_set_search_type(self):
        data = [1, 2, 3]
        result = set_search(data, 2)
        self.assertIsInstance(result, bool)

    def test_linear_search_index(self):
        data = [1, 2, 3]
        self.assertEqual(linear_search(data, 2), 1)

    def test_binary_search_index(self):
        data = [1, 2, 3]
        self.assertEqual(binary_search(data, 2), 1)

    def test_linear_search_first_occurrence(self):
        data = [1, 3, 3, 3, 5]
        self.assertEqual(linear_search(data, 3), 1)


if __name__ == "__main__":
    unittest.main()
