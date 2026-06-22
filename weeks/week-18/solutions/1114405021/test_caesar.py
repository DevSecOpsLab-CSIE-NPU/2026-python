import unittest
from io import StringIO
import sys

import caesar


class TestCaesarCipher(unittest.TestCase):
    def test_basic_lowercase(self):
        self.assertEqual(caesar.encrypt_line("abc"), "cde")

    def test_basic_uppercase(self):
        self.assertEqual(caesar.encrypt_line("XYZ"), "ZAB")

    def test_wrap_around(self):
        self.assertEqual(caesar.encrypt_line("yz"), "ab")
        self.assertEqual(caesar.encrypt_line("YZ"), "AB")

    def test_mixed_case(self):
        self.assertEqual(caesar.encrypt_line("Hello"), "Jgnnq")

    def test_non_letters_unchanged(self):
        self.assertEqual(caesar.encrypt_line("A1b2!"), "C1d2!")

    def test_empty_line(self):
        self.assertEqual(caesar.encrypt_line(""), "")

    def test_full_sample(self):
        input_data = "Hello World!\nabc XYZ\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        caesar.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "Jgnnq Yqtnf!\ncde ZAB")

    def test_multiple_lines(self):
        input_data = "a\nb\nc\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        caesar.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "c\nd\ne")


if __name__ == "__main__":
    unittest.main()
