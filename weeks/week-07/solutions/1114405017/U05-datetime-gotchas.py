import timeit
import calendar
from datetime import datetime, timedelta

# ── 陷阱一：timedelta 不支援月份（3.12） ──────────────────────
# 原因是「一個月」的天數並不固定（28, 29, 30, 或 31 天），
# 為了維持運算的精確性，Python 標準函式庫的 timedelta 僅支援固定長度的單位（如天、秒、微秒）。
dt = datetime(2012, 9, 23)
try:
    # 嘗試直接加一個月會拋出錯誤，因為 timedelta 不接受 'months' 參數
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 輸出：'months' is an invalid keyword argument


# 【正確做法】：手動計算月份進位，並處理「月底溢出」的問題
def add_one_month(dt: datetime) -> datetime:
    """
    將給定的 datetime 物件增加一個月。
    處理邏輯：
    1. 計算目標年份與月份。
    2. 處理 12 月跨年到隔年 1 月的情況。
    3. 使用 calendar.monthrange 確保日期不會超過目標月份的最大天數（例如 1/31 加一月應為 2/29）。
    """
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    
    # 處理跨年邏輯
    if month == 13:
        year += 1
        month = 1

    # 取得目標月份的總天數 (calendar.monthrange 回傳: (該月第一天是星期幾, 該月總天數))
    _, days_in_target_month = calendar.monthrange(year, month)
    
    # 關鍵步驟：如果原日期的 day (例如 31) 超過目標月天數 (例如 28)，
    # 則取該月最後一天 (用 min 函數達成 clamp 效果)
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


# 測試：2012 是閏年，2 月有 29 天
print(add_one_month(datetime(2012, 1, 31)))  # 輸出：2012-02-29
print(add_one_month(datetime(2012, 9, 23)))  # 輸出：2012-10-23


# ── 陷阱二：strptime 效能問題（3.15） ─────────────────────────
# datetime.strptime 是萬用解析器，內部使用正則表達式且需處理本地化設定 (Locale)，
# 在處理大量「格式固定」的字串時，效能遠低於手動切割字串。

# 建立一個測試資料集：1 到 12 月，每月 1 到 28 號
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 28)]


def use_strptime(s: str) -> datetime:
    """使用官方標準的 strptime 解析字串"""
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    """
    使用手動解析：針對已知格式 (YYYY-MM-DD) 進行切割。
    這種方法跳過了複雜的正則匹配，速度極快。
    """
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 驗證兩者結果是否相同
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 進行效能測試（各執行 100 次循環）
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)

print(f"strptime 耗時: {t1:.3f}s")
print(f"手動解析 耗時: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")