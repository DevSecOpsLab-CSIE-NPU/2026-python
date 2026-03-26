# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# 建立時間差：2 天 6 小時
a = timedelta(days=2, hours=6)
# 也可用小數小時（4.5 小時 = 4 小時 30 分）
b = timedelta(hours=4.5)
# timedelta 可直接相加
c = a + b
# .days 只回傳「整天數」部分
print(c.days)  # 2
# 若要完整時數，建議用 total_seconds() 再換算
print(c.total_seconds() / 3600)  # 58.5

# datetime 可和 timedelta 相加，得到新日期時間
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

# 兩個 datetime 相減會得到 timedelta
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年自動處理
# 2012 是閏年，2/29 存在，所以差 2 天
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
# 2013 是平年，2 月只有 28 天，所以差 1 天
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
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
    # 未指定起始日就用「現在時間」
    if start is None:
        start = datetime.today()
    # weekday(): Monday=0, ..., Sunday=6
    day_num = start.weekday()
    # 目標星期在 WEEKDAYS 中的索引
    target = WEEKDAYS.index(dayname)
    # 計算往前回推幾天：
    # - (7 + day_num - target) % 7 可得距離（0~6）
    # - 若結果是 0，代表同一天；題意要「前一個」該星期，因此改成 7
    days_ago = (7 + day_num - target) % 7 or 7
    # 回推對應天數，取得前一個指定星期日期
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
# 從週二往前找最近一個週一
print(get_previous_byday("Monday", base))  # 2012-08-27
# 從週二往前找最近一個週五
print(get_previous_byday("Friday", base))  # 2012-08-24
