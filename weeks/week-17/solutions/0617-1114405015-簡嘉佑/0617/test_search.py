import unittest

from search import binary_search, linear_search


class TestSearch(unittest.TestCase):
    def test_linear_search_found_and_not_found(self):
        data = [5, 1, 9, 2]
        self.assertEqual(linear_search(data, 9), 2)
        self.assertEqual(linear_search(data, 7), -1)

    def test_binary_search_found_and_not_found(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 7), 3)
        self.assertEqual(binary_search(data, 8), -1)

    def test_search_does_not_modify_input(self):
        data1 = [4, 2, 8, 1]
        data1_before = data1[:]
        _ = linear_search(data1, 8)
        self.assertEqual(data1, data1_before)

        data2 = [1, 2, 3, 4]
        data2_before = data2[:]
        _ = binary_search(data2, 3)
        self.assertEqual(data2, data2_before)


if __name__ == "__main__":
    unittest.main()
