# 單元測試：主題 06（可迭代物件）

import unittest
import importlib

# 動態導入 06_formal 模組
formal_06 = importlib.import_module('06_formal')
consume_iterable = formal_06.consume_iterable
demonstrate_iterator_exhaustion = formal_06.demonstrate_iterator_exhaustion
filter_iterable = formal_06.filter_iterable

class TestIterable(unittest.TestCase):
    
    def test_consume_iterable(self):
        """測試消耗 iterable"""
        count = consume_iterable([1, 2, 3, 4, 5])
        self.assertEqual(count, 5)
    
    def test_iterator_exhaustion(self):
        """測試 iterator 耗盡"""
        result = demonstrate_iterator_exhaustion()
        self.assertEqual(result['first_pass'], [(1, 3), (2, 4)])
        self.assertEqual(result['second_pass'], [])
    
    def test_filter_iterable(self):
        """測試過濾"""
        result = filter_iterable([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [3, 4, 5])

if __name__ == '__main__':
    unittest.main()
