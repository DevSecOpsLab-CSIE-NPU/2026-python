from datetime import datetime, date, timedelta
from calendar import monthrange


def get_month_range(start: date | None = None) -> tuple[date, date]:
    """回傳某月的第一天與下個月第一天（左閉右開區間）。"""
    if start is None:
        # 若未指定，預設為本月第一天
        start = date.today().replace(day=1)
    # monthrange(year, month) → (該月第一天是星期幾, 該月天數)
    _, days = monthrange(start.year, start.month)
    # 回傳 (月初, 下個月月初)，方便做左閉右開的日期範圍
    return start, start + timedelta(days=days)


# 取得 2012 年 8 月的日期範圍
first, last = get_month_range(date(2012, 8, 1))
# last 是 9/1，減一天得到月底 8/31
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


def date_range(start: datetime, stop: datetime, step: timedelta):
    """產生器：以 step 為間隔，從 start 到 stop（不含）逐步產出 datetime。"""
    while start < stop:
        yield start
        start += step


# 以 6 小時為間隔，列出 2012-09-01 當天的時間點
for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)

# ── 字串與 datetime 互轉 ──────────────────────────────────
text = "2012-09-20"
# strptime：parse string → datetime，需指定格式字串
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)
# strftime：format datetime → string
print(datetime.strftime(dt, "%A %B %d, %Y"))  # Thursday September 20, 2012


def parse_ymd(s: str) -> datetime:
    """手動分割 'YYYY-MM-DD' 字串並建構 datetime（比 strptime 快）。"""
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))
