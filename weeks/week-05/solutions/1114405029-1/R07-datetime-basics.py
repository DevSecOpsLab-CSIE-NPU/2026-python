# R07. 日期時間基本運算（3.12–3.13）
# 說明：timedelta 加減 / weekday() 計算指定星期

from datetime import datetime, timedelta

# ─────────────────────────────────────────────────────────────────
# 3.12 timedelta 基本運算
# 說明：timedelta 用於表示時間的差值，可進行加減運算
# ─────────────────────────────────────────────────────────────────

# 建立時間差：2 天又 6 小時
a = timedelta(days=2, hours=6)

# 建立時間差：4.5 小時（小數會轉換為分和秒）
b = timedelta(hours=4.5)

# timedelta 相加
c = a + b
print(c.days)  # 輸出：2（總天數）

# 取得總秒數並轉換為小時
print(c.total_seconds() / 3600)  # 輸出：58.5（小時）

# 日期加上 timedelta
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 輸出：2012-10-03 00:00:00

# 兩個日期相減得到 timedelta
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 輸出：89（相隔天數）

# 閏年自動處理：2012 年是閏年，2 月有 29 天
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 輸出：2

# 平年：2013 年不是閏年，2 月只有 28 天
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 輸出：1

# ─────────────────────────────────────────────────────────────────
# 3.13 計算指定星期日期
# 說明：使用 weekday() 取得星期幾（0=星期一，6=星期日）
# ─────────────────────────────────────────────────────────────────

# 星期名稱對照表（索引 0 對應 Monday）
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
    """
    取得某個日期之前最近的特定星期幾的日期
    
    參數：
        dayname：目標星期名稱（如 "Monday"）
        start：起始日期，預設為今天
    
    回傳：
        在 start 之前最近的那個星期幾的日期
    """
    # 如果沒有指定起始日期，預設為今天
    if start is None:
        start = datetime.today()
    
    # 取得起始日期是星期幾（0=星期一，6=星期日）
    day_num = start.weekday()
    
    # 找出目標星期在 WEEKDAYS 清單中的索引
    target = WEEKDAYS.index(dayname)
    
    # 計算需要往前多少天
    # (7 + day_num - target) % 7 算出天數差
    # 如果結果是 0，表示當天就是目標星期，需要往回 7 天
    days_ago = (7 + day_num - target) % 7 or 7
    
    # 回推指定天數前的日期
    return start - timedelta(days=days_ago)


# 測試：2012年8月28日是星期二
base = datetime(2012, 8, 28)
print(get_previous_byday("Monday", base))  # 輸出：2012-08-27（前一個星期一）
print(get_previous_byday("Friday", base))  # 輸出：2012-08-24（前一個星期五）