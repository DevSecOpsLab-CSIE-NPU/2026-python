import unittest

# 解題函數
def solve_beat_the_spread(S, D):
    """
    求解兩隊分數。
    
    給定兩隊分數的和 S 和差 D（絕對值），
    計算兩隊各自的得分（較大的先輸出）。
    
    參數:
        S (int): 兩隊分數的和
        D (int): 兩隊分數的差（絕對值）
    
    返回:
        tuple: 若有解則返回 (較大分數, 較小分數)；
               若無解則返回 None
    """
    # 檢查 S + D 是否為偶數
    # 如果 S + D 不是偶數，則較高分無法是整數
    if (S + D) % 2 != 0:
        return None
    
    # 檢查 S - D 是否為偶數
    # 如果 S - D 不是偶數，則較低分無法是整數
    if (S - D) % 2 != 0:
        return None
    
    # 計算較高分
    higher_score = (S + D) // 2
    
    # 計算較低分
    lower_score = (S - D) // 2
    
    # 檢查分數是否都是非負數
    if lower_score < 0:
        return None
    
    # 返回較大的分數先輸出
    return (higher_score, lower_score)


class TestBeatTheSpread(unittest.TestCase):
    """
    為 UVA 10812 - Beat the Spread! 設計的單元測試類別
    """
    
    def test_normal_case_1(self):
        """
        測試: 正常情況 1
        輸入: S=40, D=20
        預期輸出: (30, 10)
        驗證: 30 + 10 = 40, |30 - 10| = 20
        """
        result = solve_beat_the_spread(40, 20)
        self.assertEqual(result, (30, 10))
    
    def test_normal_case_2(self):
        """
        測試: 正常情況 2
        輸入: S=100, D=50
        預期輸出: (75, 25)
        驗證: 75 + 25 = 100, |75 - 25| = 50
        """
        result = solve_beat_the_spread(100, 50)
        self.assertEqual(result, (75, 25))
    
    def test_impossible_case_1(self):
        """
        測試: 不可能情況 1（題目範例）
        輸入: S=20, D=40
        預期輸出: None (impossible)
        原因: (S - D) / 2 = (20 - 40) / 2 = -10（負數）
        """
        result = solve_beat_the_spread(20, 40)
        self.assertIsNone(result)
    
    def test_impossible_case_2(self):
        """
        測試: 不可能情況 2（S + D 為奇數）
        輸入: S=10, D=3
        預期輸出: None (impossible)
        原因: (S + D) = 13 為奇數，無法整除以 2
        """
        result = solve_beat_the_spread(10, 3)
        self.assertIsNone(result)
    
    def test_impossible_case_3(self):
        """
        測試: 不可能情況 3（S - D 為奇數）
        輸入: S=11, D=2
        預期輸出: None (impossible)
        原因: (S - D) = 9 為奇數，無法整除以 2
        """
        result = solve_beat_the_spread(11, 2)
        self.assertIsNone(result)
    
    def test_zero_difference(self):
        """
        測試: 兩隊平手（差為 0）
        輸入: S=30, D=0
        預期輸出: (15, 15)
        驗證: 15 + 15 = 30, |15 - 15| = 0
        """
        result = solve_beat_the_spread(30, 0)
        self.assertEqual(result, (15, 15))
    
    def test_zero_sum(self):
        """
        測試: 總分為 0（都沒得分）
        輸入: S=0, D=0
        預期輸出: (0, 0)
        驗證: 0 + 0 = 0, |0 - 0| = 0
        """
        result = solve_beat_the_spread(0, 0)
        self.assertEqual(result, (0, 0))
    
    def test_one_team_zero_score(self):
        """
        測試: 一隊得分為 0
        輸入: S=20, D=20
        預期輸出: (20, 0)
        驗證: 20 + 0 = 20, |20 - 0| = 20
        """
        result = solve_beat_the_spread(20, 20)
        self.assertEqual(result, (20, 0))
    
    def test_large_numbers(self):
        """
        測試: 大數字情況
        輸入: S=1000, D=500
        預期輸出: (750, 250)
        驗證: 750 + 250 = 1000, |750 - 250| = 500
        """
        result = solve_beat_the_spread(1000, 500)
        self.assertEqual(result, (750, 250))
    
    def test_odd_sum_even_difference(self):
        """
        測試: 和為奇數、差為偶數
        輸入: S=25, D=10
        預期輸出: None (impossible)
        原因: (S + D) = 35 為奇數，無法得到整數分數
        """
        result = solve_beat_the_spread(25, 10)
        self.assertIsNone(result)
    
    def test_negative_result(self):
        """
        測試: 計算結果出現負數
        輸入: S=5, D=20
        預期輸出: None (impossible)
        原因: (S - D) / 2 = (5 - 20) / 2 = -7.5（負數且不是整數）
        """
        result = solve_beat_the_spread(5, 20)
        self.assertIsNone(result)


if __name__ == '__main__':
    # 運行所有測試
    unittest.main()
