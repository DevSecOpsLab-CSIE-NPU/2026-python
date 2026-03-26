# R07. 日期時間基本運算（3.12–3.13）
#
# 這份範例示範兩件事：
# 1. 使用 timedelta 進行日期與時間的加減
# 2. 利用 weekday() 推算「上一個指定星期幾」的日期

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# timedelta 用來表示「時間差」，可由天、小時、分鐘等單位組成。
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

# days 只會顯示整天部分。
print(c.days)  # 2

# 若要看完整時間差，通常用 total_seconds() 再自行換算。
print(c.total_seconds() / 3600)  # 58.5

dt = datetime(2012, 9, 23)
# datetime 加上 timedelta，就能得到新的日期時間。
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
# 兩個 datetime 相減會得到 timedelta。
print((d2 - d1).days)  # 89

# Python 內建日期運算會自動處理閏年，不需要自己判斷二月有幾天。
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
# weekday() 的編號規則是：Monday=0, ..., Sunday=6。
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
    """回傳 start 之前最近一次指定星期幾的日期。

    如果 start 本身剛好就是目標星期，也會往前退 7 天，
    也就是找「上一個」而不是「當天」。
    """
    if start is None:
        start = datetime.today()

    # 目前日期是星期幾（0~6）。
    day_num = start.weekday()

    # 目標星期名稱對應到清單中的索引值。
    target = WEEKDAYS.index(dayname)

    # 透過模數運算算出要往前退幾天。
    # 若結果為 0，表示今天就是目標星期，但此函式要找「上一個」；
    # 因此用 or 7 強制退回 7 天。
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24
