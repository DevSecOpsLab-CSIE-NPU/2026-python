# U05. 日期時間的陷阱（3.12–3.15）
# timedelta 不支援月份 / strptime 效能問題
# 本檔重點：日期時間最常見的 bug 來自「月份長度不固定」與「大量解析效能」。
# 日期處理不像整數加法那麼單純，因為月份長度、閏年、解析成本都會影響結果。

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# 先建立一個日期物件作為示範起點。
dt = datetime(2012, 9, 23)
try:
    # timedelta 的設計只支援固定長度單位，例如天、秒、微秒。
    # month 和 year 因為每次長度不固定，所以不能直接傳進去。
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument


# 正確做法：自己計算目標年月，再決定該月合法的最後一天。
def add_one_month(dt: datetime) -> datetime:
    # 先推算目標月份。
    year = dt.year
    month = dt.month + 1

    # 若原本是 12 月，加一個月後要變成隔年 1 月。
    if month == 13:
        year += 1
        month = 1

    # calendar.monthrange(year, month) 會回傳：
    # 1. 該月第一天是星期幾
    # 2. 該月總共有幾天
    # 我們這裡只需要第二個值。
    _, days_in_target_month = calendar.monthrange(year, month)

    # 若原日期是月底，而目標月份沒有那麼多天，
    # 就要把日期壓到該月最後一天。
    # 例如：1/31 + 1 個月，不可能得到 2/31，只能是 2/29 或 2/28。
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# 這裡建立一批固定格式 yyyy-mm-dd 的日期字串，模擬批次資料。
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    # datetime.strptime() 的好處是語意清楚、格式彈性高。
    # 但因為它需要做格式解析，所以在大量固定格式資料時成本較高。
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    # 若輸入格式完全固定，手動 split 再轉 int 往往更快。
    # 缺點是可讀性略差，且格式稍微變動就要自己改程式。
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 先確認兩種方法邏輯上會得到相同結果。
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 再做簡單效能比較，觀察在固定格式資料下的差異。
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
