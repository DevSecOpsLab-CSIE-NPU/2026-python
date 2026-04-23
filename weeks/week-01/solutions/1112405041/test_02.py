# 單元測試：主題 02（基本資料型別）

import unittest
import importlib

# 動態導入 02_formal 模組
formal_02 = importlib.import_module('02_formal')
get_basic_types = formal_02.get_basic_types
convert_types = formal_02.convert_types

class TestBasicTypes(unittest.TestCase):
    
    def test_get_basic_types(self):
        """測試基本型別"""
        result = get_basic_types()
        self.assertIsInstance(result['int'], int)
        self.assertIsInstance(result['float'], float)
        self.assertIsInstance(result['str'], str)
        self.assertIsInstance(result['bool'], bool)
    
    def test_convert_types(self):
        """測試型別轉換"""
        result = convert_types()
        self.assertEqual(result['to_int'], 12)
        self.assertEqual(result['to_float'], 19.99)
        self.assertEqual(result['to_str'], '42')
    
    def test_int_conversion(self):
        """測試字串轉整數"""
        self.assertEqual(int('42'), 42)
        self.assertEqual(int('0'), 0)

if __name__ == '__main__':
    unittest.main()
