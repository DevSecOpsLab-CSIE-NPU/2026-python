# U05. 日期時間的陷阱（3.12–3.15）
#
# 這個檔案示範兩個常見的日期時間問題：
# 1. timedelta 只能表示固定的時間長度，不能直接加「月份」。
# 2. datetime.strptime() 很方便，但在大量解析時可能比手動拆字串慢。

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# timedelta 表示的是固定長度的時間差，例如秒、分鐘、天。
# 但「一個月」不是固定天數，因為有 28、29、30、31 天的差異，
# 所以 timedelta 不提供 months 參數。
dt = datetime(2012, 9, 23)
try:
    # 這裡故意示範錯誤用法，讓讀者知道 timedelta(months=1) 會失敗。
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument


# 正確做法：如果真的要「加一個月」，通常要自己處理年、月、日的邊界。
# 例如 1 月 31 日加一個月，不能直接得到 2 月 31 日，因為那天不存在。
# 這裡的做法是：先算出目標年月，再把日期限制在該月最後一天。
def add_one_month(dt: datetime) -> datetime:
    # 先計算目標的年與月；如果月份超過 12，就換到下一年 1 月。
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1

    # calendar.monthrange() 會回傳該月第一天的星期與該月總天數。
    # 我們只需要天數，然後把原本的 day 限制在合法範圍內。
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month)

    # replace() 只改變指定欄位，不會重新計算其他欄位。
    return dt.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# datetime.strptime() 很適合讀取格式固定的日期字串，程式碼也很清楚。
# 但它內部要做格式解析，所以在大量資料處理時，可能比手動 split 再轉型慢。
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    # 直接交給 strptime() 解析格式，最直觀，但未必是最快。
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    # 手動拆出年月日，再轉成整數建立 datetime。
    # 當格式固定且簡單時，這種寫法常常比 strptime() 更快。
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 先確認兩種方法的結果一致，避免只比速度卻忽略正確性。
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# timeit 比較大量解析時的差異。若資料量很大，手動解析常有明顯優勢。
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
