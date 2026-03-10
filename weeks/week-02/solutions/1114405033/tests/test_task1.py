import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task1_sequence_clean import clean_sequence

class TestTask1(unittest.TestCase):
    def test_normal_case(self):
        
        res = clean_sequence("5 3 5 2 9 2 8 3 1")
        self.assertEqual(res["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(res["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(res["evens"], [2, 2, 8])

    def test_empty_boundary(self):
        
        res = clean_sequence("  ")
        self.assertEqual(res["dedupe"], [])
        self.assertEqual(res["asc"], [])

    def test_no_evens(self):
        
        res = clean_sequence("1 3 5 7")
        self.assertEqual(res["evens"], [])