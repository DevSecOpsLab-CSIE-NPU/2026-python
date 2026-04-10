# R08. 日期範圍與字串轉換（3.14–3.15）
# 說明：calendar.monthrange / strptime / strftime 的用法

from datetime import datetime, date, timedelta
from calendar import monthrange


# ─────────────────────────────────────────────────────────────────
# 3.14 當月日期範圍
# 說明：使用 monthrange 取得當月天數
# ─────────────────────────────────────────────────────────────────

def get_month_range(start: date | None = None) -> tuple[date, date]:
    """
    取得某月的日期範圍
    
    參數：
        start：起始日期，預設為當月第一天
    
    回傳：
        (當月第一天, 當月最後一天的隔天)
        使用時需要減一天才能得到最後一天
    """
    # 如果沒有指定起始日期，預設為當月第一天
    if start is None:
        start = date.today().replace(day=1)
    
    # monthrange(year, month) 回傳 (該月第一天是星期幾, 該月天數)
    # 星期幾用 0=星期一, 6=星期日 表示
    _, days = monthrange(start.year, start.month)
    
    # 回傳當月第一天和下月第一天（不包含的最後一天）
    return start, start + timedelta(days=days)


# 測試：2012年8月
first, last = get_month_range(date(2012, 8, 1))
# last 是下月第一天，需要減一天才是 8 月最後一天
print(first, "~", last - timedelta(days=1))  # 輸出：2012-08-01 ~ 2012-08-31


# ─────────────────────────────────────────────────────────────────
# 通用日期迭代生成器
# 說明：產生指定日期範圍內的連續日期
# ─────────────────────────────────────────────────────────────────

def date_range(start: datetime, stop: datetime, step: timedelta):
    """
    產生日期範圍內的日期序列
    
    參數：
        start：起始日期（包含）
        stop：結束日期（不包含）
        step：每次遞增的時間間隔
    """
    while start < stop:
        yield start
        start += step


# 測試：產生 2012年9月1日 每 6 小時的日期
for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 輸出：
# 2012-09-01 00:00:00
# 2012-09-01 06:00:00
# 2012-09-01 12:00:00
# 2012-09-01 18:00:00


# ─────────────────────────────────────────────────────────────────
# 3.15 字串轉換為日期
# 說明：strptime 解析字串，strftime 格式化輸出
# ─────────────────────────────────────────────────────────────────

# 待解析的字串
text = "2012-09-20"

# strptime()：將字串解析為 datetime 物件
# 第一個參數是要解析的字串
# 第二個參數是格式字串，%Y=年, %m=月, %d=日
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 輸出：2012-09-20 00:00:00

# strftime()：將 datetime 格式化為字串
# %A=完整星期名稱, %B=完整月份名稱
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 輸出：'Thursday September 20, 2012'


# ─────────────────────────────────────────────────────────────────
# 手動解析（比 strptime 快 7 倍）
# 說明：對於固定格式的字串，手動解析比 strptime 更快
# ─────────────────────────────────────────────────────────────────

def parse_ymd(s: str) -> datetime:
    """
    快速解析 "年-月-日" 格式的字串
    
    這種方法比 strptime 快約 7 倍，因為：
    1. 不需要解析複雜的格式字串
    2. 使用簡單的字串分割和轉換
    """
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 輸出：2012-09-20 00:00:00