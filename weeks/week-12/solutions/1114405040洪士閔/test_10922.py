"""
題目 10922 的單元測試

測試 q10922_solution.py 中的函數
"""

import unittest
from q10922_solution import calculate_digit_sum, calculate_degree


class TestCalculateDigitSum(unittest.TestCase):
    """測試 calculate_digit_sum 函數"""
    
    def test_single_digit(self):
        """測試單位數"""
        self.assertEqual(calculate_digit_sum("9"), 9)
        self.assertEqual(calculate_digit_sum("5"), 5)
    
    def test_two_digits(self):
        """測試兩位數"""
        self.assertEqual(calculate_digit_sum("18"), 9)  # 1+8=9
        self.assertEqual(calculate_digit_sum("27"), 9)  # 2+7=9
    
    def test_three_digits(self):
        """測試三位數"""
        self.assertEqual(calculate_digit_sum("999"), 27)  # 9+9+9=27
    
    def test_large_number(self):
        """測試大數字"""
        self.assertEqual(calculate_digit_sum("123456789"), 45)  # 1+2+...+9=45


class TestCalculateDegree(unittest.TestCase):
    """測試 calculate_degree 函數"""
    
    def test_single_digit_nine(self):
        """測試單位數 9（深度=0）"""
        self.assertEqual(calculate_degree("9"), 0)
    
    def test_two_digit_multiple(self):
        """測試兩位數 9 的倍數：18（1+8=9，深度=1）"""
        self.assertEqual(calculate_degree("18"), 1)
    
    def test_three_digit_multiple(self):
        """測試三位數 9 的倍數：999（9+9+9=27, 2+7=9，深度=2）"""
        self.assertEqual(calculate_degree("999"), 2)
    
    def test_large_multiple(self):
        """測試大數字 9 的倍數：123456789"""
        # 1+2+...+9=45, 4+5=9，深度=2
        self.assertEqual(calculate_degree("123456789"), 2)
    
    def test_nine_nines(self):
        """測試多個 9：999999999"""
        # 9+9+9+9+9+9+9+9+9=81, 8+1=9，深度=2
        self.assertEqual(calculate_degree("999999999"), 2)


class TestMultiplesOf9(unittest.TestCase):
    """測試 9 的倍數的深度計算"""
    
    def test_multiples_sequence(self):
        """測試一系列 9 的倍數"""
        test_cases = [
            ("9", 0),      # 9: 深度 0
            ("18", 1),     # 18: 1+8=9, 深度 1
            ("27", 1),     # 27: 2+7=9, 深度 1
            ("36", 1),     # 36: 3+6=9, 深度 1
                ("99", 2),     # 99: 9+9=18, 1+8=9, 深度 2
            ("108", 1),    # 108: 1+0+8=9, 深度 1
            ("999", 2),    # 999: 9+9+9=27, 2+7=9, 深度 2
        ]
        for num_str, expected_degree in test_cases:
            with self.subTest(num_str=num_str):
                self.assertEqual(calculate_degree(num_str), expected_degree)


if __name__ == '__main__':
    unittest.main(verbosity=2)
