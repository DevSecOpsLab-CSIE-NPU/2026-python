# 單元測試：主題 08（容器操作與推導式）

import unittest
import sys
import importlib

# 動態導入 08_formal 模組
formal_08 = importlib.import_module('08_formal')
filter_positive = formal_08.filter_positive
double_values = formal_08.double_values
create_dict_from_pairs = formal_08.create_dict_from_pairs
invert_dict = formal_08.invert_dict
unique_squares = formal_08.unique_squares
sum_of_squares = formal_08.sum_of_squares
replace_negative_with_zero = formal_08.replace_negative_with_zero

class TestComprehensions(unittest.TestCase):
    
    def test_filter_positive(self):
        """測試篩選正數"""
        result = filter_positive([1, -2, 3, -4])
        self.assertEqual(result, [1, 3])
    
    def test_double_values(self):
        """測試雙倍"""
        result = double_values([1, 2, 3])
        self.assertEqual(result, [2, 4, 6])
    
    def test_create_dict(self):
        """測試建立字典"""
        pairs = [('a', 1), ('b', 2)]
        result = create_dict_from_pairs(pairs)
        self.assertEqual(result, {'a': 1, 'b': 2})
    
    def test_invert_dict(self):
        """測試反轉字典"""
        result = invert_dict({'a': 1, 'b': 2})
        self.assertEqual(result, {1: 'a', 2: 'b'})
    
    def test_sum_of_squares(self):
        """測試平方和"""
        result = sum_of_squares([1, 2, 3])
        self.assertEqual(result, 14)

if __name__ == '__main__':
    unittest.main()
