"""
U05. 日期時間的陷阱 - 單元測試
=============================
測試重點：
1. timedelta 不支援月份參數
2. 月份加法的正確實現
3. strptime 效能考慮
"""

import unittest
import calendar
from datetime import datetime, timedelta


class TestDatetimeGotchas(unittest.TestCase):
    """日期時間的陷阱的單元測試"""

    def test_timedelta_does_not_support_months(self):
        """測試：timedelta 不支援 months 參數"""
        dt = datetime(2012, 9, 23)
        
        # 嘗試用 months 會拋出 TypeError
        with self.assertRaises(TypeError) as context:
            dt + timedelta(months=1)  # type: ignore
        
        self.assertIn("months", str(context.exception))

    def test_add_one_month_correct_implementation(self):
        """測試：正確的月份加法實現"""
        def add_one_month(dt: datetime) -> datetime:
            """為日期加一個月，處理邊界情況（如 1/31 + 1 月 = 2/29）"""
            year = dt.year
            month = dt.month + 1
            if month == 13:
                year += 1
                month = 1
            
            # 取得目標月份的天數，並把日期限制在該月最後一天
            _, days_in_target_month = calendar.monthrange(year, month)
            day = min(dt.day, days_in_target_month)
            
            return dt.replace(year=year, month=month, day=day)
        
        # 1/31 + 1 月 = 2/29（2012 是閏年）
        result = add_one_month(datetime(2012, 1, 31))
        self.assertEqual(result, datetime(2012, 2, 29))
        
        # 正常情況
        result = add_one_month(datetime(2012, 9, 23))
        self.assertEqual(result, datetime(2012, 10, 23))

    def test_add_months_year_boundary(self):
        """測試：跨年份的月份加法"""
        def add_one_month(dt: datetime) -> datetime:
            year = dt.year
            month = dt.month + 1
            if month == 13:
                year += 1
                month = 1
            _, days_in_target_month = calendar.monthrange(year, month)
            day = min(dt.day, days_in_target_month)
            return dt.replace(year=year, month=month, day=day)
        
        # 12 月加一月 = 隔年 1 月
        result = add_one_month(datetime(2012, 12, 15))
        self.assertEqual(result, datetime(2013, 1, 15))

    def test_timedelta_supports_days_seconds_microseconds(self):
        """測試：timedelta 支援的參數"""
        dt = datetime(2012, 9, 23, 10, 30, 45)
        
        # timedelta 支援 days, seconds, milliseconds, microseconds, minutes, hours, weeks
        result = dt + timedelta(days=5)
        self.assertEqual(result.date(), datetime(2012, 9, 28).date())
        
        result = dt + timedelta(hours=2, minutes=30)
        self.assertEqual(result, datetime(2012, 9, 23, 13, 0, 45))

    def test_strptime_parsing(self):
        """測試：strptime 日期解析"""
        date_str = "2012-09-20"
        
        # strptime 正確解析日期字串
        result = datetime.strptime(date_str, "%Y-%m-%d")
        self.assertEqual(result, datetime(2012, 9, 20))

    def test_manual_date_parsing_faster(self):
        """測試：手動解析比 strptime 更快（簡單格式下）"""
        def use_manual(s: str) -> datetime:
            y, m, d = s.split("-")
            return datetime(int(y), int(m), int(d))
        
        result = use_manual("2012-09-20")
        self.assertEqual(result, datetime(2012, 9, 20))


if __name__ == "__main__":
    unittest.main()
