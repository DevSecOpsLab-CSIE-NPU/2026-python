import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task1_sequence_clean import process_sequence, solve, get_D


class TestGetD(unittest.TestCase):

    def test_my_student_id(self):
        self.assertEqual(get_D(1114405007), 5)


class TestProcessSequence(unittest.TestCase):

    def test_group1_all_filtered(self):
        nums = [4, 7, 4, 2, 9, 2, 6]
        self.assertEqual(process_sequence(nums, D=5), [])

    def test_group2_one_match(self):
        nums = [1, 5, 3]
        self.assertEqual(process_sequence(nums, D=5), [5])

    def test_group3_all_divisible(self):
        nums = [5, 10, 15, 20, 25]
        self.assertEqual(process_sequence(nums, D=5), [5, 10, 15, 20, 25])

    def test_group4_with_duplicates(self):
        nums = [5, 5, 10, 5, 10, 15]
        self.assertEqual(process_sequence(nums, D=5), [5, 10, 15])

    def test_single_element_divisible(self):
        nums = [25]
        self.assertEqual(process_sequence(nums, D=5), [25])

    def test_single_element_not_divisible(self):
        nums = [7]
        self.assertEqual(process_sequence(nums, D=5), [])

    def test_negative_numbers(self):
        nums = [-10, -5, 0, 5, 10]
        self.assertEqual(process_sequence(nums, D=5), [-10, -5, 0, 5, 10])

    def test_large_numbers(self):
        nums = [10**9, -10**9, 10**9]
        self.assertEqual(process_sequence(nums, D=5), [-10**9, 10**9])


class TestSolve(unittest.TestCase):

    def test_two_groups(self):
        input_data = "7\n4 7 4 2 9 2 6\n3\n1 5 3\n0\n"
        expected = "NONE\n5\n"
        self.assertEqual(solve(input_data, D=5), expected)

    def test_three_groups(self):
        input_data = "5\n5 10 15 20 25\n3\n1 2 3\n1\n7\n0\n"
        expected = "5 10 15 20 25\nNONE\nNONE\n"
        self.assertEqual(solve(input_data, D=5), expected)

    def test_empty_input(self):
        input_data = "0\n"
        expected = ""
        self.assertEqual(solve(input_data, D=5), expected)

    def test_single_group_all_match(self):
        input_data = "4\n5 10 15 20\n0\n"
        expected = "5 10 15 20\n"
        self.assertEqual(solve(input_data, D=5), expected)

    def test_single_group_none_match(self):
        input_data = "4\n1 2 3 4\n0\n"
        expected = "NONE\n"
        self.assertEqual(solve(input_data, D=5), expected)


if __name__ == "__main__":
    unittest.main()
