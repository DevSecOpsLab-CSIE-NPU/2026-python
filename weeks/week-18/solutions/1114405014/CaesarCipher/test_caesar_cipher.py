import unittest

from caesar_cipher import caesar_cipher, process_text


class TestCaesarCipher(unittest.TestCase):

    def test_uppercase_letters_shift(self):
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")

    def test_lowercase_letters_shift(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_preserve_non_letters(self):
        self.assertEqual(caesar_cipher("Hello, NPU! 123", 3), "Khoor, QSX! 123")

    def test_uppercase_wrap_around(self):
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

    def test_lowercase_wrap_around(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")

    def test_empty_string(self):
        self.assertEqual(caesar_cipher("", 3), "")

    def test_shift_one(self):
        self.assertEqual(caesar_cipher("Az az", 1), "Ba ba")

    def test_shift_ten(self):
        self.assertEqual(caesar_cipher("ABC xyz", 10), "KLM hij")

    def test_process_multiple_lines_until_eof(self):
        input_text = "Hello, NPU!\nabc XYZ\n"
        expected = "Khoor, QSX!\ndef ABC\n"

        self.assertEqual(process_text(input_text, 3), expected)

    def test_process_keeps_blank_lines(self):
        input_text = "abc\n\nXYZ\n"
        expected = "def\n\nABC\n"

        self.assertEqual(process_text(input_text, 3), expected)


if __name__ == "__main__":
    unittest.main()