import unittest
from q2 import caesar_cipher


class TestCaesarCipher(unittest.TestCase):

    def test_mixed_case_with_punctuation(self):
        self.assertEqual(caesar_cipher("Hello, NPU!", 5), "Mjqqt, SUZ!")

    def test_upper_and_lower(self):
        self.assertEqual(caesar_cipher("abc XYZ", 5), "fgh CDE")

    def test_wrap_around_uppercase_V(self):
        self.assertEqual(caesar_cipher("V", 5), "A")

    def test_wrap_around_uppercase_Z(self):
        self.assertEqual(caesar_cipher("Z", 5), "E")

    def test_non_letters_unchanged(self):
        self.assertEqual(caesar_cipher("123 !@#", 5), "123 !@#")


if __name__ == "__main__":
    unittest.main()
