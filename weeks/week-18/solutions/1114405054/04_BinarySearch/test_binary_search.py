import unittest
from binary_search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    def test_linear_found(self):
        idx, cmp = linear_search(self.arr, 10)
        self.assertEqual(idx, 4)

    def test_linear_not_found(self):
        idx, cmp = linear_search(self.arr, 99)
        self.assertEqual(idx, -1)

    def test_binary_found(self):
        idx, cmp = binary_search(self.arr, 10)
        self.assertEqual(idx, 4)

    def test_binary_not_found(self):
        idx, cmp = binary_search(self.arr, 99)
        self.assertEqual(idx, -1)

    def test_target_at_ends(self):
        idx1, _ = binary_search(self.arr, 2)
        idx2, _ = binary_search(self.arr, 20)
        self.assertEqual(idx1, 0)
        self.assertEqual(idx2, 9)


if __name__ == "__main__":
    unittest.main()
