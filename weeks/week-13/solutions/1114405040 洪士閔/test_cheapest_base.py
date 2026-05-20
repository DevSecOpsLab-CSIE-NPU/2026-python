"""
針對 UVA 11005 - Cheapest Base 設計的 unit tests。
使用 Python 內建的 unittest 框架，檔案內包含中文註解與多個案例。
"""

import unittest
from cheapest_base import cheapest_bases


class TestCheapestBase(unittest.TestCase):
    def test_zero_returns_all_bases(self):
        # 測試：數字 0 在任何進位制皆為單一字元 '0'
        # 因此在所有進位下成本相同，預期回傳所有 base
        costs = [i for i in range(36)]  # 任意成本配置
        expected = list(range(2, 37))
        self.assertEqual(cheapest_bases(costs, 0), expected)

    def test_all_costs_equal(self):
        # 測試：若所有字元成本相同（例如都為 1），
        # 不同進位的總成本取決於表示法的位數，但至少應回傳一個或多個最小 base
        costs = [1] * 36
        res = cheapest_bases(costs, 12345)
        # 驗證回傳非空，且為升序排列
        self.assertTrue(len(res) >= 1)
        self.assertEqual(res, sorted(res))

    def test_preferred_base(self):
        # 測試：設計成本使某一進位最便宜
        # 這裡讓字元 '1' 很便宜，'0' 很貴，
        # 讓數字 10 在 base 9 表示為 '11'（成本低），在 base 10 為 '10'（成本高）
        costs = [10] * 36
        costs[1] = 1

        # 檢查結果應為 base 9
        self.assertEqual(cheapest_bases(costs, 10), [9])


if __name__ == "__main__":
    unittest.main()
