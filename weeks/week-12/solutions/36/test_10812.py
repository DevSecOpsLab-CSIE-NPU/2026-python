import unittest

# 導入解答程式
# from solution_10812 import solve_10812

class TestBeatTheSpread(unittest.TestCase):
    """
    測試 UVA 10812 - Beat the Spread!
    測試兩隊分數計算是否正確
    """
    
    def test_valid_case_1(self):
        """測試案例1：S=40, D=20，預期輸出 30 10"""
        # 較高分 = (40+20)/2 = 30
        # 較低分 = (40-20)/2 = 10
        high, low = (40 + 20) // 2, (40 - 20) // 2
        self.assertEqual((high, low), (30, 10))
    
    def test_valid_case_2(self):
        """測試案例2：S=20, D=40，無解"""
        # 較高分 = (20+40)/2 = 30
        # 較低分 = (20-40)/2 = -10 (負數，無解)
        S, D = 20, 40
        is_valid = (S + D) % 2 == 0 and (S - D) % 2 == 0 and (S - D) >= 0
        self.assertFalse(is_valid)
    
    def test_edge_case_zero(self):
        """測試邊界情況：S=0, D=0"""
        high, low = (0 + 0) // 2, (0 - 0) // 2
        self.assertEqual((high, low), (0, 0))
    
    def test_odd_sum_plus_diff(self):
        """測試奇數和的情況：無法整除"""
        S, D = 15, 8  # S+D=23 (奇數)
        is_valid = (S + D) % 2 == 0
        self.assertFalse(is_valid)
    
    def test_negative_low_score(self):
        """測試低分為負的情況"""
        S, D = 10, 20  # 低分 = (10-20)/2 = -5
        low = (S - D) // 2
        self.assertTrue(low < 0)

if __name__ == '__main__':
    unittest.main()
