import unittest
from main import BASE_MAP, digit_root, get_base, sum_digits_in_base


class TestQuestion3(unittest.TestCase):
    def test_get_base(self):
        self.assertEqual(get_base("1114405017"), 11)
        self.assertEqual(get_base("1114405018"), 13)

    def test_sum_digits_in_base(self):
        self.assertEqual(sum_digits_in_base(63, 11), 13)
        self.assertEqual(sum_digits_in_base(100, 11), 10)

    def test_digit_root(self):
        self.assertEqual(digit_root(63, 11), 3)
        self.assertEqual(digit_root(100, 11), 10)

    def test_digit_root_zero(self):
        self.assertEqual(digit_root(0, 11), 0)


if __name__ == "__main__":
    unittest.main()
