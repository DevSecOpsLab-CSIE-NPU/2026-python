# R08. 日期範圍與字串轉換（3.14–3.15）
#
# 本檔案示範三個實用情境：
# 1) 計算某個月份的日期範圍
# 2) 以固定步長迭代日期時間（產生時間序列）
# 3) 日期字串與 datetime 物件互相轉換
#
# 主要工具：
# - calendar.monthrange：取得某月天數
# - datetime.strptime：字串 -> datetime
# - datetime.strftime：datetime -> 格式化字串

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    # 若未提供日期，預設使用今天所在月份的「1 號」
    if start is None:
        start = date.today().replace(day=1)

    # monthrange(year, month) 回傳 (該月第一天是星期幾, 該月天數)
    # 這裡只需要天數，因此第一個值以 _ 忽略
    _, days = monthrange(start.year, start.month)

    # 回傳 [月初, 下個月月初) 的半開區間
    # 這種表示法在迭代時通常更直覺、也不易有邊界錯誤
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
# 由於 last 是「下個月月初」，印出時減 1 天即可得到當月最後一天
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器
def date_range(start: datetime, stop: datetime, step: timedelta):
    # 以半開區間 [start, stop) 產生序列：不包含 stop
    while start < stop:
        yield start
        start += step


# 從 9/1 00:00 到 9/2 00:00，每 6 小時產生一個時間點
for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"

# strptime 依照格式碼解析字串：
# %Y=四位年份, %m=兩位月份, %d=兩位日期
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00

# strftime 將 datetime 格式化為可讀字串
# %A=星期全名, %B=月份全名
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 手動解析（比 strptime 快 7 倍）
def parse_ymd(s: str) -> datetime:
    # 若格式固定為 YYYY-MM-DD，手動 split + int 轉換可更快
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
