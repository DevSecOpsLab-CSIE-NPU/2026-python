# U05. 日期時間的陷阱（3.12–3.15）
# 說明：timedelta 不支援月份 / strptime 效能問題

import timeit
import calendar
from datetime import datetime, timedelta

# ─────────────────────────────────────────────────────────────────
# timedelta 不支援月份（3.12）
# 說明：timedelta 只能用於天/秒/微秒的運算，不支援直接加月份
# ─────────────────────────────────────────────────────────────────

dt = datetime(2012, 9, 23)

try:
    # 嘗試直接加月份（會報錯！）
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 輸出：'months' is an invalid keyword argument


# ─────────────────────────────────────────────────────────────────
# 正確做法：用 calendar 取得目標月份天數，並將日期 clamp 到該月最後一天
# 說明：自訂函數處理月份加法，注意邊界情況（如 1/31 加一個月）
# ─────────────────────────────────────────────────────────────────

def add_one_month(dt: datetime) -> datetime:
    """
    正確地將日期加一個月
    
    參數：
        dt：原始日期
    
    回傳：
        加一個月後的日期（會自動處理月末邊界）
    """
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1
    
    # 取得目標月份的天數
    _, days_in_target_month = calendar.monthrange(year, month)
    
    # 將日期限制在該月最後一天（防止 1/31 變成 2/31）
    day = min(dt.day, days_in_target_month)
    
    return dt.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 輸出：2012-02-29（閏年）
print(add_one_month(datetime(2012, 9, 23)))  # 輸出：2012-10-23


# ─────────────────────────────────────────────────────────────────
# strptime 效能問題（3.15）
# 說明：strptime 功能強大但效能較差，對固定格式可用手動解析優化
# ─────────────────────────────────────────────────────────────────

# 建立測試資料：12 個月 x 28 天 = 336 個日期字串
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    """使用 strptime 解析（功能強但效能較差）"""
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    """手動解析（效能較好，但只適用固定格式）"""
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 驗證兩者結果相同
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 效能測試：各執行 100 次
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")