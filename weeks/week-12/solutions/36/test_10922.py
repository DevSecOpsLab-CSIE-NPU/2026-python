import unittest

# 導入解答程式
# from solution_10922 import solve_10922

class TestTwoTheNines(unittest.TestCase):
    """
    測試 UVA 10922 - 2 the 9s
    測試 9 的倍數判斷和 9 的深度計算
    """
    
    def calculate_digit_sum(self, num_str):
        """計算數字和"""
        return sum(int(d) for d in num_str)
    
    def test_nine_multiple_9(self):
        """測試 9：是 9 的倍數，深度 1"""
        self.assertEqual(self.calculate_digit_sum("9"), 9)
    
    def test_nine_multiple_18(self):
        """測試 18：是 9 的倍數"""
        result = self.calculate_digit_sum("18")  # 1+8=9
        self.assertEqual(result, 9)
    
    def test_nine_multiple_999(self):
        """測試 999：是 9 的倍數"""
        result = self.calculate_digit_sum("999")  # 9+9+9=27
        result2 = self.calculate_digit_sum("27")  # 2+7=9
        self.assertEqual(result2, 9)
    
    def test_not_nine_multiple_10(self):
        """測試 10：不是 9 的倍數"""
        result = self.calculate_digit_sum("10")  # 1+0=1
        self.assertNotEqual(result, 9)
    
    def test_nine_multiple_large_number(self):
        """測試大數字 123456789：是 9 的倍數"""
        result = self.calculate_digit_sum("123456789")  # 1+2+3+4+5+6+7+8+9=45
        result2 = self.calculate_digit_sum("45")  # 4+5=9
        self.assertEqual(result2, 9)

if __name__ == '__main__':
    unittest.main()
