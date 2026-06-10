import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(digit_root(24), 6)
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(9999), 9)

    def test_edge_cases(self):
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(10), 1)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)

        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(-1)

    def test_large_number(self):
        self.assertEqual(digit_root(2_000_000_000), 2)
        self.assertEqual(digit_root(1_999_999_999), 1)


if __name__ == "__main__":
    unittest.main()
