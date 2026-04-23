# 單元測試：主題 07（函式與 Lambda）

import unittest
import importlib

# 動態導入 07_formal 模組
formal_07 = importlib.import_module('07_formal')
double = formal_07.double
sort_by_key = formal_07.sort_by_key
map_operation = formal_07.map_operation
filter_even = formal_07.filter_even

class TestFunctionsLambda(unittest.TestCase):
    
    def test_double(self):
        """測試 double 函式"""
        self.assertEqual(double(5), 10)
        self.assertEqual(double(0), 0)
    
    def test_sort_by_key(self):
        """測試根據 key 排序"""
        rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
        result = sort_by_key(rows, 'score')
        self.assertEqual(result[0]['score'], 75)
    
    def test_map_operation(self):
        """測試 map 操作"""
        result = map_operation([1, 2, 3], 2)
        self.assertEqual(result, [2, 4, 6])
    
    def test_filter_even(self):
        """測試 filter 偶數"""
        result = filter_even([1, 2, 3, 4, 5])
        self.assertEqual(result, [2, 4])

if __name__ == '__main__':
    unittest.main()
