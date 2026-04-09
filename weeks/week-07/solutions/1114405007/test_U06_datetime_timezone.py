"""
U06. 時區操作最佳實踐 - 單元測試
===============================
測試重點：
1. UTC 優先 - 內部計算用 UTC
2. 夏令時邊界問題
3. 本地時間 ↔ UTC 轉換
"""

import unittest
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


class TestDatetimeTimezone(unittest.TestCase):
    """時區操作最佳實踐的單元測試"""

    def test_naive_datetime_addition_dst_problem(self):
        """測試：直接在本地時間加減日期在夏令時邊界會出錯"""
        # 美國中部時間，2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
        central = ZoneInfo("America/Chicago")
        local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
        
        # 直接加會得到不存在的時間
        wrong = local_dt + timedelta(minutes=30)
        
        # 結果是 2:15 AM，但這個時間不存在（被跳過）
        # 實際上會是 3:15 AM（因為 2:00-3:00 被跳過）
        # 此測試顯示問題存在
        self.assertEqual(wrong.hour, 2)
        self.assertEqual(wrong.minute, 15)

    def test_correct_timezone_addition_via_utc(self):
        """測試：正確做法 - 先轉 UTC 再計算"""
        utc = ZoneInfo("UTC")
        central = ZoneInfo("America/Chicago")
        
        # 美國中部時間 2013-03-10 1:45 AM
        local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
        
        # 步驟1: 轉成 UTC
        utc_dt = local_dt.astimezone(utc)
        
        # 步驟2: 在 UTC 中加時間
        correct_utc = utc_dt + timedelta(minutes=30)
        
        # 步驟3: 轉回本地時間
        correct_local = correct_utc.astimezone(central)
        
        # 結果應該是 3:15 AM（跳過了 2:xx 的一小時）
        self.assertEqual(correct_local.hour, 3)
        self.assertEqual(correct_local.minute, 15)

    def test_user_input_to_utc_storage(self):
        """測試：最佳實踐 - 輸入→UTC→計算→輸出時轉本地"""
        # 用户输入的本地时间字符串（不含时区信息）
        user_input = "2012-12-21 09:30:00"
        
        # 步驟1: 解析為 naive datetime
        naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
        
        # 步驟2: 加上時區信息（假設用户在台北）
        central = ZoneInfo("America/Chicago")
        aware = naive.replace(tzinfo=ZoneInfo("Asia/Taipei")).astimezone(ZoneInfo("UTC"))
        
        # 步驟3: 存儲為 UTC
        self.assertEqual(aware.tzinfo, ZoneInfo("UTC"))

    def test_timezone_aware_comparison(self):
        """測試：具有時區的日期時間比較"""
        utc = ZoneInfo("UTC")
        ny = ZoneInfo("America/New_York")
        tokyo = ZoneInfo("Asia/Tokyo")
        
        # 同一時刻，不同時區表示
        utc_time = datetime(2023, 1, 1, 12, 0, 0, tzinfo=utc)
        ny_time = utc_time.astimezone(ny)
        tokyo_time = utc_time.astimezone(tokyo)
        
        # 都表示同一時刻，所以相等
        self.assertEqual(utc_time, ny_time)
        self.assertEqual(utc_time, tokyo_time)
        
        # 本地時間不同，但代表同一時刻
        self.assertNotEqual(utc_time.hour, ny_time.hour)
        self.assertNotEqual(utc_time.hour, tokyo_time.hour)

    def test_naive_vs_aware_datetime(self):
        """測試：naive datetime vs aware datetime"""
        # naive datetime（不含時區信息）
        naive = datetime(2012, 12, 21, 9, 30, 0)
        self.assertIsNone(naive.tzinfo)
        
        # aware datetime（含時區信息）
        aware = datetime(2012, 12, 21, 9, 30, 0, tzinfo=ZoneInfo("UTC"))
        self.assertIsNotNone(aware.tzinfo)


if __name__ == "__main__":
    unittest.main()
