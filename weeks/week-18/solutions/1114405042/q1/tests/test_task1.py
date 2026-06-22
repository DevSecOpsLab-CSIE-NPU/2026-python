import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from task1_sequence_clean import process_sequence, format_output


class TestSequenceClean(unittest.TestCase):

    def test_normal_case(self):
        result = process_sequence("5 3 5 2 9 2 8 3 1")
        self.assertEqual(result["result"], [8])

    def test_multiple_divisible(self):
        result = process_sequence("4 8 12 4 16 8 20")
        self.assertEqual(result["result"], [4, 8, 12, 16, 20])

    def test_no_divisible(self):
        result = process_sequence("1 2 3 5 7 9")
        self.assertEqual(result["result"], [])

    def test_empty_input(self):
        result = process_sequence("")
        self.assertEqual(result["result"], [])

    def test_single_divisible(self):
        result = process_sequence("4")
        self.assertEqual(result["result"], [4])

    def test_negative_divisible(self):
        result = process_sequence("-8 -4 0 4 8")
        self.assertEqual(result["result"], [-8, -4, 0, 4, 8])

    def test_preserve_order_then_filter(self):
        result = process_sequence("12 4 8 12 4 20")
        self.assertEqual(result["result"], [4, 8, 12, 20])


if __name__ == "__main__":
    unittest.main()
