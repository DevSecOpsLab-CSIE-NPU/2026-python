"""
R07: datetime 與 timedelta 基本操作。

示範重點：
1. 用 `timedelta` 表示時間差。
2. 計算兩個日期之間的天數。
3. 依星期幾回推上一個指定日期。
"""

from datetime import datetime, timedelta

# `timedelta` 可組合天、小時、分鐘等時間單位。
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)  # 2
print(c.total_seconds() / 3600)  # 58.5

dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年的 2 月有 29 天，因此日期差會和一般年份不同。
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(day_name: str, start: datetime | None = None) -> datetime:
    """
    找出 `start` 之前最近的一個指定星期。

    若今天剛好就是目標星期，函式會回傳往前推 7 天的那一天，
    因為題目要找的是「上一個」而不是「今天」。
    """

    if start is None:
        start = datetime.today()

    current_day_num = start.weekday()
    target_day_num = WEEKDAYS.index(day_name)

    # `% 7` 用來把差值限制在一週內。
    # 若結果是 0，代表今天就是目標星期，因此改成回推 7 天。
    days_ago = (7 + current_day_num - target_day_num) % 7 or 7
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 星期二
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24
