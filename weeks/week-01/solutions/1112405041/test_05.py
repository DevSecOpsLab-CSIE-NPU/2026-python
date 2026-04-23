# 單元測試：主題 05（索引與切片）

import unittest
import importlib

# 動態導入 05_formal 模組
formal_05 = importlib.import_module('05_formal')
string_indexing = formal_05.string_indexing
list_slicing = formal_05.list_slicing

class TestIndexingSlicing(unittest.TestCase):
    
    def test_string_indexing(self):
        """測試字串索引"""
        result = string_indexing()
        self.assertEqual(result['first'], 'a')
        self.assertEqual(result['last'], 'g')
        self.assertEqual(result['mid'], 'cde')
    
    def test_list_slicing(self):
        """測試 list 切片"""
        result = list_slicing()
        self.assertEqual(result['last_two'], [40, 50])
        self.assertEqual(result['first_three'], [10, 20, 30])
        self.assertEqual(result['every_other'], [10, 30, 50])
    
    def test_negative_index(self):
        """測試負索引"""
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(lst[-1], 5)
        self.assertEqual(lst[-2], 4)

if __name__ == '__main__':
    unittest.main()
