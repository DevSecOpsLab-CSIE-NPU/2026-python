"""
單元測試：UVA 11005 — Cheapest Base

說明：
- 此檔使用 `unittest` 測試 `cheapest_bases` 函式的正確性。

執行指引：

# 在專案根目錄執行（PowerShell 範例）：
# $env:PYTHONPATH = "weeks/week-13/1114405006" ; python -m unittest -v weeks/week-13/1114405006/test_question_11005.py

"""

import unittest

from cheapest_base import cheapest_bases


class TestCheapestBase(unittest.TestCase):
    """包含多個情境的單元測試"""

    def test_zero_number_all_bases(self):
        """
        測試 N = 0 時，所有進位的表示皆為單一數字 '0'，成本相同。
        預期輸出為 2..36（全部進位）。
        """
        costs = list(range(36))  # 任意成本設定
        res = cheapest_bases(costs, 0)
        self.assertEqual(res, list(range(2, 37)))

    def test_all_ones_prefers_single_digit(self):
        """
        若所有字元成本都為 1，則成本等於位數長度。對於 N=10，
        當 base>=11 時為單一位數 'A'，因此應為最低成本。
        """
        costs = [1] * 36
        res = cheapest_bases(costs, 10)
        self.assertEqual(res, list(range(11, 37)))

    def test_custom_costs_prefer_A(self):
        """
        自訂成本使得字元 A (數值 10) 的成本遠低於其他字元，
        因此對於 N=10，base>=11（單一字元 A）應為最便宜。
        """
        costs = [100] * 36
        costs[10] = 1  # 將 'A' 的成本設為 1
        res = cheapest_bases(costs, 10)
        self.assertEqual(res, list(range(11, 37)))


if __name__ == "__main__":
    # 運行測試
    unittest.main()

