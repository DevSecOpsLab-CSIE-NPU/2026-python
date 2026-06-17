import unittest
from search import linear_search, binary_search

class TestSearchFunctions(unittest.TestCase):
    
    def test_linear_search_found(self):
        data = [1, 2, 3, 4, 5]
        target = 3
        result = linear_search(data, target)
        self.assertEqual(result, 2)  # Index of 3 is 2

    def test_linear_search_not_found(self):
        data = [1, 2, 3, 4, 5]
        target = 6
        result = linear_search(data, target)
        self.assertEqual(result, -1)  # Not found should return -1

    def test_binary_search_found(self):
        data = [1, 2, 3, 4, 5]
        target = 4
        result = binary_search(data, target)
        self.assertEqual(result, 3)  # Index of 4 is 3

    def test_binary_search_not_found(self):
        data = [1, 2, 3, 4, 5]
        target = 0
        result = binary_search(data, target)
        self.assertEqual(result, -1)  # Not found should return -1

    def test_binary_search_unsorted_data(self):
        data = [5, 3, 1, 4, 2]
        target = 3
        result = binary_search(data, target)
        self.assertEqual(result, -1)  # Should return -1 since data is unsorted

if __name__ == "__main__":
    unittest.main()