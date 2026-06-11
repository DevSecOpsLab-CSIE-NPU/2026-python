import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        # example from the prompt
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(24), 6)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_case_large_and_single_digit(self):
        # single-digit should return itself
        self.assertEqual(digit_root(5), 5)
        # large value near upper bound
        self.assertEqual(digit_root(2000000000), 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0)  # reduces to 2

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError) as cm:
            digit_root(0)
        self.assertEqual(str(cm.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
