import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_multi_digit(self):
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(38), 2)
        self.assertEqual(digit_root(987), 6)

    def test_single_digit(self):
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(9), 9)

    def test_large_number(self):
        self.assertEqual(digit_root(2000000000), 2)
        self.assertEqual(digit_root(999999999), 9)

    def test_zero_raises(self):
        with self.assertRaises(ValueError) as cm:
            digit_root(0)
        self.assertEqual(str(cm.exception), "n must be >= 1")

    def test_negative_raises(self):
        with self.assertRaises(ValueError) as cm:
            digit_root(-1)
        self.assertEqual(str(cm.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
