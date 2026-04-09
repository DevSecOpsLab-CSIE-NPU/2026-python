# U05. 日期時間的陷阱（3.12–3.15）
# 本程式示範日期時間處理中的常見陷阱和解決方案：
# 3.12 timedelta 不支援月份 - timedelta 無法直接加減月份
# 3.15 strptime 效能問題 - 解析大量日期字串的效能優化

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# 問題：datetime.timedelta 不支援 months 或 years 參數
# 原因：不同月份的天數不固定（28-31天），加上月份會有歧義

dt = datetime(2012, 9, 23)

# 錯誤：timedelta 不接受 months 參數
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")


# 正確做法：手動計算目標月份，並處理月份天數限制
def add_one_month(dt: datetime) -> datetime:
    """
    安全地為日期加上一個月，自動處理月份天數差異

    演算法：
    1. 計算目標年月
    2. 取得目標月份的最大天數
    3. 將日期限制在目標月份的有效範圍內

    Args:
        dt: 原始日期時間

    Returns:
        加上一個月後的日期時間
    """
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    if month == 13:  # 12月 + 1 = 次年1月
        year += 1
        month = 1

    # 取得目標月份的天數，並把日期限制在該月最後一天
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month)  # 避免如 1/31 + 1月 = 2/31（不存在）

    return dt.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29（2月只有29天，自動調整）
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# 問題：datetime.strptime() 對於大量日期解析很慢
# 原因：每次呼叫都會重新編譯正則表達式
# 解決方案：手動解析比 strptime 快約 10 倍

# 測試資料：大量日期字串
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


# 使用 strptime 解析
def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


# 手動解析：直接分割字串並轉換
def use_manual(s: str) -> datetime:
    y, m, d = s.split("-")  # 分割字串
    return datetime(int(y), int(m), int(d))  # 直接建構 datetime


# 驗證兩種方法結果相同
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 效能測試：解析所有日期 100 次
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
