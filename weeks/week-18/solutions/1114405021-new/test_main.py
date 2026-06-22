import unittest
from io import StringIO
import sys

import main


class TestCaesarCipher(unittest.TestCase):
    def test_uppercase_wrap(self):
        self.assertEqual(main.shift_char("Z", 1), "A")

    def test_lowercase_wrap(self):
        self.assertEqual(main.shift_char("z", 1), "a")

    def test_preserve_non_letter(self):
        self.assertEqual(main.shift_char("!", 1), "!")

    def test_encrypt_simple_word(self):
        self.assertEqual(main.encrypt_line("abc"), "cde")

    def test_encrypt_mixed_case(self):
        self.assertEqual(main.encrypt_line("YyZz"), "AaBb")

    def test_encrypt_with_spaces(self):
        self.assertEqual(main.encrypt_line("Hello World"), "Jgnnq Yqtnf")

    def test_encrypt_with_punctuation(self):
        self.assertEqual(main.encrypt_line("a,b.c!"), "c,d.e!")

    def test_multiple_lines(self):
        input_data = "abc\nXYZ\nHello, World!\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out
        try:
            main.main()
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = old_stdout
        self.assertEqual(out.getvalue(), "cde\nZAB\nJgnnq, Yqtnf!\n")

    def test_empty_line(self):
        self.assertEqual(main.encrypt_line(""), "")

    def test_full_cycle(self):
        self.assertEqual(main.encrypt_line("AaZz"), "CcBb")


if __name__ == "__main__":
    unittest.main()