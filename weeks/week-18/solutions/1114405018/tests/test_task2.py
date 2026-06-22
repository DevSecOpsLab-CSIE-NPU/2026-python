import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from task2_caesar_cipher import caesar_encrypt, solve_caesar


class TestCaesarCipher(unittest.TestCase):

    def test_sample_shift3(self):
        self.assertEqual(caesar_encrypt("Hello, NPU!", 3), "Khoor, QSX!")

    def test_sample_shift3_abc(self):
        self.assertEqual(caesar_encrypt("abc XYZ", 3), "def ABC")

    def test_shift9_hello(self):
        self.assertEqual(caesar_encrypt("Hello, NPU!", 9), "Qnuux, WYD!")

    def test_shift9_abc(self):
        self.assertEqual(caesar_encrypt("abc XYZ", 9), "jkl GHI")

    def test_wrap_uppercase(self):
        self.assertEqual(caesar_encrypt("XYZ", 3), "ABC")

    def test_wrap_lowercase(self):
        self.assertEqual(caesar_encrypt("xyz", 3), "abc")

    def test_non_alpha_unchanged(self):
        self.assertEqual(caesar_encrypt("123 !@#", 5), "123 !@#")

    def test_empty_string(self):
        self.assertEqual(caesar_encrypt("", 9), "")

    def test_large_shift(self):
        self.assertEqual(caesar_encrypt("abc", 26 + 3), "def")

    def test_shift0(self):
        self.assertEqual(caesar_encrypt("Hello", 0), "Hello")

    def test_mixed_content(self):
        self.assertEqual(caesar_encrypt("a1b2C!z", 1), "b1c2D!a")

    def test_solve_caesar_multiline(self):
        data = "Hello, NPU!\nabc XYZ\n"
        result = solve_caesar(data, 9)
        self.assertEqual(result, "Qnuux, WYD!\njkl GHI")

    def test_solve_caesar_trailing_newline(self):
        data = "Hello\nWorld\n"
        result = solve_caesar(data, 9)
        self.assertEqual(result, "Qnuux\nFxaum")


if __name__ == '__main__':
    unittest.main()
