import unittest
from task1_sequence_clean import clean_sequence

class TestTask1(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(clean_sequence([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_empty_sequence(self):
        self.assertEqual(clean_sequence([]), [])

    def test_no_duplicates(self):
        self.assertEqual(clean_sequence([1, 2, 3]), [1, 2, 3])

    def test_all_duplicates(self):
        self.assertEqual(clean_sequence([1, 1, 1]), [1])

if __name__ == '__main__':
    unittest.main()