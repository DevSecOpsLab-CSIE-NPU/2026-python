"""
題目 12019 - Doom's Day Algorithm (計算星期幾) 測試程式
使用 Doom's Day 演算法判斷 2012 年任意日期是星期幾
"""

import unittest
from solution_12019 import get_day_of_week


class TestDoomsDayAlgorithm(unittest.TestCase):
    """Doom's Day 演算法的單元測試"""

    def test_doomsday_itself_may(self):
        """測試 5 月的 Doomsday（5 月 9 日）應該是星期三"""
        # 2012 年 5 月 9 日是 Doomsday，應該是星期三 (Wednesday)
        self.assertEqual(get_day_of_week(5, 9), "Wednesday")

    def test_doomsday_itself_apr(self):
        """測試 4 月的 Doomsday（4 月 4 日）應該是星期三"""
        # 2012 年 4 月 4 日是 Doomsday，應該是星期三
        self.assertEqual(get_day_of_week(4, 4), "Wednesday")

    def test_doomsday_itself_june(self):
        """測試 6 月的 Doomsday（6 月 6 日）應該是星期三"""
        # 2012 年 6 月 6 日是 Doomsday，應該是星期三
        self.assertEqual(get_day_of_week(6, 6), "Wednesday")

    def test_may_10(self):
        """測試 5 月 10 日（在 Doomsday 之後 1 天）"""
        # 5 月 9 日是星期三，所以 5 月 10 日是星期四
        self.assertEqual(get_day_of_week(5, 10), "Thursday")

    def test_may_8(self):
        """測試 5 月 8 日（在 Doomsday 之前 1 天）"""
        # 5 月 9 日是星期三，所以 5 月 8 日是星期二
        self.assertEqual(get_day_of_week(5, 8), "Tuesday")

    def test_april_7(self):
        """測試 4 月 7 日（在 Doomsday 之後 3 天）"""
        # 4 月 4 日是星期三，所以 4 月 7 日是星期六
        self.assertEqual(get_day_of_week(4, 7), "Saturday")

    def test_april_1(self):
        """測試 4 月 1 日（在 Doomsday 之前 3 天）"""
        # 4 月 4 日是星期三，所以 4 月 1 日是星期日
        self.assertEqual(get_day_of_week(4, 1), "Sunday")

    def test_january_10(self):
        """測試 1 月的 Doomsday（1 月 10 日）"""
        # 1 月 10 日是 Doomsday，應該是星期三
        self.assertEqual(get_day_of_week(1, 10), "Wednesday")

    def test_december_12(self):
        """測試 12 月的 Doomsday（12 月 12 日）"""
        # 12 月 12 日是 Doomsday，應該是星期三
        self.assertEqual(get_day_of_week(12, 12), "Wednesday")

    def test_february_21(self):
        """測試 2 月的 Doomsday（2 月 21 日）"""
        # 2 月 21 日是 Doomsday，應該是星期三
        self.assertEqual(get_day_of_week(2, 21), "Wednesday")

    def test_february_29(self):
        """測試 2 月 29 日（2012 年是閏年）"""
        # 2 月 21 日是星期三，所以 2 月 29 日（8 天後）是星期四
        # 21 + 8 = 29，星期三 + 8 天 = 星期四
        self.assertEqual(get_day_of_week(2, 29), "Thursday")

    def test_may_21(self):
        """測試 5 月 21 日（在 Doomsday 之後 12 天）"""
        # 5 月 9 日是星期三，所以 5 月 21 日（12 天後）是星期一
        # 星期三 + 12 天 = 星期三 + 12 % 7 天 = 星期三 + 5 天 = 星期一
        self.assertEqual(get_day_of_week(5, 21), "Monday")


if __name__ == '__main__':
    unittest.main()
