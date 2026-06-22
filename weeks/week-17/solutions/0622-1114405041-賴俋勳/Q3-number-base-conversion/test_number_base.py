import unittest
from number_base_conversion import convert_to_base


class TestNumberBaseConversion(unittest.TestCase):
    """
    題目：任意進位的數字轉換 - 30分
    
    輸入說明：
    - 每行輸入一個十進位數字 n (0 ≤ n ≤ 10^9)
    - 是 EOF 表示結束
    
    輸出說明：
    - 對於每個十進位數字，輸出其進位轉換結果
    - base 位數 (2,3,5,6,7,8,9,11,13,16) (依據題目)
    
    範例 (base = 8)：
    輸入: 0, 8, 63
    輸出: 0, 10, 77
    """
    
    def test_zero_conversion(self):
        """基本測試：0 轉換"""
        result = convert_to_base(0, base=8)
        self.assertEqual(result, "0")
    
    def test_single_digit_conversion(self):
        """基本測試：單位數轉換"""
        result = convert_to_base(8, base=8)
        self.assertEqual(result, "10")
    
    def test_multi_digit_conversion(self):
        """測試：多位數轉換"""
        result = convert_to_base(63, base=8)
        self.assertEqual(result, "77")
    
    def test_binary_conversion(self):
        """測試：二進位轉換"""
        result = convert_to_base(10, base=2)
        self.assertEqual(result, "1010")
    
    def test_hexadecimal_conversion(self):
        """測試：十六進位轉換"""
        result = convert_to_base(255, base=16)
        self.assertEqual(result, "FF")
    
    def test_large_number_conversion(self):
        """測試：大數字轉換"""
        result = convert_to_base(1000000000, base=8)
        self.assertIsNotNone(result)
    
    def test_base_3_conversion(self):
        """測試：三進位轉換"""
        result = convert_to_base(9, base=3)
        self.assertEqual(result, "100")
    
    def test_base_5_conversion(self):
        """測試：五進位轉換"""
        result = convert_to_base(25, base=5)
        self.assertEqual(result, "100")


if __name__ == '__main__':
    unittest.main()
