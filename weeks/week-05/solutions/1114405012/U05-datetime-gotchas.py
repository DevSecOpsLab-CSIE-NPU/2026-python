# U05. 日期時間的陷阱（3.12–3.15）
# timedelta 不支援月份 / strptime 效能問題

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
dt = datetime(2012, 9, 23)
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"錯誤示範：{e}")  # timedelta 不認得 months


# 正確做法：用 calendar 取得目標月份天數，並將日期 clamp 到該月最後一天
# timedelta 不能直接表示「加一個月」，所以要自己算新年月，再處理月底溢位。
def add_one_month(dt: datetime) -> datetime:
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1

    # 取得目標月份的天數，並把日期限制在該月最後一天
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


print("2012-01-31 加一個月：", add_one_month(datetime(2012, 1, 31)))  # 2012-02-29
print("2012-09-23 加一個月：", add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# strptime 很方便，但大量解析時會比較慢。
# 如果格式固定且非常單純，手動切字串再組 datetime 往往更快。
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


assert use_strptime("2012-09-20") == use_manual("2012-09-20")

t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime 解析時間：{t1:.3f}s")
print(f"手動解析時間：{t2:.3f}s")
print(f"手動解析大約快 {t1 / t2:.1f} 倍")
