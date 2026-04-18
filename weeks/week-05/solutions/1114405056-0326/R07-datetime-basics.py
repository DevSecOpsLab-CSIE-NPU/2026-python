from datetime import datetime, timedelta

# ── timedelta：表示一段時間間隔 ──────────────────────────
# timedelta 可接受 days、seconds、microseconds、hours、minutes、weeks
a = timedelta(days=2, hours=6)   # 2 天 6 小時
b = timedelta(hours=4.5)         # 4.5 小時
c = a + b                        # timedelta 相加

print(c.days)                    # 整數天數部分
print(c.total_seconds() / 3600)  # 換算為總小時數

# ── datetime 加減 timedelta ───────────────────────────────
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))   # 往後推 10 天

# 兩個 datetime 相減 → 得到 timedelta
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)            # 相差天數

# 驗證閏年：2012 是閏年（2/28 → 3/1 差 2 天），2013 不是（差 1 天）
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1

# ── 計算「上一個星期幾」的日期 ────────────────────────────
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
    """回傳 start 之前（不含當天）最近一次指定星期幾的日期。"""
    if start is None:
        start = datetime.today()
    day_num = start.weekday()          # 0=Monday … 6=Sunday
    target = WEEKDAYS.index(dayname)   # 目標星期的數字
    # (7 + 目前 - 目標) % 7 得出距離天數；若結果為 0 表示今天就是該天，往前推 7 天
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


# 2012-08-28 是星期二，上一個 Monday 是 08-27，上一個 Friday 是 08-24
base = datetime(2012, 8, 28)
print(get_previous_byday("Monday", base))   # 2012-08-27
print(get_previous_byday("Friday", base))   # 2012-08-24
