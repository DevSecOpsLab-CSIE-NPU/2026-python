import unittest
import os
import sys

ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import question299 as q299

class TestQuestion299(unittest.TestCase):
    def test_count_swaps(self):
        self.assertEqual(q299.count_swaps([1, 3, 2]), 1)
        self.assertEqual(q299.count_swaps([3, 2, 1]), 3)

    def test_solve_299(self):
        input_data = '3\n3\n1 3 2\n3\n3 2 1\n2\n2 1\n'
        expected = ('Optimal train swapping takes 1 swaps.\n'
                    'Optimal train swapping takes 3 swaps.\n'
                    'Optimal train swapping takes 1 swaps.')
        self.assertEqual(q299.solve_299(input_data), expected)

if __name__ == '__main__':
    unittest.main()
