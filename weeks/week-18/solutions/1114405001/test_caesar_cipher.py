"""
Caesar Cipher (SHIFT=2) Test Cases
"""
import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    """Test Caesar Cipher with SHIFT = 2"""
    
    def test_basic_lowercase_and_special_chars(self):
        """Test Case 1: Basic functionality with lowercase and special characters"""
        input_text = "Hello, NPU!"
        expected = "Jgnnq, PQW!"
        self.assertEqual(caesar_cipher(input_text), expected)
    
    def test_wrap_around_edge_case(self):
        """Test Case 2: Edge case - letter wrapping (X→Z, Y→A, Z→B)"""
        input_text = "xyz XYZ"
        expected = "zab ZAB"
        self.assertEqual(caesar_cipher(input_text), expected)
    
    def test_mixed_with_digits_and_symbols(self):
        """Test Case 3: Mixed case, digits, and special symbols"""
        input_text = "abc123!@# ABC"
        expected = "cde123!@# CDE"
        self.assertEqual(caesar_cipher(input_text), expected)
    
    def test_all_uppercase(self):
        """Test Case 4: All uppercase letters"""
        input_text = "ABCXYZ"
        expected = "CDCZAB"
        self.assertEqual(caesar_cipher(input_text), expected)
    
    def test_only_special_chars(self):
        """Test Case 5: Only special characters and spaces (no letters)"""
        input_text = "123 !@# $%^"
        expected = "123 !@# $%^"
        self.assertEqual(caesar_cipher(input_text), expected)


if __name__ == '__main__':
    unittest.main()
