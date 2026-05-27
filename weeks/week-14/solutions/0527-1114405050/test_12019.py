import unittest
import datetime

# ==========================================
# 核心解題邏輯 (可移至獨立檔案例如 solution_12019.py)
# ==========================================
def get_weekday_2012(month: int, day: int) -> str:
    """
    計算 2012 年特定日期是星期幾。
    2012 年是閏年。
    使用 Python datetime 模組是最穩健的做法。
    """
    # weekday() 回傳 0-6，分別代表 Monday-Sunday
    weekdays = [
        "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"
    ]
    
    # 建立 2012 年的日期物件
    date_obj = datetime.date(2012, month, day)
    return weekdays[date_obj.weekday()]

# ==========================================
# 單元測試區塊
# ==========================================
class TestDoomsDay(unittest.TestCase):
    
    def test_doomsday_dates(self):
        """測試 2012 年的固定對稱日期（4/4, 6/6 等皆應為 Wednesday）"""
        # 2012 年是閏年，這些日期在該年確實都是星期三
        doomsdays = [
            (3, 7), (4, 4), (5, 9), (6, 6),
            (7, 11), (8, 8), (9, 5), (10, 10), (11, 7), (12, 12)
        ]
        # 注意：1/10 與 2/21 在閏年 2012 分別是 Tuesday 與 Tuesday
        for m, d in doomsdays:
            with self.subTest(month=m, day=d):
                self.assertEqual(get_weekday_2012(m, d), "Wednesday")

    def test_specific_dates(self):
        """測試特定的已知日期"""
        # 2012/1/1 是星期日
        self.assertEqual(get_weekday_2012(1, 1), "Sunday")
        # 2012/12/31 是星期一
        self.assertEqual(get_weekday_2012(12, 31), "Monday")
        # 2012/2/29 (閏日) 是星期三
        self.assertEqual(get_weekday_2012(2, 29), "Wednesday")

    def test_invalid_date(self):
        """測試無效日期是否會拋出異常 (輔助檢查)"""
        with self.assertRaises(ValueError):
            # 2012 年 2 月只有 29 天，測試 30 號
            get_weekday_2012(2, 30)

if __name__ == '__main__':
    # 執行單元測試
    unittest.main()