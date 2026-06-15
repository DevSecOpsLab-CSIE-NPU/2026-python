import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?ÆÂ?Ê∏¨Ë©¶Ôºö‰∏ªÈ°?07ÔºàÂáΩÂºèË? LambdaÔº?

import unittest
import importlib

# ?ïÊ?Â∞éÂÖ• 07_formal Ê®°Á?
formal_07 = importlib.import_module('07_hand')
double = formal_07.double
sort_by_key = formal_07.sort_by_key
map_operation = formal_07.map_operation
filter_even = formal_07.filter_even

class TestFunctionsLambda(unittest.TestCase):
    
    def test_double(self):
        """Ê∏¨Ë©¶ double ?ΩÂ?"""
        self.assertEqual(double(5), 10)
        self.assertEqual(double(0), 0)
    
    def test_sort_by_key(self):
        """Ê∏¨Ë©¶?πÊ? key ?íÂ?"""
        rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
        result = sort_by_key(rows, 'score')
        self.assertEqual(result[0]['score'], 75)
    
    def test_map_operation(self):
        """Ê∏¨Ë©¶ map ?ç‰?"""
        result = map_operation([1, 2, 3], 2)
        self.assertEqual(result, [2, 4, 6])
    
    def test_filter_even(self):
        """Ê∏¨Ë©¶ filter ?∂Êï∏"""
        result = filter_even([1, 2, 3, 4, 5])
        self.assertEqual(result, [2, 4])

if __name__ == '__main__':
    unittest.main()
