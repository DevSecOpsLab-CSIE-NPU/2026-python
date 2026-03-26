# R07. 日期時間基本運算（3.12–3.13）
# 主題：timedelta 加減 / weekday() + 自訂函式計算前一個星期幾

from datetime import datetime, timedelta

# ------------------------------------------------------------
# 3.12 timedelta：時間差與日期加減
# ------------------------------------------------------------
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

# days 只看整天數，剩下的小時在 seconds 內
print(c.days)  # 2

# total_seconds() 可拿到完整秒數，再換算小時
print(c.total_seconds() / 3600)  # 58.5

# datetime + timedelta：往後推日期
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

# 兩個 datetime 相減得到 timedelta
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年差異：2012 是閏年，所以 2/28 到 3/1 差 2 天
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1

# ------------------------------------------------------------
# 3.13 計算「前一個指定星期幾」
# ------------------------------------------------------------
# weekday() 規則：Monday=0, ... Sunday=6
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
    """回傳 start 之前最近一次的 dayname。

    參數：
    - dayname: 目標星期名稱，例如 "Monday"
    - start: 參考日期，若為 None 則使用今天

    計算概念：
    - 先取得今天是星期幾（day_num）
    - 目標星期索引是 target
    - days_ago = (7 + day_num - target) % 7
    - 若剛好同一天，題目要求「前一個」，所以用 or 7 退一整週
    """
    if start is None:
        start = datetime.today()

    day_num = start.weekday()
    target = WEEKDAYS.index(dayname)
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


# 範例：2012-08-28 是星期二
base = datetime(2012, 8, 28)
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24
