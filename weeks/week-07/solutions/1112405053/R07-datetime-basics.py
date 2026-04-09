# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
a = timedelta(days=2, hours=6)  # 建立時間差物件：2天6小時
b = timedelta(hours=4.5)  # 建立時間差物件：4.5小時
c = a + b  # 時間差相加
print(c.days)  # 輸出天數: 2
print(c.total_seconds() / 3600)  # 輸出總秒數轉換為小時: 58.5

dt = datetime(2012, 9, 23)  # 建立日期時間物件
print(dt + timedelta(days=10))  # 日期加10天：2012-10-03 00:00:00

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)  # 建立兩個日期物件
print((d2 - d1).days)  # 計算日期差距的天數: 89

# 閏年自動處理
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2012年是閏年，差距為2天
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 2013年是平年，差距為1天

# ── 3.13 計算指定星期日期 ─────────────────────────────
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]  # 星期幾的英文名稱列表


def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    """根據星期名稱，找出該星期距今最近的過去日期"""
    if start is None:
        start = datetime.today()  # 若未指定起始日期，預設為今天
    day_num = start.weekday()  # 取得起始日期是星期幾 (0=週一, 6=週日)
    target = WEEKDAYS.index(dayname)  # 取得目標星期在列表中的索引
    days_ago = (7 + day_num - target) % 7 or 7  # 計算要往前退幾天 (若為0則改為7)
    return start - timedelta(days=days_ago)  # 回傳計算結果


base = datetime(2012, 8, 28)  # 週二
print(get_previous_byday("Monday", base))  # 往前找週一：2012-08-27
print(get_previous_byday("Friday", base))  # 往前找週五：2012-08-24
