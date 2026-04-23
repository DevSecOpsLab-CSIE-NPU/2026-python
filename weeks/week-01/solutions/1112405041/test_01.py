# 單元測試：主題 01（變數與指定）

import unittest
import importlib

# 動態導入 01_formal 模組
formal_01 = importlib.import_module('01_formal')
get_point = formal_01.get_point
demonstrate_assignment = formal_01.demonstrate_assignment

class TestAssignment(unittest.TestCase):
    
    def test_get_point(self):
        """測試 get_point 函式"""
        result = get_point()
        self.assertEqual(result, (4, 9))
    
    def test_demonstrate_assignment(self):
        """測試 demonstrate_assignment 函式"""
        result = demonstrate_assignment()
        self.assertEqual(result['x'], 3)
        self.assertEqual(result['name'], 'ACME')
        self.assertEqual(result['y'], 5)
        self.assertEqual(result['px'], 4)
        self.assertEqual(result['py'], 9)
    
    def test_tuple_unpacking(self):
        """測試 tuple 解包"""
        a, b = 1, 2
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)

if __name__ == '__main__':
    unittest.main()
