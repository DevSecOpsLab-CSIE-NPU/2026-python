import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task1_sequence_clean import process_sequence, solve


class TestTask1(unittest.TestCase):

    def test_normal_case(self):
        nums = [4, 7, 4, 2, 9, 2, 6, 7]
        self.assertEqual(process_sequence(nums, D=2), [2, 4, 6])

    def test_all_filtered_out(self):
        nums = [1, 3, 5]
        self.assertEqual(process_sequence(nums, D=2), [])

    def test_single_divisible(self):
        nums = [10]
        self.assertEqual(process_sequence(nums, D=5), [10])

    def test_single_not_divisible(self):
        nums = [7]
        self.assertEqual(process_sequence(nums, D=5), [])

    def test_duplicates_removed(self):
        nums = [5, 10, 5, 15, 10, 20]
        self.assertEqual(process_sequence(nums, D=5), [5, 10, 15, 20])

    def test_solve_multiple_cases(self):
        input_data = "8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
        expected = "2 4 6\nNONE\n"
        self.assertEqual(solve(input_data, D=2), expected)

    def test_solve_empty_input(self):
        input_data = "0\n"
        expected = ""
        self.assertEqual(solve(input_data, D=2), expected)


if __name__ == "__main__":
    unittest.main()
