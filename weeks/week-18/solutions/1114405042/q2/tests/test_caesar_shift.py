import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from task_caesar_shift import caesar_encrypt


class TestCaesarShift(unittest.TestCase):

    def test_example_hello_npu(self):
        self.assertEqual(caesar_encrypt("Hello, NPU!"), "Khoor, QSX!")

    def test_example_abc_xyz(self):
        self.assertEqual(caesar_encrypt("abc XYZ"), "def ABC")

    def test_wraparound_lowercase(self):
        self.assertEqual(caesar_encrypt("xyz"), "abc")

    def test_wraparound_uppercase(self):
        self.assertEqual(caesar_encrypt("XYZ"), "ABC")

    def test_non_alpha_unchanged(self):
        self.assertEqual(caesar_encrypt("123 !@#"), "123 !@#")

    def test_empty_string(self):
        self.assertEqual(caesar_encrypt(""), "")

    def test_mixed_content(self):
        self.assertEqual(caesar_encrypt("Test123!?"), "Whvw123!?")

    def test_full_alphabet_lower(self):
        self.assertEqual(caesar_encrypt("abcdefghijklmnopqrstuvwxyz"), "defghijklmnopqrstuvwxyzabc")

    def test_full_alphabet_upper(self):
        self.assertEqual(caesar_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "DEFGHIJKLMNOPQRSTUVWXYZABC")


if __name__ == "__main__":
    unittest.main()
