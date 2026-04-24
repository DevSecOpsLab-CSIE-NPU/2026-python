import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10056.py 中
# 並且您的解答會提供一個 calculate_probability(n, p, i) 函式：
# - n: 玩家總人數 (int)
# - p: 單次成功事件發生的機率 (float)
# - i: 目標玩家的順序 (int)
# 回傳格式化後的機率字串，精確到小數點後四位 (如 "0.5455")。
from solution_10056 import calculate_probability

class TestUVA10056(unittest.TestCase):
    
    def test_sample_case_1(self):
        """
        基礎測試 1：兩個玩家，成功機率約為 1/6 (0.166666)，求第 1 個玩家獲勝的機率。
        預期輸出為 "0.5455"
        """
        self.assertEqual(calculate_probability(2, 0.166666, 1), "0.5455")

    def test_sample_case_2(self):
        """
        基礎測試 2：兩個玩家，成功機率約為 1/6 (0.166666)，求第 2 個玩家獲勝的機率。
        預期輸出為 "0.4545"
        """
        self.assertEqual(calculate_probability(2, 0.166666, 2), "0.4545")

    def test_zero_probability(self):
        """
        陷阱測試：如果單次成功的機率為 0，任何玩家都不可能獲勝。
        演算法實作時若直接代入公式，分母 (1 - (1-p)^N) 會變成 (1 - 1) = 0，引發除以零錯誤。
        程式必須特別處理 p == 0 的情況。
        """
        self.assertEqual(calculate_probability(2, 0.0, 1), "0.0000")

    def test_one_probability(self):
        """邊界測試：如果成功機率為 1，第 1 個玩家擲骰子必定直接獲勝，後面的玩家勝率皆為 0。"""
        self.assertEqual(calculate_probability(5, 1.0, 1), "1.0000")
        self.assertEqual(calculate_probability(5, 1.0, 2), "0.0000")

if __name__ == '__main__':
    unittest.main()