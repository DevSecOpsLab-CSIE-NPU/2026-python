"""
UVA 10812 — Beat the Spread! 測試程式
題目說明：超級盃賭局中，根據兩隊的分數之和 S 和分數之差 D，
求出兩隊各自的得分（較大的先輸出）。

解題原理：
- 設高分隊伍得分為 x，低分隊伍得分為 y
- 可建立方程式組：
  x + y = S （分數之和）
  x - y = D （分數之差的絕對值）
- 解得：
  x = (S + D) / 2 （較高分）
  y = (S - D) / 2 （較低分）
- 必須滿足的條件：
  1. x 和 y 都必須是非負整數
  2. (S + D) 和 (S - D) 都必須是偶數
  3. y >= 0（即 S - D >= 0 且 S - D 是偶數）
"""

import unittest


def solve_beat_the_spread(S, D):
    """
    根據分數之和和分數之差計算兩隊的得分。
    
    參數:
        S (int): 兩隊分數之和
        D (int): 兩隊分數之差的絕對值
    
    返回:
        tuple: 若有解，返回 (較高分, 較低分)；若無解，返回 None
    
    條件檢查:
        - 高分 = (S + D) / 2
        - 低分 = (S - D) / 2
        - S + D 必須為偶數（才能整除 2）
        - 低分必須非負（S >= D）
        - 兩個分數都必須非負
    """
    
    # 檢查 S + D 是否為偶數
    # 如果不是偶數，無法得到整數解
    if (S + D) % 2 != 0:
        return None
    
    # 計算較高分和較低分
    higher_score = (S + D) // 2
    lower_score = (S - D) // 2
    
    # 檢查較低分是否為非負整數
    # 若 lower_score < 0，表示無解
    if lower_score < 0:
        return None
    
    # 返回結果（較大分數在前）
    return (higher_score, lower_score)


class TestBeatTheSpread(unittest.TestCase):
    """
    UVA 10812 問題的單元測試類別。
    
    測試項目包括：
    1. 正常情況的計算
    2. 邊界情況（如其中一隊得分為 0）
    3. 無解的情況
    4. 相同得分的情況
    """
    
    def test_normal_case_1(self):
        """
        測試正常情況 1
        輸入：S = 40, D = 20
        預期輸出：(30, 10)
        說明：30 + 10 = 40, 30 - 10 = 20 ✓
        """
        result = solve_beat_the_spread(40, 20)
        self.assertEqual(result, (30, 10))
    
    def test_normal_case_2(self):
        """
        測試正常情況 2
        輸入：S = 20, D = 40
        預期輸出：None（無解）
        說明：若 S < D，則 (S - D) / 2 < 0，無法有非負分數
        """
        result = solve_beat_the_spread(20, 40)
        self.assertIsNone(result)
    
    def test_edge_case_zero_difference(self):
        """
        測試邊界情況：兩隊分數相同（差為 0）
        輸入：S = 30, D = 0
        預期輸出：(15, 15)
        說明：15 + 15 = 30, 15 - 15 = 0 ✓
        """
        result = solve_beat_the_spread(30, 0)
        self.assertEqual(result, (15, 15))
    
    def test_edge_case_one_team_zero_score(self):
        """
        測試邊界情況：其中一隊得分為 0
        輸入：S = 20, D = 20
        預期輸出：(20, 0)
        說明：20 + 0 = 20, 20 - 0 = 20 ✓
        """
        result = solve_beat_the_spread(20, 20)
        self.assertEqual(result, (20, 0))
    
    def test_impossible_odd_sum_plus_diff(self):
        """
        測試無解情況 1：S + D 為奇數
        輸入：S = 15, D = 10
        預期輸出：None
        說明：S + D = 25（奇數），無法整除 2
        """
        result = solve_beat_the_spread(15, 10)
        self.assertIsNone(result)
    
    def test_impossible_negative_score(self):
        """
        測試無解情況 2：計算出負數分數
        輸入：S = 5, D = 15
        預期輸出：None
        說明：較低分 = (5 - 15) / 2 = -5（負數），無解
        """
        result = solve_beat_the_spread(5, 15)
        self.assertIsNone(result)
    
    def test_large_numbers(self):
        """
        測試大數字情況
        輸入：S = 1000000, D = 999998
        預期輸出：(999999, 1)
        說明：999999 + 1 = 1000000, 999999 - 1 = 999998 ✓
        """
        result = solve_beat_the_spread(1000000, 999998)
        self.assertEqual(result, (999999, 1))
    
    def test_both_zero(self):
        """
        測試兩隊都得分為 0 的情況
        輸入：S = 0, D = 0
        預期輸出：(0, 0)
        說明：0 + 0 = 0, 0 - 0 = 0 ✓
        """
        result = solve_beat_the_spread(0, 0)
        self.assertEqual(result, (0, 0))
    
    def test_small_difference(self):
        """
        測試差值很小的情況
        輸入：S = 100, D = 2
        預期輸出：(51, 49)
        說明：51 + 49 = 100, 51 - 49 = 2 ✓
        """
        result = solve_beat_the_spread(100, 2)
        self.assertEqual(result, (51, 49))
    
    def test_return_type_is_tuple(self):
        """
        測試返回值類型
        確保當有解時返回的是 tuple，無解時返回 None
        """
        # 有解的情況
        result = solve_beat_the_spread(40, 20)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        
        # 無解的情況
        result = solve_beat_the_spread(20, 40)
        self.assertIsNone(result)


def print_test_explanation():
    """
    列印測試說明和題目解析
    """
    print("=" * 60)
    print("UVA 10812 — Beat the Spread! 單元測試")
    print("=" * 60)
    print("\n題目說明:")
    print("- 超級盃賭局中，根據分數之和 S 和分數之差 D")
    print("- 計算兩隊各自的得分（較大的先輸出）")
    print("\n數學公式:")
    print("- 較高分 = (S + D) / 2")
    print("- 較低分 = (S - D) / 2")
    print("\n有效條件:")
    print("1. (S + D) 必須為偶數")
    print("2. (S - D) 必須為偶數（即 S 和 D 同奇偶）")
    print("3. 較低分必須 >= 0（即 S >= D）")
    print("\n無解情況:")
    print("- 如果 S < D")
    print("- 如果 (S + D) 為奇數")
    print("- 如果 (S - D) 為奇數")
    print("\n" + "=" * 60 + "\n")


if __name__ == '__main__':
    # 列印測試說明
    print_test_explanation()
    
    # 執行單元測試
    unittest.main(verbosity=2)
