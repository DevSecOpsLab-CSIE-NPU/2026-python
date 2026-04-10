"""
U05. 日期時間的常見陷阱。

重點：
1. `timedelta` 不支援月份，因為每個月的天數不同。
2. 需要加月份時，必須自己處理跨月與月底對齊問題。
3. `datetime.strptime()` 很方便，但大量資料時可能不是最快做法。
"""

import calendar
import timeit
from datetime import datetime, timedelta


# ── 1. timedelta 不支援 months 參數 ────────────────────────
dt = datetime(2012, 9, 23)

try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as error:
    print(f"TypeError: {error}")


def add_one_month(value: datetime) -> datetime:
    """
    自行計算「加一個月」。

    做法：
    1. 先決定目標年與月。
    2. 查目標月份總共有幾天。
    3. 若原本日期超過目標月份天數，就壓到該月最後一天。
    """

    year = value.year
    month = value.month + 1

    if month == 13:
        year += 1
        month = 1

    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(value.day, days_in_target_month)
    return value.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23


# ── 2. strptime 在大量字串時可能較慢 ──────────────────────
dates = [f"2012-{month:02d}-{day:02d}" for month in range(1, 13) for day in range(1, 29)]


def use_strptime(text: str) -> datetime:
    """直接交給 strptime 解析。"""
    return datetime.strptime(text, "%Y-%m-%d")


def use_manual(text: str) -> datetime:
    """手動拆字串，適合已知固定格式的情境。"""
    year, month, day = text.split("-")
    return datetime(int(year), int(month), int(day))


assert use_strptime("2012-09-20") == use_manual("2012-09-20")

strptime_time = timeit.timeit(lambda: [use_strptime(item) for item in dates], number=100)
manual_time = timeit.timeit(lambda: [use_manual(item) for item in dates], number=100)
print(f"strptime: {strptime_time:.3f}s  手動解析: {manual_time:.3f}s（快 {strptime_time / manual_time:.1f} 倍）")
