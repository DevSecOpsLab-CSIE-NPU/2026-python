import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def test_linear_finds_existing(self):
        data = [3, 7, 1, 9, 4]
        self.assertEqual(linear_search(data, 9), 3)

    def test_linear_returns_minus1_if_not_found(self):
        data = [3, 7, 1, 9, 4]
        self.assertEqual(linear_search(data, 5), -1)

    def test_binary_finds_existing(self):
        data = [1, 3, 4, 7, 9]
        self.assertEqual(binary_search(data, 9), 4)

    def test_binary_returns_minus1_if_not_found(self):
        data = [1, 3, 4, 7, 9]
        self.assertEqual(binary_search(data, 5), -1)

    def test_binary_on_unsorted_returns_minus1(self):
        data = [1, 3, 7, 9, 4]
        self.assertEqual(binary_search(data, 4), -1)

    def test_does_not_modify_input(self):
        data = [3, 7, 1, 9, 4]
        original = data.copy()
        linear_search(data, 9)
        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
