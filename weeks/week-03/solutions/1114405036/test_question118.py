import unittest
import os
import sys

ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import question118 as q118

class TestQuestion118(unittest.TestCase):
    def test_simulation(self):
        input_data = '5 3\n1 1 E\nRFRFRFRF\n3 2 N\nFRRFLLFFRRFLL\n0 3 W\nLLFFFLFLFL\n'
        expected = '1 1 E\n3 3 N LOST\n2 3 S'
        self.assertEqual(q118.solve_118(input_data), expected)

if __name__ == '__main__':
    unittest.main()
