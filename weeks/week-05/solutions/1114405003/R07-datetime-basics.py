# -*- coding: utf-8 -*-
"""
R07. 日期時間基本運算 - 單元測試程式

【學習目標】
本程式針對 Python 日期時間運算進行單元測試，包括：
1. timedelta 時間差運算
2. 日期加減計算
3. 計算指定星期幾的日期

【重要概念】
- timedelta 表示時間差
- datetime 可以進行日期加減
- 自動處理閏年
- weekday() 回傳星期幾（0=星期一，6=星期日）
"""

import unittest
from datetime import datetime, timedelta


class TestTimedeltaOperations(unittest.TestCase):
    """測試 timedelta 時間差運算"""

    def test_timedelta_basic(self):
        """
        【測試1】建立 timedelta

        timedelta(days=天, hours=小時, minutes=分, seconds=秒)
        """
        a = timedelta(days=2, hours=6)
        self.assertEqual(a.days, 2)
        self.assertEqual(a.seconds, 6 * 3600)  # 6 小時 = 21600 秒

    def test_timedelta_add(self):
        """
        【測試2】timedelta 相加

        timedelta 可以相加，結果仍是 timedelta
        """
        a = timedelta(days=2, hours=6)
        b = timedelta(hours=4.5)
        c = a + b

        # 2 天 6 小時 + 4.5 小時 = 2 天 10.5 小時
        self.assertEqual(c.days, 2)
        self.assertAlmostEqual(c.total_seconds() / 3600, 58.5)

    def test_timedelta_total_seconds(self):
        """
        【測試3】total_seconds() 取得總秒數
        """
        t = timedelta(days=1, hours=2)
        self.assertEqual(t.total_seconds(), 26 * 3600)  # 1天2小時 = 26 小時


class TestDatetimeArithmetic(unittest.TestCase):
    """測試 datetime 日期運算"""

    def test_datetime_add_days(self):
        """
        【測試4】日期加天數

        datetime + timedelta = 新的 datetime
        """
        dt = datetime(2012, 9, 23)
        result = dt + timedelta(days=10)
        self.assertEqual(result, datetime(2012, 10, 3))

    def test_datetime_subtract_days(self):
        """
        【測試5】日期減天數
        """
        dt = datetime(2012, 9, 23)
        result = dt - timedelta(days=10)
        self.assertEqual(result, datetime(2012, 9, 13))

    def test_date_difference(self):
        """
        【測試6】兩個日期相減

        datetime1 - datetime2 = timedelta

        範例：
        2012-12-21 - 2012-09-23 = 89 天
        """
        d1 = datetime(2012, 9, 23)
        d2 = datetime(2012, 12, 21)
        diff = d2 - d1
        self.assertEqual(diff.days, 89)

    def test_leap_year_handling(self):
        """
        【測試7】自動處理閏年

        Python 自動處理閏年！
        - 2012 是閏年（2月有29天）
        - 2013 是平年（2月有28天）

        從 2/28 到 3/1：
        - 閏年：2天（2/28 → 2/29 → 3/1）
        - 平年：1天（2/28 → 3/1）
        """
        # 閏年
        leap = datetime(2012, 3, 1) - datetime(2012, 2, 28)
        self.assertEqual(leap.days, 2)

        # 平年
        normal = datetime(2013, 3, 1) - datetime(2013, 2, 28)
        self.assertEqual(normal.days, 1)


class TestWeekdayCalculation(unittest.TestCase):
    """測試星期計算"""

    def test_weekday_method(self):
        """
        【測試8】weekday() 方法

        weekday() 回傳星期幾：
        - 0 = Monday（星期一）
        - 1 = Tuesday（星期二）
        - 2 = Wednesday（星期三）
        - 3 = Thursday（星期四）
        - 4 = Friday（星期五）
        - 5 = Saturday（星期六）
        - 6 = Sunday（星期日）
        """
        # 2012-08-28 是星期二
        dt = datetime(2012, 8, 28)
        self.assertEqual(dt.weekday(), 1)  # 1 = Tuesday

    def test_get_previous_byday(self):
        """
        【測試9】取得最近的指定星期幾

        找到 start 日期之前，最近的指定星期幾

        範例：
        base = 2012-08-28（週二）
        get_previous_byday("Monday", base) → 2012-08-27（週一）
        get_previous_byday("Friday", base) → 2012-08-24（週五）
        """
        WEEKDAYS = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
            if start is None:
                start = datetime.today()
            day_num = start.weekday()
            target = WEEKDAYS.index(dayname)
            days_ago = (7 + day_num - target) % 7 or 7
            return start - timedelta(days=days_ago)

        base = datetime(2012, 8, 28)  # 週二
        # 找週一：週二的前一天
        result = get_previous_byday("Monday", base)
        self.assertEqual(result, datetime(2012, 8, 27))

        # 找週五：週二的前4天
        result = get_previous_byday("Friday", base)
        self.assertEqual(result, datetime(2012, 8, 24))

    def test_isoweekday(self):
        """
        【測試10】isoweekday() 方法

        isoweekday() 與 weekday() 類似，但：
        - 1 = Monday（星期一）
        - 7 = Sunday（星期日）
        """
        dt = datetime(2012, 8, 28)  # 週二
        self.assertEqual(dt.isoweekday(), 2)


class TestDatetimeAttributes(unittest.TestCase):
    """測試 datetime 屬性"""

    def test_datetime_attributes(self):
        """
        【測試11】datetime 各屬性

        datetime 物件的年、月、日、時、分、秒
        """
        dt = datetime(2012, 9, 23, 10, 30, 45)
        self.assertEqual(dt.year, 2012)
        self.assertEqual(dt.month, 9)
        self.assertEqual(dt.day, 23)
        self.assertEqual(dt.hour, 10)
        self.assertEqual(dt.minute, 30)
        self.assertEqual(dt.second, 45)

    def test_datetime_replace(self):
        """
        【測試12】replace() 修改部分屬性

        replace(year=年, month=月, day=日, ...)

        建立新物件，修改指定的屬性
        """
        dt = datetime(2012, 9, 23)
        result = dt.replace(year=2020, month=1)
        self.assertEqual(result, datetime(2020, 1, 23))


if __name__ == "__main__":
    unittest.main(verbosity=2)
