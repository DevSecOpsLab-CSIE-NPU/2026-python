# R08. 日期範圍與字串轉換（3.14–3.15）
#
# 這份範例聚焦在兩種常見需求：
# 1. 取得某個月份的日期範圍，並迭代區間內的日期時間
# 2. 日期字串與 datetime 之間的轉換

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    """回傳某月份的起始日與「下一個月的第一天」。

    第二個回傳值不是該月最後一天，而是區間終點，
    這種設計適合搭配 while start < stop 的寫法。
    """
    if start is None:
        start = date.today().replace(day=1)

    # monthrange(year, month) 會回傳：
    # 1. 當月第一天是星期幾
    # 2. 該月總天數
    _, days = monthrange(start.year, start.month)
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
# last 是下個月第一天，因此顯示本月最後一天時要再減 1 天。
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器。
# 這裡採用「左閉右開」區間：包含 start，但不包含 stop。
def date_range(start: datetime, stop: datetime, step: timedelta):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"

# strptime() 依指定格式把字串解析成 datetime。
# %Y=%4位年份，%m=2位月份，%d=2位日期。
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00

# strftime() 則是反方向，把 datetime 格式化成字串。
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 如果輸入格式非常固定，手動 split 再轉型也是可行做法。
# 這種方式通常比 strptime() 更輕量，但可讀性與彈性較低。
def parse_ymd(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
