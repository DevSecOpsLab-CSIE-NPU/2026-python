"""
Test Suite for Data Cleaning Problem (D=3)
Task: Extract numbers divisible by D from input and output in ascending order without duplicates.
If no numbers are divisible by D, output NONE.
"""

import unittest
from solution import clean_data


class TestCleanData(unittest.TestCase):
    """Test cases for clean_data function"""
    
    def test_tc1_mixed_numbers(self):
        """TC1: Normal case with mixed odd and even numbers divisible by D=3"""
        # Input: 4 7 4 2 9 2 6 7 (where n=8)
        # Expected: numbers divisible by 3 are [9, 6]
        # Output should be sorted and unique: "6 9"
        numbers = [4, 7, 4, 2, 9, 2, 6, 7]
        result = clean_data(numbers, D=3)
        self.assertEqual(result, "6 9")
    
    def test_tc2_mostly_non_divisible(self):
        """TC2: Edge case where only one number is divisible by D=3"""
        # Input: 1 3 5 (where n=3)
        # Only 3 is divisible by 3
        # Output: "3"
        numbers = [1, 3, 5]
        result = clean_data(numbers, D=3)
        self.assertEqual(result, "3")
    
    def test_tc3_empty_list(self):
        """TC3: Edge case with empty list (n=0)"""
        # Input: no numbers
        # Output: "NONE"
        numbers = []
        result = clean_data(numbers, D=3)
        self.assertEqual(result, "NONE")
    
    def test_tc4_all_divisible(self):
        """TC4: Normal case where all numbers are divisible by D=3"""
        # Input: 3 6 9 12 (where n=4)
        # All are divisible by 3
        # Output: "3 6 9 12"
        numbers = [3, 6, 9, 12]
        result = clean_data(numbers, D=3)
        self.assertEqual(result, "3 6 9 12")
    
    def test_tc5_duplicates(self):
        """TC5: Edge case with duplicate numbers divisible by D=3"""
        # Input: 3 3 6 6 9 (where n=5)
        # Divisible by 3: [3, 3, 6, 6, 9]
        # After deduplication and sorting: "3 6 9"
        numbers = [3, 3, 6, 6, 9]
        result = clean_data(numbers, D=3)
        self.assertEqual(result, "3 6 9")


if __name__ == '__main__':
    unittest.main()
