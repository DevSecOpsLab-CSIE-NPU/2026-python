import unittest
from task1_sequence_clean import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):
    
    def test_normal_case(self):
        """Test with normal input containing unique and duplicate numbers."""
        result = remove_duplicates([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_repeated_numbers_case(self):
        """Test with repeated numbers, keeping first occurrence order."""
        result = remove_duplicates([1, 2, 2, 3, 1, 4, 3])
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_empty_list_case(self):
        """Test with empty list."""
        result = remove_duplicates([])
        self.assertEqual(result, [])
    
    def test_all_duplicates(self):
        """Test when all elements are the same."""
        result = remove_duplicates([5, 5, 5, 5])
        self.assertEqual(result, [5])
    
    def test_single_element(self):
        """Test with single element."""
        result = remove_duplicates([42])
        self.assertEqual(result, [42])


if __name__ == "__main__":
    unittest.main()