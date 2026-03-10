import unittest
from task1_sequence_clean import process_sequence

class TestSequenceClean(unittest.TestCase):
    def test_normal_case(self):
        nums = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        result = process_sequence(nums)
        self.assertEqual(result['dedupe'], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result['asc'], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result['desc'], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result['evens'], [2, 2, 8])

    def test_edge_case_empty(self):
        nums = []
        result = process_sequence(nums)
        self.assertEqual(result['dedupe'], [])
        self.assertEqual(result['asc'], [])
        self.assertEqual(result['desc'], [])
        self.assertEqual(result['evens'], [])

    def test_edge_case_all_same(self):
        nums = [2, 2, 2, 2]
        result = process_sequence(nums)
        self.assertEqual(result['dedupe'], [2])
        self.assertEqual(result['asc'], [2, 2, 2, 2])
        self.assertEqual(result['desc'], [2, 2, 2, 2])
        self.assertEqual(result['evens'], [2, 2, 2, 2])

    def test_no_duplicates(self):
        nums = [1, 3, 5, 7]
        result = process_sequence(nums)
        self.assertEqual(result['dedupe'], [1, 3, 5, 7])
        self.assertEqual(result['asc'], [1, 3, 5, 7])
        self.assertEqual(result['desc'], [7, 5, 3, 1])
        self.assertEqual(result['evens'], [])

    def test_mixed_pos_neg(self):
        nums = [-1, 2, -3, 4, -1, 2]
        result = process_sequence(nums)
        self.assertEqual(result['dedupe'], [-1, 2, -3, 4])
        self.assertEqual(result['asc'], [-3, -1, -1, 2, 2, 4])
        self.assertEqual(result['desc'], [4, 2, 2, -1, -1, -3])
        self.assertEqual(result['evens'], [2, 4, 2])

if __name__ == '__main__':
    unittest.main()