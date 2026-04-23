# 單元測試：主題 12（字串格式化）

import unittest
import sys
import importlib

# 動態導入 12_formal 模組
formal_12 = importlib.import_module('12_formal')
format_price = formal_12.format_price
format_with_method = formal_12.format_with_method
format_precision = formal_12.format_precision
number_bases = formal_12.number_bases

class TestStringFormatting(unittest.TestCase):
    
    def test_format_price_fstring(self):
        """測試 f-string 格式化"""
        result = format_price('ACME', 91.1)
        self.assertEqual(result, 'ACME price = 91.10')
    
    def test_format_price_method(self):
        """測試 format 方法"""
        result = format_with_method('ACME', 91.1)
        self.assertEqual(result, 'ACME price = 91.10')
    
    def test_format_precision(self):
        """測試浮點數精度"""
        result = format_precision(3.14159, 2)
        self.assertEqual(result, '3.14')
    
    def test_number_bases(self):
        """測試進位制轉換"""
        result = number_bases(255)
        self.assertEqual(result['hex'], 'ff')
        self.assertEqual(result['binary'], '11111111')
        self.assertEqual(result['octal'], '377')

if __name__ == '__main__':
    unittest.main()
