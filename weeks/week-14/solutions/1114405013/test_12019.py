"""
問題：UVA 12019 — Doom's Day Algorithm（世界末日演算法）
題目來源：https://zerojudge.tw/ShowProblem?problemid=f709

題意摘要：
使用 Doom's Day 演算法計算 2012 年任意日期是星期幾。
演算法核心：每年某些特定日期（Doomsday）落在同一個星期幾。
  2012 年的 Doomsday 是星期三（Wednesday）。
每個月的 Doomsday 對應日期：Jan 10, Feb 21, Mar 7, Apr 4, May 9,
                               Jun 6, Jul 11, Aug 8, Sep 5,
                               Oct 10, Nov 7, Dec 12
"""

import unittest

# 從解題程式中匯入被測試的函式與常數
from p12019 import day_of_week, DOOMSDAY


class TestDoomsDay(unittest.TestCase):
    """UVA 12019 Doom's Day Algorithm 的單元測試"""

    def test_doomsday_itself(self):
        """測試 Doomsday 本身（2012/1/10）應為 Wednesday"""
        self.assertEqual(day_of_week(1, 10), "Wednesday")

    def test_known_date_jan1(self):
        """測試 2012/1/1（元旦）是 Monday"""
        # 計算：1/1 距離 1/10（Doomsday）差 -9 天
        # -9 mod 7 = 5 → Wednesday + 5 = Monday
        self.assertEqual(day_of_week(1, 1), "Monday")

    def test_known_date_feb29(self):
        """測試 2012/2/29（閏日）是 Thursday"""
        # 計算：2/29 距離 2/21（Doomsday）差 8 天
        # 8 mod 7 = 1 → Wednesday + 1 = Thursday
        self.assertEqual(day_of_week(2, 29), "Thursday")

    def test_known_date_dec25(self):
        """測試 2012/12/25（聖誕節）是 Tuesday"""
        self.assertEqual(day_of_week(12, 25), "Tuesday")

    def test_known_date_jul4(self):
        """測試 2012/7/4（美國獨立日）是 Wednesday"""
        self.assertEqual(day_of_week(7, 4), "Wednesday")

    def test_known_date_oct31(self):
        """測試 2012/10/31（萬聖節）是 Wednesday"""
        self.assertEqual(day_of_week(10, 31), "Wednesday")

    def test_known_date_feb14(self):
        """測試 2012/2/14（情人節）是 Wednesday"""
        # 計算：2/14 距離 2/21（Doomsday）差 -7 天
        # -7 mod 7 = 0 → Wednesday + 0 = Wednesday
        self.assertEqual(day_of_week(2, 14), "Wednesday")

    def test_all_doomsday_dates(self):
        """測試每個月的 Doomsday 都是 Wednesday"""
        for month, date in DOOMSDAY.items():
            with self.subTest(month=month, date=date):
                self.assertEqual(day_of_week(month, date), "Wednesday")


if __name__ == "__main__":
    unittest.main()
