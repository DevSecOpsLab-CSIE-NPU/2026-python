"""0617 任務二: 搜尋函式測試。"""

import unittest

from search import binary_search, linear_search


class TestSearch(unittest.TestCase):
    def test_linear_search_found_and_not_found(self):
        data = [10, 20, 30, 40]
        self.assertEqual(linear_search(data, 30), 2)
        self.assertEqual(linear_search(data, 99), -1)

    def test_binary_search_found_and_not_found(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(data, 7), 3)
        self.assertEqual(binary_search(data, 8), -1)

    def test_binary_search_unsorted_behavior_is_undefined(self):
        data = [3, 1, 2]
        result = binary_search(data, 2)
        self.assertIsInstance(result, int)

    def test_search_functions_do_not_modify_input(self):
        linear_data = [5, 2, 8]
        linear_before = linear_data.copy()
        _ = linear_search(linear_data, 2)
        self.assertEqual(linear_data, linear_before)

        binary_data = [1, 2, 4, 8]
        binary_before = binary_data.copy()
        _ = binary_search(binary_data, 4)
        self.assertEqual(binary_data, binary_before)


if __name__ == "__main__":
    unittest.main()
