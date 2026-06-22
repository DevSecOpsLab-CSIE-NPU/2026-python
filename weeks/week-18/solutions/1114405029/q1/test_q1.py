import os
import sys
import unittest
import importlib.util

MODULE_PATH = os.path.join(os.path.dirname(__file__), "q1.py")
SPEC = importlib.util.spec_from_file_location("q1_solution", MODULE_PATH)
q1_solution = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(q1_solution)

clean_numbers = q1_solution.clean_numbers
dedupe_keep_order = q1_solution.dedupe_keep_order
filter_divisible = q1_solution.filter_divisible
solve = q1_solution.solve


class TestQ1DataCleaning(unittest.TestCase):
    def test_dedupe_filter_sort_general_case(self):
        nums = [4, 7, 4, 2, 9, 2, 6, 7]
        self.assertEqual(dedupe_keep_order(nums), [4, 7, 2, 9, 6])
        self.assertEqual(filter_divisible(nums, 3), [9, 6])
        self.assertEqual(clean_numbers(nums, 3), [6, 9])

    def test_no_matching_numbers_outputs_none(self):
        self.assertEqual(clean_numbers([1, 2, 4, 5], 3), [])
        self.assertEqual(solve("4\n1 2 4 5\n0\n", 3), "NONE")

    def test_negative_zero_and_duplicates(self):
        nums = [-6, 0, -6, 3, 4, 0, -3]
        self.assertEqual(dedupe_keep_order(nums), [-6, 0, 3, 4, -3])
        self.assertEqual(clean_numbers(nums, 3), [-6, -3, 0, 3])

    def test_multiple_groups_until_zero(self):
        sample = "8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
        self.assertEqual(solve(sample, 3), "6 9\n3")

    def test_edge_single_number_empty_result(self):
        self.assertEqual(solve("1\n5\n0\n", 3), "NONE")

    def test_invalid_divisor_raises(self):
        with self.assertRaises(ValueError):
            filter_divisible([1, 2, 3], 0)


if __name__ == "__main__":
    unittest.main()
