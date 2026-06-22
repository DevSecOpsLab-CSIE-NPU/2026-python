"""
第一題測試：資料清理
"""

import unittest

from p1_data_cleaning import clean_numbers, solve


class TestDataCleaning(unittest.TestCase):
    def test_clean_numbers_should_remove_duplicates_filter_and_sort(self):
        numbers = [10, 3, 10, 5, -5]
        self.assertEqual(clean_numbers(numbers), [-5, 5, 10])

    def test_clean_numbers_should_return_empty_when_no_match(self):
        self.assertEqual(clean_numbers([1, 2, 3, 4]), [])

    def test_clean_numbers_should_not_modify_original_list(self):
        numbers = [10, 5, 10, 3]
        original = numbers.copy()

        clean_numbers(numbers)

        self.assertEqual(numbers, original)

    def test_solve_multiple_groups(self):
        input_text = "5\n10 3 10 5 -5\n4\n1 2 3 4\n0\n"
        expected = "-5 5 10\nNONE"
        self.assertEqual(solve(input_text), expected)


if __name__ == "__main__":
    unittest.main()
