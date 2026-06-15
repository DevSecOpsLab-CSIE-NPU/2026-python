import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?06ï¼ˆå¯è¿­ä»£?©ä»¶ï¼?

import unittest
import importlib

# ?•æ?å°å…¥ 06_formal æ¨¡ç?
formal_06 = importlib.import_module('06_hand')
consume_iterable = formal_06.consume_iterable
demonstrate_iterator_exhaustion = formal_06.demonstrate_iterator_exhaustion
filter_iterable = formal_06.filter_iterable

class TestIterable(unittest.TestCase):
    
    def test_consume_iterable(self):
        """æ¸¬è©¦æ¶ˆè€?iterable"""
        count = consume_iterable([1, 2, 3, 4, 5])
        self.assertEqual(count, 5)
    
    def test_iterator_exhaustion(self):
        """æ¸¬è©¦ iterator ?—ç›¡"""
        result = demonstrate_iterator_exhaustion()
        self.assertEqual(result['first_pass'], [(1, 3), (2, 4)])
        self.assertEqual(result['second_pass'], [])
    
    def test_filter_iterable(self):
        """æ¸¬è©¦?æ¿¾"""
        result = filter_iterable([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [3, 4, 5])

if __name__ == '__main__':
    unittest.main()
