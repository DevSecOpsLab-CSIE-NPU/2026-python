# 單元測試：主題 03（基本容器型別）

import unittest
import importlib

# 動態導入 03_formal 模組
formal_03 = importlib.import_module('03_formal')
manage_containers = formal_03.manage_containers

class TestContainers(unittest.TestCase):
    
    def test_manage_containers(self):
        """測試容器操作"""
        result = manage_containers()
        self.assertIn(4, result['list'])
        self.assertEqual(result['tuple'], (4, 5))
        self.assertIn(4, result['set'])
        self.assertIn('GOOGL', result['dict'])
    
    def test_list_append(self):
        """測試 list 新增"""
        lst = [1, 2, 3]
        lst.append(4)
        self.assertEqual(len(lst), 4)
    
    def test_dict_access(self):
        """測試 dict 存取"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(d['a'], 1)

if __name__ == '__main__':
    unittest.main()
