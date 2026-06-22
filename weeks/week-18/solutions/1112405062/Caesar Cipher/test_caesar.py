import unittest
from caesar import caesar_encrypt


class TestCaesarEncrypt(unittest.TestCase):

    def test_basic_mixed_case(self):
        self.assertEqual(caesar_encrypt("Hello, NPU!"), "Khoor, QSX!")

    def test_lowercase_only(self):
        self.assertEqual(caesar_encrypt("abc"), "def")

    def test_uppercase_wrap(self):
        self.assertEqual(caesar_encrypt("XYZ"), "ABC")

    def test_with_non_letters(self):
        self.assertEqual(caesar_encrypt("abc123! xyz"), "def123! abc")

    def test_empty_string(self):
        self.assertEqual(caesar_encrypt(""), "")

    def test_only_non_letters(self):
        self.assertEqual(caesar_encrypt("123 !@#"), "123 !@#")

    def test_lowercase_wrap(self):
        self.assertEqual(caesar_encrypt("z"), "c")

    def test_uppercase_wrap(self):
        self.assertEqual(caesar_encrypt("Z"), "C")


if __name__ == '__main__':
    unittest.main()
