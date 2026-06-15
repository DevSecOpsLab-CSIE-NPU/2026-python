import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?10ï¼ˆæ¨¡çµ„ã€é??¥ã€ä?å¤–è? Big-Oï¼?

import unittest
from collections import deque
import importlib

# ?•æ?å°å…¥ 10_formal æ¨¡ç?
formal_10 = importlib.import_module('10_hand')
User = formal_10.User
demonstrate_deque = formal_10.demonstrate_deque
is_int = formal_10.is_int
safe_divide = formal_10.safe_divide

class TestModulesClassesExceptions(unittest.TestCase):
    
    def test_user_class(self):
        """æ¸¬è©¦ User é¡åˆ¥"""
        u = User(42)
        self.assertEqual(u.user_id, 42)
    
    def test_demonstrate_deque(self):
        """æ¸¬è©¦ deque ç¤ºç?"""
        result = demonstrate_deque()
        self.assertEqual(result, [2, 3])
    
    def test_is_int_valid(self):
        """æ¸¬è©¦ is_int ?‰æ?è¼¸å…¥"""
        self.assertTrue(is_int('42'))
        self.assertTrue(is_int('0'))
    
    def test_is_int_invalid(self):
        """æ¸¬è©¦ is_int ?¡æ?è¼¸å…¥"""
        self.assertFalse(is_int('abc'))
        self.assertFalse(is_int('12.34'))
    
    def test_safe_divide_valid(self):
        """æ¸¬è©¦å®‰å…¨?¤æ??‰æ??…æ?"""
        result = safe_divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_safe_divide_by_zero(self):
        """æ¸¬è©¦å®‰å…¨?¤æ??¤ä»¥??""
        result = safe_divide(10, 0)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
