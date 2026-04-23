# 單元測試：主題 09（比較、排序與 key 函式）

import unittest
import sys
import importlib

# 動態導入 09_formal 模組
formal_09 = importlib.import_module('09_formal')
sort_by_uid = formal_09.sort_by_uid
find_min_max_by_key = formal_09.find_min_max_by_key
sort_tuples = formal_09.sort_tuples
sort_descending = formal_09.sort_descending
tuple_comparison = formal_09.tuple_comparison

class TestSortingComparison(unittest.TestCase):
    
    def test_sort_by_uid(self):
        """測試根據 uid 排序"""
        rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
        result = sort_by_uid(rows)
        self.assertEqual(result[0]['uid'], 1)
        self.assertEqual(result[2]['uid'], 3)
    
    def test_find_min_max(self):
        """測試找最小和最大值"""
        rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
        result = find_min_max_by_key(rows, 'uid')
        self.assertEqual(result['min']['uid'], 1)
        self.assertEqual(result['max']['uid'], 3)
    
    def test_sort_descending(self):
        """測試降序排列"""
        result = sort_descending([3, 1, 4, 1, 5])
        self.assertEqual(result, [5, 4, 3, 1, 1])
    
    def test_tuple_comparison(self):
        """測試 tuple 比較"""
        result = tuple_comparison()
        self.assertTrue(result['a_less_than_b'])
        self.assertTrue(result['x_less_than_y'])

if __name__ == '__main__':
    unittest.main()
