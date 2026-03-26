# -*- coding: utf-8 -*-
"""
R08. 日期範圍與字串轉換 - 單元測試程式

【學習目標】
本程式針對 Python 日期範圍與字串轉換進行單元測試，包括：
1. 當月日期範圍計算
2. 日期迭代器
3. 字串轉日期（strptime）
4. 日期轉字串（strftime）

【重要概念】
- calendar.monthrange() 取得當月天數
- strptime(str, format) 將字串轉換為 datetime
- strftime(format) 將 datetime 轉換為字串
- %Y = 年（4位）, %m = 月, %d = 日, %H = 時, %M = 分, %S = 秒
"""

import unittest
from datetime import datetime, date, timedelta
from calendar import monthrange


class TestMonthRange(unittest.TestCase):
    """測試當月日期範圍"""

    def test_monthrange(self):
        """
        【測試1】monthrange() 取得當月資訊

        monthrange(年, 月) 回傳 (星期幾開始, 天數)

        星期幾：0=週一, 1=週二, ..., 6=週日

        範例：
        monthrange(2012, 8) → (2, 31)
        - 2012年8月從星期三開始（2=週三）
        - 共有31天
        """
        # 2012年8月：從週三開始，31天
        result = monthrange(2012, 8)
        self.assertEqual(result[0], 2)  # 週三
        self.assertEqual(result[1], 31)  # 31天

    def test_get_month_range(self):
        """
        【測試2】取得月份開始和結束日期
        """

        def get_month_range(start: date | None = None) -> tuple[date, date]:
            if start is None:
                start = date.today().replace(day=1)
            _, days = monthrange(start.year, start.month)
            return start, start + timedelta(days=days)

        first, last = get_month_range(date(2012, 8, 1))
        self.assertEqual(first, date(2012, 8, 1))
        self.assertEqual(last, date(2012, 9, 1))

        # 月份最後一天 = 下一月第一天 - 1天
        last_day = last - timedelta(days=1)
        self.assertEqual(last_day.day, 31)

    def test_days_in_month(self):
        """
        【測試3】各月份天數

        大月（31天）：1,3,5,7,8,10,12
        小月（30天）：4,6,9,11
        閏年2月：29天
        平年2月：28天
        """
        # 8月有31天
        self.assertEqual(monthrange(2024, 8)[1], 31)
        # 9月有30天
        self.assertEqual(monthrange(2024, 9)[1], 30)
        # 閏年2月有29天
        self.assertEqual(monthrange(2024, 2)[1], 29)
        # 平年2月有28天
        self.assertEqual(monthrange(2023, 2)[1], 28)


class TestDateRangeIterator(unittest.TestCase):
    """測試日期範圍迭代"""

    def test_date_range_generator(self):
        """
        【測試4】日期範圍生成器

        產生從 start 到 stop（不包含）的日期序列
        """

        def date_range(start: datetime, stop: datetime, step: timedelta):
            result = []
            while start < stop:
                result.append(start)
                start += step
            return result

        # 從 9月1日 00:00 到 9月2日 00:00，每6小時
        result = date_range(
            datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)
        )

        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], datetime(2012, 9, 1))
        self.assertEqual(result[1], datetime(2012, 9, 1, 6))
        self.assertEqual(result[2], datetime(2012, 9, 1, 12))
        self.assertEqual(result[3], datetime(2012, 9, 1, 18))

    def test_day_range(self):
        """
        【測試5】日期範圍（每天）
        """

        def date_range(start: datetime, stop: datetime, step: timedelta):
            result = []
            while start < stop:
                result.append(start)
                start += step
            return result

        result = date_range(
            datetime(2024, 1, 1), datetime(2024, 1, 5), timedelta(days=1)
        )

        self.assertEqual(len(result), 4)


class TestStrptimeParsing(unittest.TestCase):
    """測試字串解析為日期"""

    def test_strptime_basic(self):
        """
        【測試6】strptime() 基本用法

        datetime.strptime(字串, 格式)

        將字串按照指定格式轉換為 datetime

        常見格式碼：
        - %Y = 4位年份（2012）
        - %y = 2位年份（12）
        - %m = 2位月份（01-12）
        - %d = 2位日期（01-31）
        - %H = 24小時（00-23）
        - %M = 分鐘（00-59）
        - %S = 秒數（00-59）
        """
        text = "2012-09-20"
        dt = datetime.strptime(text, "%Y-%m-%d")

        self.assertEqual(dt.year, 2012)
        self.assertEqual(dt.month, 9)
        self.assertEqual(dt.day, 20)

    def test_strptime_various_formats(self):
        """
        【測試7】各種日期格式解析
        """
        # 格式 1：2012/09/20
        dt1 = datetime.strptime("2012/09/20", "%Y/%m/%d")
        self.assertEqual(dt1.day, 20)

        # 格式 2：20/09/2012
        dt2 = datetime.strptime("20/09/2012", "%d/%m/%Y")
        self.assertEqual(dt2.day, 20)

        # 格式 3：2012-09-20 14:30:00
        dt3 = datetime.strptime("2012-09-20 14:30:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(dt3.hour, 14)
        self.assertEqual(dt3.minute, 30)


class TestStrftimeFormatting(unittest.TestCase):
    """測試日期格式化為字串"""

    def test_strftime_basic(self):
        """
        【測試8】strftime() 基本用法

        datetime.strftime(格式)

        將 datetime 按照指定格式轉換為字串

        常用格式碼：
        - %Y = 年（4位）
        - %m = 月（2位）
        - %d = 日（2位）
        - %H = 時（24小時）
        - %M = 分
        - %S = 秒
        - %A = 星期幾全名（Monday）
        - %B = 月份全名（September）
        """
        dt = datetime(2012, 9, 20)
        result = dt.strftime("%Y-%m-%d")
        self.assertEqual(result, "2012-09-20")

    def test_strftime_readable_format(self):
        """
        【測試9】可讀性格式

        範例：Thursday September 20, 2012
        """
        dt = datetime(2012, 9, 20)
        result = dt.strftime("%A %B %d, %Y")
        self.assertEqual(result, "Thursday September 20, 2012")

    def test_strftime_various_formats(self):
        """
        【測試10】各種格式化輸出
        """
        dt = datetime(2012, 9, 20, 14, 30, 0)

        # 日期：2012-09-20
        self.assertEqual(dt.strftime("%Y-%m-%d"), "2012-09-20")
        # 時間：14:30
        self.assertEqual(dt.strftime("%H:%M"), "14:30")
        # 完整：2012/09/20 14:30:00
        self.assertEqual(dt.strftime("%Y/%m/%d %H:%M:%S"), "2012/09/20 14:30:00")
        # 短日期：12/09/20
        self.assertEqual(dt.strftime("%y/%m/%d"), "12/09/20")


class TestManualParsing(unittest.TestCase):
    """測試手動解析"""

    def test_parse_ymd(self):
        """
        【測試11】手動解析 YYYY-MM-DD 格式

        比 strptime 快約 7 倍！

        適用於：已知格式，格式固定簡單
        """

        def parse_ymd(s: str) -> datetime:
            y, m, d = s.split("-")
            return datetime(int(y), int(m), int(d))

        result = parse_ymd("2012-09-20")
        self.assertEqual(result, datetime(2012, 9, 20))


if __name__ == "__main__":
    unittest.main(verbosity=2)
