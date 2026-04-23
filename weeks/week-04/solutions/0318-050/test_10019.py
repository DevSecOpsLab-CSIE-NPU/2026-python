import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10019.py 中
# 並且您的解答會提供一個 calculate_difference(a, b) 函式：
# 接收兩個整數 a 與 b (代表 Hashmat 與敵人的士兵數量)
# 回傳兩者之間的差值 (必須為正數/絕對值)。
from solution_10019 import calculate_difference

class TestUVA10019(unittest.TestCase):
    
    def test_hashmat_less_than_enemy(self):
        """
        基礎測試：Hashmat 的士兵數量少於敵人士兵數量的情況。
        預期輸出為兩者的差值 (正數)。
        """
        self.assertEqual(calculate_difference(10, 12), 2)

    def test_hashmat_greater_than_enemy(self):
        """
        反向測試：雖然題目敘述中提到「Hashmat 的士兵數絕不會比敵人的士兵數大」，
        但在實際的測資中，輸入的兩個數字順序可能會顛倒 (Hashmat 及敵人的士兵數或反之)。
        因此程式必須能處理第一個數字大於第二個數字的情況，並回傳絕對值。
        """
        self.assertEqual(calculate_difference(14, 10), 4)

    def test_equal_soldiers(self):
        """
        邊界測試：兩軍士兵數量相等的情況，預期差值為 0。
        """
        self.assertEqual(calculate_difference(100, 100), 0)

    def test_large_numbers(self):
        """
        極端值測試：測資保證數字不會超過 2^63 (題目上的 263 實際上是 2^63 的排版遺失)。
        雖然 Python 預設即支援無上限的大數運算，但加入此測試以確保極端測資的邏輯無誤。
        """
        self.assertEqual(calculate_difference(2**62, 2**63 - 1), (2**63 - 1) - 2**62)

if __name__ == '__main__':
    unittest.main()