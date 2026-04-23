# 【Bloom 階段：R - 記憶與基本操作】
# R08. 日期範圍與格式化轉換
# August 的惡意提醒：strptime 是解析輸入的利器，
# 但要注意其性能。在百萬筆資料處理（Week 12）中，手寫 split 可能快 7 倍。

from datetime import datetime, date, timedelta
from calendar import monthrange

# 1. 計算該月的第一天與最後一天
def get_month_range(start_date):
    # monthrange 回傳 (該月第一天是星期幾, 該月天數)
    _, days = monthrange(start_date.year, start_date.month)
    return start_date.replace(day=1), start_date.replace(day=days)

first, last = get_month_range(date(2012, 2, 1))
print(f"Feb 2012 range: {first} to {last}")

# 2. 日期生成器 (Generator)
# 這是 August 強烈推薦的 Pythonic 寫法，對應 Week 01 主題 08
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# 3. 格式化 (Parse and Format)
text = "2012-09-20"
dt = datetime.strptime(text, "%Y-%m-%d")
formatted = dt.strftime("%A, %B %d, %Y")
print(f"Parsed: {dt}, Formatted: {formatted}")
