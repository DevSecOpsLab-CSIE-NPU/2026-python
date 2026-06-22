import unittest
from main import caesar_shift, get_shift


class TestQuestion2(unittest.TestCase):
    def test_get_shift(self):
        self.assertEqual(get_shift("1114405017"), 8)

    def test_caesar_shift_letters(self):
        self.assertEqual(caesar_shift("Hello, NPU!", 8), "Pmttw, VXC!")
        self.assertEqual(caesar_shift("abc XYZ", 8), "ijk FGH")

    def test_caesar_shift_non_letters_preserved(self):
        self.assertEqual(caesar_shift("123! @", 8), "123! @")


if __name__ == "__main__":
    unittest.main()
