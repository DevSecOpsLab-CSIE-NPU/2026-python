# 單元測試：主題 04（for 迴圈）

import unittest
import importlib

# 動態導入 04_formal 模組
formal_04 = importlib.import_module('04_formal')
calculate_sum = formal_04.calculate_sum
calculate_squares = formal_04.calculate_squares
iterate_string = formal_04.iterate_string

class TestForLoop(unittest.TestCase):
    
    def test_calculate_sum(self):
        """測試總和計算"""
        self.assertEqual(calculate_sum([2, 4, 6]), 12)
        self.assertEqual(calculate_sum([1, 1, 1]), 3)
    
    def test_calculate_squares(self):
        """測試平方計算"""
        self.assertEqual(calculate_squares([2, 4, 6]), [4, 16, 36])
        self.assertEqual(calculate_squares([1, 2]), [1, 4])
    
    def test_iterate_string(self):
        """測試字串遍歷"""
        result = iterate_string('hello')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 'h')

if __name__ == '__main__':
    unittest.main()
