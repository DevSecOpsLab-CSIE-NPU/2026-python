# R08. 日期範圍與字串轉換（3.14–3.15）
# calendar.monthrange / strptime / strftime

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    # 若未指定日期，預設用「本月第一天」
    if start is None:
        start = date.today().replace(day=1)
    # monthrange(year, month) -> (該月第一天是星期幾, 該月總天數)
    _, days = monthrange(start.year, start.month)
    # 回傳 [起始日, 下一個月第一天)
    # 使用「左閉右開」區間，迭代時邏輯會更一致
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
# last 是「下個月第一天」，所以顯示月底要再減一天
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器
def date_range(start: datetime, stop: datetime, step: timedelta):
    # 與 range() 類似：包含 start，不包含 stop
    while start < stop:
        yield start
        # 每次往前推進 step（可用小時、天數等）
        start += step


# 每 6 小時產生一筆時間點
for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"
# strptime: 依指定格式把字串解析成 datetime
# %Y=四位數年份、%m=兩位數月份、%d=兩位數日期
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00
# strftime: 把 datetime 依格式輸出為字串
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 手動解析（比 strptime 快 7 倍）
def parse_ymd(s: str) -> datetime:
    # 直接拆分 YYYY-MM-DD，再轉成整數建構 datetime
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
