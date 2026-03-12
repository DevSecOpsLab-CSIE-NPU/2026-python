import unittest
from task1_sequence_clean import clean_sequence

class TestTask1(unittest.TestCase):
    def test_basic(self):
        res = clean_sequence("5 3 5 2")
        self.assertEqual(res['dedupe'], [5, 3, 2])
        self.assertEqual(res['asc'], [2, 3, 5, 5])
    def test_empty(self):
        self.assertEqual(clean_sequence("")['dedupe'], [])
    def test_evens(self):
        self.assertEqual(clean_sequence("1 3 5")['evens'], [])