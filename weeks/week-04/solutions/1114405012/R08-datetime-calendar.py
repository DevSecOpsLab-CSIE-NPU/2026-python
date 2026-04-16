"""R08 日期範圍與字串轉換（3.14–3.15）。"""

# 本檔示範當月日期範圍、日期迭代器、以及字串和日期的互轉

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
# monthrange(year, month) 會回傳星期起始值與當月天數
def get_month_range(start: date | None = None) -> tuple[date, date]:
    # 沒指定 start 時，就以今天所在月份的第一天為起點
    if start is None:
        start = date.today().replace(day=1)
    _, days = monthrange(start.year, start.month)
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器：用 yield 一次產生一個日期
def date_range(start: datetime, stop: datetime, step: timedelta):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
# strptime 適合格式固定的字串，但大量解析時可能較慢
text = "2012-09-20"
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 若格式固定且只需要簡單切割，手動解析通常更快
def parse_ymd(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
