import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?ÆÂ?Ê∏¨Ë©¶Ôºö‰∏ªÈ°?04Ôºàfor Ëø¥Â?Ôº?

import unittest
import importlib

# ?ïÊ?Â∞éÂÖ• 04_formal Ê®°Á?
formal_04 = importlib.import_module('04_hand')
calculate_sum = formal_04.calculate_sum
calculate_squares = formal_04.calculate_squares
iterate_string = formal_04.iterate_string

class TestForLoop(unittest.TestCase):
    
    def test_calculate_sum(self):
        """Ê∏¨Ë©¶Á∏ΩÂ?Ë®àÁ?"""
        self.assertEqual(calculate_sum([2, 4, 6]), 12)
        self.assertEqual(calculate_sum([1, 1, 1]), 3)
    
    def test_calculate_squares(self):
        """Ê∏¨Ë©¶Âπ≥ÊñπË®àÁ?"""
        self.assertEqual(calculate_squares([2, 4, 6]), [4, 16, 36])
        self.assertEqual(calculate_squares([1, 2]), [1, 4])
    
    def test_iterate_string(self):
        """Ê∏¨Ë©¶Â≠ó‰∏≤?çÊ≠∑"""
        result = iterate_string('hello')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 'h')

if __name__ == '__main__':
    unittest.main()
