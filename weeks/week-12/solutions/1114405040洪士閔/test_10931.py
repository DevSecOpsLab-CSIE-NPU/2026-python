"""
題目 10931 的單元測試

測試 q10931_solution.py 中的函數
"""

import unittest
from q10931_solution import calculate_parity


class TestCalculateParity(unittest.TestCase):
    """測試 calculate_parity 函數"""
    
    def test_single_bit_one(self):
        """測試 1（二進位：1）"""
        binary, parity = calculate_parity(1)
        self.assertEqual(binary, "1")
        self.assertEqual(parity, 1)
    
    def test_single_bit_zero(self):
        """測試 0（二進位：0）"""
        binary, parity = calculate_parity(0)
        self.assertEqual(binary, "0")
        self.assertEqual(parity, 0)
    
    def test_two(self):
        """測試 2（二進位：10）"""
        binary, parity = calculate_parity(2)
        self.assertEqual(binary, "10")
        self.assertEqual(parity, 1)
    
    def test_three(self):
        """測試 3（二進位：11）"""
        binary, parity = calculate_parity(3)
        self.assertEqual(binary, "11")
        self.assertEqual(parity, 2)
    
    def test_five(self):
        """測試 5（二進位：101）"""
        binary, parity = calculate_parity(5)
        self.assertEqual(binary, "101")
        self.assertEqual(parity, 2)
    
    def test_ten(self):
        """測試 10（二進位：1010）"""
        binary, parity = calculate_parity(10)
        self.assertEqual(binary, "1010")
        self.assertEqual(parity, 2)
    
    def test_fifteen(self):
        """測試 15（二進位：1111）"""
        binary, parity = calculate_parity(15)
        self.assertEqual(binary, "1111")
        self.assertEqual(parity, 4)
    
    def test_twenty_one(self):
        """測試 21（二進位：10101）"""
        binary, parity = calculate_parity(21)
        self.assertEqual(binary, "10101")
        self.assertEqual(parity, 3)
    
    def test_power_of_two(self):
        """測試 2 的冪"""
        # 8 = 2^3 (二進位：1000)
        binary, parity = calculate_parity(8)
        self.assertEqual(binary, "1000")
        self.assertEqual(parity, 1)
        
        # 16 = 2^4 (二進位：10000)
        binary, parity = calculate_parity(16)
        self.assertEqual(binary, "10000")
        self.assertEqual(parity, 1)
    
    def test_all_ones(self):
        """測試全 1 的數"""
        # 7 = 111 (二進位：111)
        binary, parity = calculate_parity(7)
        self.assertEqual(binary, "111")
        self.assertEqual(parity, 3)
        
        # 31 = 11111 (二進位：11111)
        binary, parity = calculate_parity(31)
        self.assertEqual(binary, "11111")
        self.assertEqual(parity, 5)
    
    def test_large_number(self):
        """測試大數字"""
        # 1023 = 1111111111 (10 個 1)
        binary, parity = calculate_parity(1023)
        self.assertEqual(binary, "1111111111")
        self.assertEqual(parity, 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
