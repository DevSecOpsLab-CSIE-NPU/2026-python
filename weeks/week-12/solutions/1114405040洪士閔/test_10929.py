"""
題目 10929 的單元測試

測試 q10929_solution.py 中的函數
"""

import unittest
from q10929_solution import is_multiple_of_11


class TestIsMultipleOf11(unittest.TestCase):
    """測試 is_multiple_of_11 函數"""
    
    def test_single_digit_11(self):
        """測試單位數 11（特殊情況）"""
        # 11 是 11 的倍數
        self.assertTrue(is_multiple_of_11("11"))
    
    def test_two_digit_11(self):
        """測試兩位數 11"""
        self.assertTrue(is_multiple_of_11("11"))
    
    def test_two_digit_22(self):
        """測試兩位數 22（2×11）"""
        self.assertTrue(is_multiple_of_11("22"))
    
    def test_two_digit_not_multiple(self):
        """測試兩位數 12（不是 11 的倍數）"""
        self.assertFalse(is_multiple_of_11("12"))
    
    def test_three_digit_121(self):
        """測試三位數 121（11×11）"""
        self.assertTrue(is_multiple_of_11("121"))
    
    def test_three_digit_1210(self):
        """測試四位數 1210（11×110）"""
        self.assertTrue(is_multiple_of_11("1210"))
    
    def test_three_digit_not_multiple(self):
        """測試三位數 123（不是 11 的倍數）"""
        self.assertFalse(is_multiple_of_11("123"))
    
    def test_zero(self):
        """測試 0"""
        self.assertTrue(is_multiple_of_11("0"))
    
    def test_large_multiple(self):
        """測試大數字"""
        # 999999 = 11 × 90909
        self.assertTrue(is_multiple_of_11("999999"))
    
    def test_large_not_multiple(self):
        """測試大數字（不是倍數）"""
        # 1000000 不是 11 的倍數
        self.assertFalse(is_multiple_of_11("1000000"))
    
    def test_alternating_digits(self):
        """測試交替數字"""
        # 121212 = 11 × 11010 + 2，不是倍數
        # 但 121212 - 2 = 121210 = 11 × 11019 + 1，不確定
        # 計算：1-2+1-2+1-2=1-2+1-2+1-2=-3，-3 % 11 = 8 ≠ 0
        self.assertFalse(is_multiple_of_11("121212"))
    
    def test_palindrome_number(self):
        """測試回文數 11"""
        self.assertTrue(is_multiple_of_11("11"))
    
    def test_official_example1(self):
        """測試官方範例 1"""
        self.assertTrue(is_multiple_of_11("110"))
    
    def test_official_example2(self):
        """測試官方範例 2"""
        self.assertTrue(is_multiple_of_11("121"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
