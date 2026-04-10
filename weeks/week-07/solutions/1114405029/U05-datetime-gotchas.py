# U05. 日期時間的陷阱（3.12–3.15）
# timedelta 不支援月份 / strptime 效能問題

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# 因為「一個月」的天數是不固定的（28-31天），所以 timedelta 只支援到 weeks
dt = datetime(2012, 9, 23)
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 報錯：'months' 是無效參數

# 正確做法：手動計算月份進位，並處理月末溢出問題（例如 1/31 加一月變 2/29）
def add_one_month(dt: datetime) -> datetime:
    year = dt.year
    month = dt.month + 1
    if month == 13: # 跨年處理
        year += 1
        month = 1

    # 使用 calendar.monthrange 取得該月最大天數，避免日期超出範圍
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month) # 若原日期是 31 號而目標月只有 30 天，自動轉為 30 號

    return dt.replace(year=year, month=month, day=day)

print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29 (閏年處理)
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# strptime 是基於 Python 實作的，包含大量正則匹配，在處理數萬筆資料時會成為瓶頸
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]

def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")

def use_manual(s: str) -> datetime:
    # 已知格式固定時，使用 split 或切片手動解析速度快很多
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))

assert use_strptime("2012-09-20") == use_manual("2012-09-20")

t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")