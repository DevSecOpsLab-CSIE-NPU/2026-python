import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?08ï¼ˆå®¹?¨æ?ä½œè??¨å?å¼ï?

import unittest
import sys
import importlib

# ?•æ?å°å…¥ 08_formal æ¨¡ç?
formal_08 = importlib.import_module('08_hand')
filter_positive = formal_08.filter_positive
double_values = formal_08.double_values
create_dict_from_pairs = formal_08.create_dict_from_pairs
invert_dict = formal_08.invert_dict
unique_squares = formal_08.unique_squares
sum_of_squares = formal_08.sum_of_squares
replace_negative_with_zero = formal_08.replace_negative_with_zero

class TestComprehensions(unittest.TestCase):
    
    def test_filter_positive(self):
        """æ¸¬è©¦ç¯©é¸æ­?•¸"""
        result = filter_positive([1, -2, 3, -4])
        self.assertEqual(result, [1, 3])
    
    def test_double_values(self):
        """æ¸¬è©¦?™å€?""
        result = double_values([1, 2, 3])
        self.assertEqual(result, [2, 4, 6])
    
    def test_create_dict(self):
        """æ¸¬è©¦å»ºç?å­—å…¸"""
        pairs = [('a', 1), ('b', 2)]
        result = create_dict_from_pairs(pairs)
        self.assertEqual(result, {'a': 1, 'b': 2})
    
    def test_invert_dict(self):
        """æ¸¬è©¦?è?å­—å…¸"""
        result = invert_dict({'a': 1, 'b': 2})
        self.assertEqual(result, {1: 'a', 2: 'b'})
    
    def test_sum_of_squares(self):
        """æ¸¬è©¦å¹³æ–¹??""
        result = sum_of_squares([1, 2, 3])
        self.assertEqual(result, 14)

if __name__ == '__main__':
    unittest.main()
