import unittest
from search import linear_search, binary_search, set_search

SEARCH_FUNCTIONS = [
    ("linear_search", linear_search),
    ("binary_search", binary_search),
    ("set_search", set_search),
]


def _found(result):
    """normalize: return True if result means 'found'"""
    if isinstance(result, bool):
        return result is True
    if isinstance(result, int):
        return result >= 0
    return False


class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        data = [1, 3, 5, 7, 9, 11]
        targets = [1, 5, 11]
        for name, func in SEARCH_FUNCTIONS:
            for t in targets:
                with self.subTest(f"{name} found {t}"):
                    self.assertTrue(_found(func(data, t)))

    def test_not_found_cases(self):
        data = [1, 3, 5, 7, 9, 11]
        targets = [0, 4, 12]
        for name, func in SEARCH_FUNCTIONS:
            for t in targets:
                with self.subTest(f"{name} not found {t}"):
                    self.assertFalse(_found(func(data, t)))

    def test_empty_list(self):
        data = []
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(f"{name} empty"):
                self.assertFalse(_found(func(data, 1)))

    def test_duplicate_values(self):
        data = [4, 2, 4, 2, 4]
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(f"{name} duplicates"):
                self.assertTrue(_found(func(data, 4)))
                self.assertFalse(_found(func(data, 1)))

    def test_input_not_mutated(self):
        data = [5, 3, 1, 4, 2]
        original = data[:]
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(f"{name} not mutated"):
                func(data, 3)
                self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
