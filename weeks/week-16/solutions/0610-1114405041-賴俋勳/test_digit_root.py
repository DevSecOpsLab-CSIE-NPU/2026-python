import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_multi_step(self):
        self.assertEqual(digit_root(199), 1)

    def test_edge_single_digit(self):
        self.assertEqual(digit_root(5), 5)

    def test_edge_large_number(self):
        self.assertEqual(digit_root(2_000_000_000), 2)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "^n must be >= 1$"):
            digit_root(0)


if __name__ == "__main__":
    unittest.main()
