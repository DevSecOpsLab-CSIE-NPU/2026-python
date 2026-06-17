
import unittest
 
from search import binary_search, linear_search
 
 
class TestLinearSearch(unittest.TestCase):
    def test_found_returns_index(self):
        self.assertEqual(linear_search([5, 3, 9, 1], 9), 2)
 
    def test_found_returns_first_match(self):
        self.assertEqual(linear_search([4, 7, 7, 4], 7), 1)
 
    def test_not_found_returns_minus_one(self):
        self.assertEqual(linear_search([1, 2, 3], 99), -1)
 
    def test_empty_returns_minus_one(self):
        self.assertEqual(linear_search([], 1), -1)
 
    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        snapshot = list(data)
        linear_search(data, 1)
        self.assertEqual(data, snapshot)
 
 
class TestBinarySearch(unittest.TestCase):
    def test_found_returns_index(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 7), 3)
 
    def test_first_and_last(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 9), 4)
 
    def test_not_found_returns_minus_one(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 4), -1)
 
    def test_empty_returns_minus_one(self):
        self.assertEqual(binary_search([], 1), -1)
 
    def test_does_not_mutate_input(self):
        data = [1, 2, 3, 4, 5]
        snapshot = list(data)
        binary_search(data, 4)
        self.assertEqual(data, snapshot)
 
 
if __name__ == "__main__":
    unittest.main()