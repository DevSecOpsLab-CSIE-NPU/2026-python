import unittest

from caesar_shift import encrypt_line, shift_char


class CaesarShiftTests(unittest.TestCase):
    def test_uppercase_wraps(self):
        self.assertEqual(shift_char("Z", 3), "C")

    def test_lowercase_wraps(self):
        self.assertEqual(shift_char("z", 3), "c")

    def test_preserves_non_letters(self):
        self.assertEqual(shift_char(" ", 5), " ")

    def test_encrypt_keeps_punctuation(self):
        self.assertEqual(encrypt_line("Hello, World!", 3), "Khoor, Zruog!")

    def test_encrypt_handles_mixed_case(self):
        self.assertEqual(encrypt_line("aZy", 2), "cBa")


if __name__ == "__main__":
    unittest.main()