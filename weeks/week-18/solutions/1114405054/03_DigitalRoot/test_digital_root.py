import unittest
from digital_root import get_digital_root


class TestDigitalRoot(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_digital_root(0, 5), 0)

    def test_eight(self):
        self.assertEqual(get_digital_root(8, 5), 4)

    def test_sixty_three(self):
        self.assertEqual(get_digital_root(63, 5), 3)

    def test_equal_to_base(self):
        self.assertEqual(get_digital_root(5, 5), 1)

    def test_single_digit(self):
        self.assertEqual(get_digital_root(1, 5), 1)


if __name__ == "__main__":
    unittest.main()
