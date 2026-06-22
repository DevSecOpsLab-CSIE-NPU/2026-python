import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task2_caesar_cipher import encrypt_line, solve


class TestEncryptLine(unittest.TestCase):

    def test_sample_shift3(self):
        result = encrypt_line("Hello, NPU!", 3)
        self.assertEqual(result, "Khoor, QSX!")

    def test_lowercase_wrap(self):
        result = encrypt_line("abc xyz", 3)
        self.assertEqual(result, "def abc")

    def test_uppercase_wrap(self):
        result = encrypt_line("XYZ", 3)
        self.assertEqual(result, "ABC")

    def test_non_letters_unchanged(self):
        result = encrypt_line("123 !@#", 8)
        self.assertEqual(result, "123 !@#")

    def test_empty_string(self):
        result = encrypt_line("", 8)
        self.assertEqual(result, "")

    def test_mixed_content_shift8(self):
        result = encrypt_line("Hello, World! 123", 8)
        expected = "Pmttw, Ewztl! 123"
        self.assertEqual(result, expected)

    def test_full_circle(self):
        result = encrypt_line("abcABC", 26)
        self.assertEqual(result, "abcABC")


class TestSolve(unittest.TestCase):

    def test_two_lines(self):
        input_data = "Hello, NPU!\nabc XYZ\n"
        expected = "Khoor, QSX!\ndef ABC\n"
        self.assertEqual(solve(input_data, 3), expected)

    def test_single_line(self):
        input_data = "test\n"
        expected = "bmab\n"
        self.assertEqual(solve(input_data, 8), expected)

    def test_empty_input(self):
        input_data = ""
        expected = ""
        self.assertEqual(solve(input_data, 8), expected)


if __name__ == "__main__":
    unittest.main()
