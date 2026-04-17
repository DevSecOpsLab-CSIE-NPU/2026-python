import unittest
import os
import sys

ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import question490 as q490

class TestQuestion490(unittest.TestCase):
    def test_rotate_text(self):
        lines = ['HELLO', 'WORLD']
        expected = ['WH', 'OE', 'RL', 'LL', 'DO']
        self.assertEqual(q490.rotate_text(lines), expected)

if __name__ == '__main__':
    unittest.main()
