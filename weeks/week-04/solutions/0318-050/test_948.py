import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_948.py 中
# 並且您的解答會提供一個 find_fake_coin(n, k, weighings) 函式：
# - n: 硬幣總數 (int)
# - k: 秤重次數 (int)
# - weighings: 秤重紀錄列表，格式為 [(左盤硬幣列表, 右盤硬幣列表, 秤重結果字串)]
# 回傳值預期為假幣的編號 (int)；如果無法明確判定，則回傳 0。
from solution_948 import find_fake_coin

class TestUVA948(unittest.TestCase):
    
    def test_single_weighing_equal(self):
        """
        基礎測試：測試單次秤重且結果相等 (=) 的情況。
        當左盤和右盤一樣重時，代表盤子上的所有硬幣都是「真幣」。
        因此，剩下的那枚硬幣必定是假幣。
        """
        n = 5
        k = 1
        weighings = [
            ([1, 2], [3, 4], '=')
        ]
        # 1, 2, 3, 4 都是真幣，假幣一定是 5
        self.assertEqual(find_fake_coin(n, k, weighings), 5)

    def test_undetermined_fake_coin(self):
        """
        無法判定測試：測試線索不足以找出唯一假幣的情況。
        如果只知道 1, 2 總重量小於 3, 4，我們無法確認假幣是哪一個
        (可能是 1, 2 其中一個比較輕，也可能是 3, 4 其中一個比較重)。
        """
        n = 5
        k = 1
        weighings = [
            ([1, 2], [3, 4], '<')
        ]
        # 資訊不足，預期回傳 0
        self.assertEqual(find_fake_coin(n, k, weighings), 0)

    def test_complex_logic_deduction(self):
        """
        進階邏輯測試：需要綜合多次秤重結果才能找出假幣的情況。
        """
        n = 5
        k = 2
        weighings = [
            ([1, 2], [3, 4], '<'),  # 第一次：1, 2 比 3, 4 輕 (假幣在 1~4 中，5為真幣)
            ([1, 2], [5, 4], '=')   # 第二次：1, 2 和 5, 4 一樣重 (代表 1, 2, 4, 5 皆為真幣)
        ]
        # 綜合以上兩次結果，假幣必定是 3，且它比較重
        self.assertEqual(find_fake_coin(n, k, weighings), 3)

if __name__ == '__main__':
    unittest.main()