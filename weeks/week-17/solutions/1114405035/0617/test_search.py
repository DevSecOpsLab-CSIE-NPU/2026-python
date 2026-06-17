import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):
    def test_search_correctness(self):
        """驗證線性搜尋與二元搜尋的正確性"""
        data = [1, 3, 5, 7, 9]
        for search_func in [linear_search, binary_search]:
            with self.subTest(search_func=search_func.__name__):
                self.assertEqual(search_func(data, 5), 2)
                self.assertEqual(search_func(data, 1), 0)
                self.assertEqual(search_func(data, 9), 4)
                self.assertEqual(search_func(data, 10), -1)
                self.assertEqual(search_func(data, 0), -1)

    def test_does_not_modify_input(self):
        """驗證搜尋過程不會修改傳入的原始 list"""
        data = [5, 3, 9, 1]
        data_copy = data.copy()
        linear_search(data, 9)
        self.assertEqual(data, data_copy)

        sorted_data = [1, 3, 5, 9]
        sorted_copy = sorted_data.copy()
        binary_search(sorted_data, 5)
        self.assertEqual(sorted_data, sorted_copy)


if __name__ == "__main__":
    unittest.main()
