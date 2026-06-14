import unittest
try:
    from square_counter import count_squares
except ImportError:
    count_squares = None

class TestCountSquares(unittest.TestCase):
    def test_basic_range(self): self.assertEqual(count_squares(1, 10), 3)
    def test_edge_case(self): self.assertEqual(count_squares(1, 1), 1)
    def test_invalid_input(self):
        with self.assertRaises(ValueError): count_squares(5, 2)

if __name__ == '__main__':
    unittest.main()
