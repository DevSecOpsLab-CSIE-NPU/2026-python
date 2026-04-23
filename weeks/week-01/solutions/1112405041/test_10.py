# 單元測試：主題 10（模組、類別、例外與 Big-O）

import unittest
from collections import deque
import importlib

# 動態導入 10_formal 模組
formal_10 = importlib.import_module('10_formal')
User = formal_10.User
demonstrate_deque = formal_10.demonstrate_deque
is_int = formal_10.is_int
safe_divide = formal_10.safe_divide

class TestModulesClassesExceptions(unittest.TestCase):
    
    def test_user_class(self):
        """測試 User 類別"""
        u = User(42)
        self.assertEqual(u.user_id, 42)
    
    def test_demonstrate_deque(self):
        """測試 deque 示範"""
        result = demonstrate_deque()
        self.assertEqual(result, [2, 3])
    
    def test_is_int_valid(self):
        """測試 is_int 有效輸入"""
        self.assertTrue(is_int('42'))
        self.assertTrue(is_int('0'))
    
    def test_is_int_invalid(self):
        """測試 is_int 無效輸入"""
        self.assertFalse(is_int('abc'))
        self.assertFalse(is_int('12.34'))
    
    def test_safe_divide_valid(self):
        """測試安全除法有效情況"""
        result = safe_divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_safe_divide_by_zero(self):
        """測試安全除法除以零"""
        result = safe_divide(10, 0)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
