"""
第二題測試：凱撒密碼
"""

import unittest

from p2_caesar_cipher import caesar_cipher, shift_char


class TestCaesarCipher(unittest.TestCase):
    def test_uppercase_should_wrap(self):
        self.assertEqual(shift_char("Z"), "D")

    def test_lowercase_should_wrap(self):
        self.assertEqual(shift_char("z"), "d")

    def test_non_letter_should_not_change(self):
        self.assertEqual(caesar_cipher("123 !?"), "123 !?")

    def test_sample_with_shift_four(self):
        input_text = "Hello, NPU!\nabc XYZ\n"
        expected = "Lipps, RTY!\nefg BCD\n"
        self.assertEqual(caesar_cipher(input_text), expected)


if __name__ == "__main__":
    unittest.main()
