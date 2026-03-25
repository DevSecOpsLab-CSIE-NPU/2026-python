import unittest
import sys
from pathlib import Path

# Add parent directory to path so we can import task1_sequence_clean
sys.path.insert(0, str(Path(__file__).parent.parent))

from task1_sequence_clean import process_sequence


class TestTask1SequenceClean(unittest.TestCase):
    """Test suite for sequence clean operations - dedupe, sort asc/desc, filter evens"""

    def test_normal_case(self):
        """Test normal case with mixed numbers"""
        input_str = "5 3 5 2 9 2 8 3 1"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result['asc'], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result['desc'], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result['evens'], [2, 2, 8])

    def test_single_element(self):
        """Test boundary case with single element"""
        input_str = "5"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [5])
        self.assertEqual(result['asc'], [5])
        self.assertEqual(result['desc'], [5])
        self.assertEqual(result['evens'], [])

    def test_all_same_numbers(self):
        """Test boundary case with repeated same number"""
        input_str = "3 3 3 3"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [3])
        self.assertEqual(result['asc'], [3, 3, 3, 3])
        self.assertEqual(result['desc'], [3, 3, 3, 3])
        self.assertEqual(result['evens'], [])

    def test_all_even_numbers(self):
        """Test case where all numbers are even"""
        input_str = "2 4 6 8"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [2, 4, 6, 8])
        self.assertEqual(result['asc'], [2, 4, 6, 8])
        self.assertEqual(result['desc'], [8, 6, 4, 2])
        self.assertEqual(result['evens'], [2, 4, 6, 8])

    def test_no_even_numbers(self):
        """Test case where no numbers are even (all odd)"""
        input_str = "1 3 5 7 9"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [1, 3, 5, 7, 9])
        self.assertEqual(result['asc'], [1, 3, 5, 7, 9])
        self.assertEqual(result['desc'], [9, 7, 5, 3, 1])
        self.assertEqual(result['evens'], [])

    def test_zero_in_sequence(self):
        """Test with zero (which is even)"""
        input_str = "0 1 2 0 3"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [0, 1, 2, 3])
        self.assertEqual(result['asc'], [0, 0, 1, 2, 3])
        self.assertEqual(result['desc'], [3, 2, 1, 0, 0])
        self.assertEqual(result['evens'], [0, 2, 0])

    def test_negative_numbers(self):
        """Test with negative numbers"""
        input_str = "-2 -1 0 1 2"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [-2, -1, 0, 1, 2])
        self.assertEqual(result['asc'], [-2, -1, 0, 1, 2])
        self.assertEqual(result['desc'], [2, 1, 0, -1, -2])
        self.assertEqual(result['evens'], [-2, 0, 2])

    def test_evens_maintain_original_order(self):
        """Test that evens filter maintains original order, not sorted"""
        input_str = "9 2 5 8 1 4"
        result = process_sequence(input_str)
        
        # evens should be: 2, 8, 4 (in order of appearance, not sorted)
        self.assertEqual(result['evens'], [2, 8, 4])

    def test_dedupe_maintains_first_occurrence(self):
        """Test that dedupe keeps first occurrence order"""
        input_str = "5 3 5 3 2"
        result = process_sequence(input_str)
        
        self.assertEqual(result['dedupe'], [5, 3, 2])


if __name__ == '__main__':
    unittest.main()
