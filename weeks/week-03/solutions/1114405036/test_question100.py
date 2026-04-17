import unittest
import os
import sys

ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import question100 as q100

class TestQuestion100(unittest.TestCase):
    def test_cycle_length(self):
        self.assertEqual(q100.cycle_length(1), 1)
        self.assertEqual(q100.cycle_length(22), 16)

    def test_max_cycle_length(self):
        self.assertEqual(q100.max_cycle_length(1, 10), 20)
        self.assertEqual(q100.max_cycle_length(100, 200), 125)

    def test_solve_100(self):
        input_data = '1 10\n100 200\n201 210\n900 1000\n'
        expected = '1 10 20\n100 200 125\n201 210 89\n900 1000 174'
        self.assertEqual(q100.solve_100(input_data), expected)

if __name__ == '__main__':
    unittest.main()
