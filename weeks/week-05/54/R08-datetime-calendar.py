# R08. 日期範圍與字串轉換（3.14–3.15）
# calendar.monthrange / strptime / strftime

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    if start is None:
        start = date.today().replace(day=1)
    _, days = monthrange(start.year, start.month)
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器
def date_range(start: datetime, stop: datetime, step: timedelta):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 手動解析（比 strptime 快 7 倍）
def parse_ymd(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
