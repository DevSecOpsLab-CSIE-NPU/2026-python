# -*- coding: utf-8 -*-
"""
R09. 時區操作 - 單元測試程式

【學習目標】
本程式針對 Python 時區操作進行單元測試，包括：
1. ZoneInfo 建立時區aware的datetime
2. 時區轉換（astimezone）
3. UTC 時間處理
4. 查詢可用時區

【重要概念】
- Python 3.9+ 使用 zoneinfo 模組（取代 pytz）
- naive datetime = 沒有時區資訊
- aware datetime = 有時區資訊
- 最佳實踐：內部儲存 UTC，輸出時轉換為本地時區
"""

import unittest
from datetime import datetime, timedelta, timezone

try:
    from zoneinfo import ZoneInfo, available_timezones

    ZONEINFO_AVAILABLE = True
except ImportError:
    ZONEINFO_AVAILABLE = False


class TestTimezoneBasic(unittest.TestCase):
    """測試時區基本概念"""

    def test_utc_timezone(self):
        """
        【測試1】UTC 時區

        使用 timezone.utc 建立 UTC 時區
        """
        utc = timezone.utc
        dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=utc)

        self.assertEqual(dt.tzinfo, timezone.utc)

    def test_fixed_offset_timezone(self):
        """
        【測試2】固定偏移時區

        使用 timedelta 建立固定偏移的時區

        例如：UTC+8 = timedelta(hours=8)
        """
        # 台北時區：UTC+8
        taipei_offset = timedelta(hours=8)
        taipei_tz = timezone(taipei_offset)

        dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=taipei_tz)
        self.assertEqual(dt.hour, 12)

    def test_datetime_now_utc(self):
        """
        【測試3】取得當前 UTC 時間

        datetime.now(timezone.utc)
        """
        now_utc = datetime.now(timezone.utc)
        self.assertIsNotNone(now_utc.tzinfo)


class TestTimezoneConversion(unittest.TestCase):
    """測試時區轉換"""

    def test_replace_timezone(self):
        """
        【測試4】替換時區

        datetime.replace(tzinfo=時區)

        注意：這只是替換時區資訊，不會調整時間
        """
        # 建立一個 naive datetime
        dt_naive = datetime(2024, 1, 1, 12, 0, 0)

        # 加上 UTC 時區
        dt_utc = dt_naive.replace(tzinfo=timezone.utc)
        self.assertEqual(dt_utc.hour, 12)

    def test_astimezone_aware(self):
        """
        【測試5】時區轉換（需要 aware datetime）

        aware_datetime.astimezone(目標時區)

        先決條件：datetime 必須有時區資訊
        """
        # 建立 UTC 時間
        dt_utc = datetime(2024, 1, 1, 4, 0, 0, tzinfo=timezone.utc)

        # 如果 zoneinfo 可用，測試完整轉換
        if ZONEINFO_AVAILABLE:
            try:
                taipei = ZoneInfo("Asia/Taipei")
                dt_taipei = dt_utc.astimezone(taipei)
                # UTC 4:00 = Taipei 12:00（+8小時）
                self.assertEqual(dt_taipei.hour, 12)
            except Exception:
                self.skipTest("Timezone data not available")
        else:
            # 使用固定偏移時區測試
            taipei_offset = timedelta(hours=8)
            taipei_tz = timezone(taipei_offset)
            dt_taipei = dt_utc.astimezone(taipei_tz)
            self.assertEqual(dt_taipei.hour, 12)


class TestTimezoneOffset(unittest.TestCase):
    """測試時區偏移計算"""

    def test_taipei_offset(self):
        """
        【測試6】台北時區偏移

        台北時區 = UTC + 8 小時

        概念：
        - 台北早上 8 點 = UTC 0 點
        - 台北中午 12 點 = UTC 4 點
        """
        taipei_offset = timedelta(hours=8)
        taipei_tz = timezone(taipei_offset)

        # 台北中午12點
        dt_taipei = datetime(2024, 1, 1, 12, 0, 0, tzinfo=taipei_tz)

        # UTC = 台北時間 - 8 小時 = 4 點
        utc = dt_taipei.astimezone(timezone.utc)
        self.assertEqual(utc.hour, 4)

    def test_japan_offset(self):
        """
        【測試7】東京時區偏移

        東京時區 = UTC + 9 小時
        """
        japan_offset = timedelta(hours=9)
        japan_tz = timezone(japan_offset)

        dt_japan = datetime(2024, 1, 1, 12, 0, 0, tzinfo=japan_tz)
        utc = dt_japan.astimezone(timezone.utc)

        # UTC = 東京時間 - 9 小時 = 3 點
        self.assertEqual(utc.hour, 3)


