import unittest

# 導入解答程式
# from solution_10929 import solve_10929

class TestMultipleOfEleven(unittest.TestCase):
    """
    測試 UVA 10929 - Multiple of 11
    測試判斷大整數是否為 11 的倍數
    """
    
    def is_multiple_of_11(self, num_str):
        """
        使用奇偶位差法判斷是否為 11 的倍數
        奇數位（從右數）數字之和 - 偶數位數字之和
        """
        total = 0
        for i, digit in enumerate(reversed(num_str)):
            # 位置從 0 開始（最右邊）
            if i % 2 == 0:  # 奇數位（1, 3, 5, ...）
                total += int(digit)
            else:  # 偶數位（2, 4, 6, ...）
                total -= int(digit)
        return total % 11 == 0
    
    def test_eleven_itself(self):
        """測試 11：是 11 的倍數"""
        self.assertTrue(self.is_multiple_of_11("11"))
    
    def test_twenty_two(self):
        """測試 22：是 11 的倍數"""
        self.assertTrue(self.is_multiple_of_11("22"))
    
    def test_thirty_three(self):
        """測試 33：是 11 的倍數"""
        self.assertTrue(self.is_multiple_of_11("33"))
    
    def test_not_multiple(self):
        """測試 10：不是 11 的倍數"""
        self.assertFalse(self.is_multiple_of_11("10"))
    
    def test_large_multiple(self):
        """測試大數字 121：是 11 的倍數"""
        self.assertTrue(self.is_multiple_of_11("121"))
    
    def test_large_non_multiple(self):
        """測試大數字 123：不是 11 的倍數"""
        self.assertFalse(self.is_multiple_of_11("123"))
    
    def test_zero(self):
        """測試 0：是 11 的倍數"""
        self.assertTrue(self.is_multiple_of_11("0"))
    
    def test_very_large_number(self):
        """測試很大的數字 12345654321"""
        # 12345654321 應該是 11 的倍數
        self.assertTrue(self.is_multiple_of_11("12345654321"))

if __name__ == '__main__':
    unittest.main()
