import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10050.py 中
# 並且您的解答會提供一個 count_hartals(n, parties) 函式：
# - n: 模擬的天數 (int)
# - parties: 包含各政黨罷會參數的整數串列 (list of ints)
# 回傳損失的工作天數 (int)。
from solution_10050 import count_hartals

class TestUVA10050(unittest.TestCase):
    
    def test_sample_case(self):
        """
        基礎測試：題目敘述中提供的範例。
        N = 14 天，政黨參數為 3, 4, 8。
        罷會發生在第 3, 4, 8, 9, 12 天。第 6 天雖然參數是 3 的倍數，但是星期五 (假日) 不算。
        預期損失 5 個工作天。
        """
        self.assertEqual(count_hartals(14, [3, 4, 8]), 5)

    def test_overlapping_hartals(self):
        """
        重疊測試：多個政黨在同一天罷會，只能算損失 1 個工作天。
        N = 14 天，政黨參數為 2, 4。
        罷會發生在 2, 4, 6(假日), 8, 10, 12, 14(假日)。
        預期損失 5 個工作天 (2, 4, 8, 10, 12)。
        """
        self.assertEqual(count_hartals(14, [2, 4]), 5)

    def test_holiday_only_hartals(self):
        """
        假日陷阱測試：罷會剛好都落在假日 (星期五或星期六)。
        N = 14 天，政黨參數為 7 (每逢週六罷會)。
        因為第 7, 14 天都是假日，不會損失任何工作天。
        """
        self.assertEqual(count_hartals(14, [7]), 0)
        # 測試每 14 天罷會一次 (剛好都落在週六)
        self.assertEqual(count_hartals(30, [14]), 0)

    def test_no_parties(self):
        """
        邊界測試：若政黨沒有提交任何罷會參數 (空陣列)。
        預期損失 0 個工作天。
        """
        self.assertEqual(count_hartals(100, []), 0)
        
    def test_large_days(self):
        """極端值測試：模擬一年 (365天)"""
        self.assertEqual(count_hartals(365, [13, 21]), 35)

if __name__ == '__main__':
    unittest.main()