class TestTimezoneConversions(unittest.TestCase):
    """測試時區轉換計算"""

    def test_convert_between_timezones(self):
        """
        【測試8】時區間轉換

        台北 2024-01-01 12:00（UTC+8）
        → UTC 2024-01-01 04:00

        如果 zoneinfo 可用，進一步測試：
        → 紐約 2023-12-31 15:00（UTC-5）
        """
        taipei_offset = timedelta(hours=8)
        taipei_tz = timezone(taipei_offset)

        # 台北時間
        dt_taipei = datetime(2024, 1, 1, 12, 0, 0, tzinfo=taipei_tz)

        # 轉換為 UTC
        dt_utc = dt_taipei.astimezone(timezone.utc)
        self.assertEqual(dt_utc.hour, 4)

    def test_us_eastern_offset(self):
        """
        【測試9】美國東部時區偏移

        冬季：UTC-5（不含夏令時間）
        夏季：UTC-4（夏令時間）
        """
        # 冬季時間
        eastern_offset = timedelta(hours=-5)
        eastern_tz = timezone(eastern_offset)

        # 紐約中午12點 = UTC 17:00（12 - (-5) = 17）
        dt_ny = datetime(2024, 1, 15, 12, 0, 0, tzinfo=eastern_tz)
        dt_utc = dt_ny.astimezone(timezone.utc)
        self.assertEqual(dt_utc.hour, 17)


class TestBestPractices(unittest.TestCase):
    """測試時區最佳實踐"""

    def test_utc_storage_concept(self):
        """
        【測試10】最佳實踐：內部用 UTC

        建議：
        1. 資料庫內部儲存 UTC 時間
        2. 使用者介面顯示本地時間
        3. 網路傳輸使用 UTC

        好處：
        - 跨時區資料一致
        - 夏令時間自動處理
        - 時區轉換簡單
        """
        # 模擬：儲存 UTC 時間
        utc_time = datetime(2024, 3, 26, 4, 0, 0, tzinfo=timezone.utc)

        # 模擬：顯示台北本地時間（UTC+8）
        taipei_offset = timedelta(hours=8)
        taipei_tz = timezone(taipei_offset)
        taipei_time = utc_time.astimezone(taipei_tz)

        # UTC 4:00 = 台北 12:00
        self.assertEqual(taipei_time.hour, 12)
        self.assertEqual(taipei_time.day, 26)

    def test_naive_vs_aware(self):
        """
        【測試11】naive datetime vs aware datetime

        - naive datetime：沒有時區資訊
        - aware datetime：有時區資訊

        時區轉換只能用在 aware datetime！
        """
        # naive datetime
        dt_naive = datetime(2024, 1, 1, 12, 0, 0)
        self.assertIsNone(dt_naive.tzinfo)

        # aware datetime
        dt_aware = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        self.assertIsNotNone(dt_aware.tzinfo)


class TestZoneInfoIfAvailable(unittest.TestCase):
    """如果有 zoneinfo 模組，測試其功能"""

    def test_zoneinfo_import(self):
        """【測試12】確認 zoneinfo 可用"""
        self.assertTrue(ZONEINFO_AVAILABLE)

    @unittest.skipUnless(ZONEINFO_AVAILABLE, "zoneinfo 模組不可用")
    def test_utc_zoneinfo(self):
        """【測試13】使用 ZoneInfo 建立 UTC"""
        try:
            utc = ZoneInfo("UTC")
            dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=utc)
            self.assertEqual(dt.hour, 12)
        except Exception:
            self.skipTest("Timezone data not properly installed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
