import unittest
from task1_sequence_clean import sequence_clean, format_sequence_clean

class TestTask1SequenceClean(unittest.TestCase):
    def test_normal_case(self):
        inp = "5 3 5 2 9 2 8 3 1"
        out = sequence_clean(inp)
        self.assertEqual(out['dedupe'], [5,3,2,9,8,1])
        self.assertEqual(out['asc'], [1,2,2,3,3,5,5,8,9])
        self.assertEqual(out['desc'], [9,8,5,5,3,3,2,2,1])
        self.assertEqual(out['evens'], [2,2,8])
        text = format_sequence_clean(out)
        self.assertIn('dedupe: 5 3 2 9 8 1', text)

    def test_empty_input(self):
        out = sequence_clean("")
        self.assertEqual(out['dedupe'], [])
        self.assertEqual(out['asc'], [])
        self.assertEqual(out['desc'], [])
        self.assertEqual(out['evens'], [])

    def test_negative_and_zero(self):
        out = sequence_clean("0 -1 -1 4 4")
        self.assertEqual(out['dedupe'], [0,-1,4])
        self.assertEqual(out['asc'], [-1,-1,0,4,4])
        self.assertEqual(out['desc'], [4,4,0,-1,-1])
        self.assertEqual(out['evens'], [0,4,4])
