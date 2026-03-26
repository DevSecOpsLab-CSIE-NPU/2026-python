# R08. 日期範圍與字串轉換（3.14–3.15）
# calendar.monthrange / strptime / strftime
# 本檔示範：
# 1) 如何安全取得某月份起訖範圍
# 2) 如何用生成器走訪時間區間
# 3) 日期字串與 datetime 的互轉技巧

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    # 未提供起點時，取今天所在月份的第一天。
    if start is None:
        start = date.today().replace(day=1)

    # monthrange 回傳 (該月第一天是星期幾, 該月天數)。
    _, days = monthrange(start.year, start.month)
    # 回傳 [start, end) 半開區間，end 指到「下個月第一天」。
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器
def date_range(start: datetime, stop: datetime, step: timedelta):
    # 以半開區間 [start, stop) 產生序列，避免終點重複計算。
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"
# strptime：依指定格式把字串解析成 datetime。
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00
# strftime：把 datetime 轉成格式化字串。
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 手動解析（比 strptime 快 7 倍）
def parse_ymd(s: str) -> datetime:
    # 固定格式時可手動切割轉型，通常效能更好。
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
