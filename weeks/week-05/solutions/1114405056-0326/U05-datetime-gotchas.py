import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援 months 參數 ─────────────────────────
# timedelta 只接受：days, seconds, microseconds, milliseconds, minutes, hours, weeks
# 沒有 months 或 years，因為「一個月」天數不固定
dt = datetime(2012, 9, 23)
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]  → 拋 TypeError
except TypeError as e:
    print(f"TypeError: {e}")


def add_one_month(dt: datetime) -> datetime:
    """安全地將日期往後推一個月，處理月底邊界（如 1/31 → 2/28）。"""
    year = dt.year
    month = dt.month + 1
    # 若月份超過 12，進位到下一年
    if month == 13:
        year += 1
        month = 1

    # monthrange 取得目標月份的天數，避免超出範圍（如 2/31 不存在）
    _, days_in_target_month = calendar.monthrange(year, month)
    # 若當前日超過目標月天數，就取月底
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


# 1/31 + 1 month → 2/29（2012 閏年）
print(add_one_month(datetime(2012, 1, 31)))
# 9/23 + 1 month → 10/23
print(add_one_month(datetime(2012, 9, 23)))

# ── 日期字串解析效能比較 ──────────────────────────────────
# strptime 每次都需解析格式字串，有額外開銷
# 手動 split + datetime() 在固定格式下速度更快
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    """使用 strptime 解析日期字串（較通用但稍慢）。"""
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    """手動分割並直接建構 datetime（較快）。"""
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 驗證兩種方法結果相同
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s 手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
