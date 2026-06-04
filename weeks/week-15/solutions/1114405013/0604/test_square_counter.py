"""平方數計數測試。"""

import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case_single_value_square(self):
        self.assertEqual(count_squares(1, 1), 1)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "a must be <= b"):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()
