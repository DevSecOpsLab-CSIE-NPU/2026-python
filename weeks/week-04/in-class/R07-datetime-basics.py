# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期
# 本檔聚焦兩個核心技能：
# 1) 使用 timedelta 做日期時間加減
# 2) 依據星期名稱回推「上一個指定星期幾」

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# timedelta 會把各種單位統整成「天 + 秒 + 微秒」儲存。
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)  # 2
# total_seconds() 可取得完整秒數（包含天數），再自行換算小時。
print(c.total_seconds() / 3600)  # 58.5

dt = datetime(2012, 9, 23)
# datetime + timedelta：往後推算日期時間。
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
# datetime 相減得到 timedelta，可直接取差幾天。
print((d2 - d1).days)  # 89

# 閏年自動處理
# datetime 差值會自動考慮閏年與月份天數，通常比手算安全。
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    # 未提供起點時，預設用今天。
    if start is None:
        start = datetime.today()

    # weekday(): Monday=0 ... Sunday=6
    day_num = start.weekday()
    target = WEEKDAYS.index(dayname)

    # 用模運算取得要回推幾天；若剛好同一天，規則設為回推 7 天。
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24
