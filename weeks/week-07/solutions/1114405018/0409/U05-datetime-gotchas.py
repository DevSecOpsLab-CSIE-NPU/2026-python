# U05. 日期時間的陷阱（3.12–3.15）
# 這份範例主要示範兩個常見問題：
# 1. timedelta 只能表示固定長度的時間差，不能直接加「月份」。
# 2. datetime.strptime() 很方便，但在大量重複解析時通常比手動切字串慢。

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# timedelta 代表的是「固定秒數的時間差」，例如天、秒、微秒。
# 但「月份」不是固定長度，因為不同月份有 28、29、30、31 天，所以 timedelta 無法直接用 months=1。
dt = datetime(2012, 9, 23)
try:
    # 這行刻意示範錯誤用法，讓你看到 timedelta 並不接受 months 這個參數。
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument


# 正確做法：用 calendar 取得目標月份天數，並將日期 clamp 到該月最後一天
def add_one_month(dt: datetime) -> datetime:
    # 先計算往後推一個月之後的年與月。
    # 如果原本是 12 月，往後一個月就會跨到下一年 1 月。
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1

    # monthrange() 會回傳該月第一天是星期幾，以及那個月總共有幾天。
    # 這裡只需要第二個值，也就是目標月份的天數。
    _, days_in_target_month = calendar.monthrange(year, month)
    # 如果原日期的日數超出目標月份上限，就把它壓到該月最後一天。
    # 這樣像 1/31 加一個月，會正確變成 2/28 或 2/29，而不會報錯。
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


# 下面兩個例子分別示範平年與一般日期往後一個月的結果。
print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# 先建立一批日期字串，方便測試大量解析時的效能差異。
# 這種批次測試可以讓速度差距更明顯，也更接近實務上的資料匯入情境。
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    # strptime() 會依照格式字串逐步解析，因此彈性高，但也會多一些解析成本。
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    # 手動切字串再轉成整數，格式固定時通常更直接，也常常比 strptime() 快。
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 先確認兩種方法解析出來的結果相同，避免只比速度卻忽略正確性。
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 這裡用 timeit 比較兩種方式的耗時。
# number 設大一些是為了降低單次執行的偶然誤差，讓比較更穩定。
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
# 實際倍數會受 Python 版本與電腦效能影響，但手動解析通常會比較快。
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
