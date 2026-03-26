# R07. 日期時間基本運算（3.12–3.13）
#
# 本檔案示範兩個常見主題：
# 1) timedelta 與 datetime 的加減運算
# 2) 依照指定星期名稱，回推「上一個」該星期的日期
#
# 重要觀念：
# - datetime 代表「某個時間點」
# - timedelta 代表「時間間隔（幾天幾小時...）」
# - datetime ± timedelta 可以得到新的 datetime

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# 建立兩個時間差：
# a = 2 天 6 小時
# b = 4.5 小時
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

# timedelta 可以直接相加
c = a + b

# .days 只會回傳「整天數」部分
print(c.days)  # 2

# 若要取得完整秒數（含小時/分鐘/秒），用 total_seconds()
# 這裡除以 3600 轉成小時
print(c.total_seconds() / 3600)  # 58.5

# datetime + timedelta：將時間點往後推指定天數
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

# datetime - datetime：得到 timedelta（兩時間點差距）
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年自動處理
# 2012 是閏年，2/28 到 3/1 相差 2 天（跨過 2/29）
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
# 2013 是平年，2/28 到 3/1 相差 1 天
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
# Python 的 weekday() 編號規則：
# Monday=0, Tuesday=1, ..., Sunday=6
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
    # 若未提供起始日，預設使用今天
    if start is None:
        start = datetime.today()

    # 目前日期是星期幾（0~6）
    day_num = start.weekday()

    # 目標星期名稱轉為對應編號（0~6）
    target = WEEKDAYS.index(dayname)

    # 計算要往回退幾天：
    # (7 + day_num - target) % 7 可得到與目標星期的差距
    # 若結果為 0，表示今天就是目標星期，但題意是「上一個」
    # 因此用 `or 7` 讓它退回 7 天
    days_ago = (7 + day_num - target) % 7 or 7

    # 回傳往回推 days_ago 天後的日期
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
# 從 2012-08-28（週二）回推上一個週一與週五
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24
