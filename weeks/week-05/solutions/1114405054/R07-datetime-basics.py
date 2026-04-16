# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期

# datetime 表示日期時間，timedelta 表示兩個時間點之間的時間差
from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# 建立 2 天 6 小時的時間差
a = timedelta(days=2, hours=6)
# 也可以使用小數小時建立時間差
b = timedelta(hours=4.5)
# timedelta 之間可直接相加
c = a + b
# days 只會回傳整天的部分
print(c.days)  # 2
# total_seconds() 會回傳完整秒數，適合再換算成小時或分鐘
print(c.total_seconds() / 3600)  # 58.5

# datetime 可直接加上 timedelta，得到新的日期時間
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

# 兩個 datetime 相減後會得到 timedelta
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年自動處理
# 2012 是閏年，所以 2 月有 29 天
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
# 2013 不是閏年，所以只差 1 天
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
# Python 的 weekday() 以星期一為 0、星期日為 6
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
    # 若未提供起始日期，預設使用今天
    if start is None:
        start = datetime.today()
    # 取得起始日期是星期幾
    day_num = start.weekday()
    # 找出目標星期在 WEEKDAYS 清單中的索引位置
    target = WEEKDAYS.index(dayname)
    # 計算距離上一個指定星期需要往前退幾天
    days_ago = (7 + day_num - target) % 7 or 7
    # 回傳往前推算後的日期
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
# 由 2012-08-28 往前找到最近的星期一
print(get_previous_byday("Monday", base))  # 2012-08-27
# 由 2012-08-28 往前找到最近的星期五
print(get_previous_byday("Friday", base))  # 2012-08-24
