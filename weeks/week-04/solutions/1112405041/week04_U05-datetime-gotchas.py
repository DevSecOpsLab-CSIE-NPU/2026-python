# 【Bloom 階段：U - 理解與進階應用】
# U05. 日期運算的邊界陷阱 (Date Edge Cases)
# August 的惡意提醒：timedelta 不支持「月」或「年」。
# 如果你在 1 月 31 日加一個月，預期是 2 月 28/29 日，手寫 if 很容易漏掉細節。

import calendar
from datetime import datetime

def add_one_month(dt):
    """精確增加一個月的資工系寫法"""
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1

    # 關鍵：利用 monthrange 處理不同月份的天數差異
    _, days_in_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_month) # 若原日為 31，目標月只有 28，則取 28

    return dt.replace(year=year, month=month, day=day)

# 測試邊界情況
start = datetime(2012, 1, 31)
print(f"Jan 31 + 1 Month: {add_one_month(start)}") # 2012-02-29
