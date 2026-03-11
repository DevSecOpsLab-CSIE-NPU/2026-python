import unittest
from task1 import sequence_clean

class TestSequenceClean(unittest.TestCase):
    def test_normal_case(self):
        input_seq = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = {
            'dedupe': [5, 3, 2, 9, 8, 1],
            'asc': [1, 2, 2, 3, 3, 5, 5, 8, 9],
            'desc': [9, 8, 5, 5, 3, 3, 2, 2, 1],
            'evens': [2, 2, 8]
        }
        self.assertEqual(sequence_clean(input_seq), expected)

    def test_empty_sequence(self):
        input_seq = []
        expected = {
            'dedupe': [],
            'asc': [],
            'desc': [],
            'evens': []
        }
        self.assertEqual(sequence_clean(input_seq), expected)

    def test_no_duplicates_no_evens(self):
        input_seq = [1, 3, 5, 7]
        expected = {
            'dedupe': [1, 3, 5, 7],
            'asc': [1, 3, 5, 7],
            'desc': [7, 5, 3, 1],
            'evens': []
        }
        self.assertEqual(sequence_clean(input_seq), expected)

if __name__ == '__main__':
    unittest.main()
