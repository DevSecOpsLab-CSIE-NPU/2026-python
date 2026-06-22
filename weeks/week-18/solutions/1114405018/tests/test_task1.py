import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from task1_data_clean import clean_data, solve_input


class TestCleanData(unittest.TestCase):

    def test_sample(self):
        nums = [4, 7, 4, 2, 9, 2, 6, 7]
        self.assertEqual(clean_data(nums, 2), [2, 4, 6])

    def test_no_match_returns_empty(self):
        nums = [1, 3, 5]
        self.assertEqual(clean_data(nums, 2), [])

    def test_edge_all_duplicates_single_result(self):
        nums = [2, 2, 2, 2]
        self.assertEqual(clean_data(nums, 2), [2])


if __name__ == '__main__':
    unittest.main()
