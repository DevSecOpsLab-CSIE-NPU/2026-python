# R08. 日期範圍與字串轉換（3.14–3.15）
# calendar.monthrange / strptime / strftime

# datetime 用於日期時間處理，date 表示純日期，timedelta 表示時間差
from datetime import datetime, date, timedelta
# monthrange() 可查詢某年某月的星期資訊與該月總天數
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    # 如果沒有指定日期，預設就從本月第一天開始
    if start is None:
        start = date.today().replace(day=1)
    # monthrange() 會回傳 (該月第一天是星期幾, 這個月總天數)
    _, days = monthrange(start.year, start.month)
    # 回傳本月起始日，以及下個月的起始日
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
# 這裡的 last 是下個月第一天，所以要減一天才是當月最後一天
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器
def date_range(start: datetime, stop: datetime, step: timedelta):
    # 每次產生一個時間點，直到到達停止時間前為止
    while start < stop:
        yield start
        start += step


# 這裡示範每隔 6 小時列出一個時間點
for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"
# strptime() 依照指定格式把字串解析成 datetime 物件
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00
# strftime() 則把 datetime 依照格式轉回字串
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 手動解析（比 strptime 快 7 倍）
def parse_ymd(s: str) -> datetime:
    # 直接把年、月、日拆開後轉成整數，建立 datetime 物件
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
