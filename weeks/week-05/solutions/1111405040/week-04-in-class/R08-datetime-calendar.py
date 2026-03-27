"""
R08: 月份區間與日期格式轉換。

示範重點：
1. 取得某月份的起訖範圍。
2. 用 generator 產生一段日期序列。
3. `strptime()` 與 `strftime()` 的基本用法。
"""

from calendar import monthrange
from datetime import date, datetime, timedelta


def get_month_range(start: date | None = None) -> tuple[date, date]:
    """
    回傳某個月份的起點與下個月份的第一天。

    這種表示方式很常用，因為區間可以寫成：
    `start <= d < stop`
    """

    if start is None:
        start = date.today().replace(day=1)

    _, days_in_month = monthrange(start.year, start.month)
    return start, start + timedelta(days=days_in_month)


first, stop = get_month_range(date(2012, 8, 1))
print(first, "~", stop - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


def date_range(start: datetime, stop: datetime, step: timedelta):
    """
    依固定步長逐步產生時間點。

    這裡使用 generator，避免一次建立整份清單。
    """

    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

text = "2012-09-20"

# `strptime()` 把字串解析成 datetime 物件。
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00

# `strftime()` 則是把 datetime 轉回指定格式字串。
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


def parse_ymd(value: str) -> datetime:
    """
    用手動切分方式解析 YYYY-MM-DD。

    這種做法在格式固定時很直接，也通常比 `strptime()` 更快。
    """

    year, month, day = value.split("-")
    return datetime(int(year), int(month), int(day))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
