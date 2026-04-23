# 【Bloom 階段：R - 記憶與基本操作】
# R07. 日期與時間基礎
# August 的惡意提醒：不要手寫「每個月幾天」的判斷。
# timedelta 會自動處理閏年與月份天數，手寫邏輯只會讓你踩雷。

from datetime import datetime, timedelta

# 1. 時間差運算 (timedelta)
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(f"Total hours: {c.total_seconds() / 3600}")

# 2. 閏年自動處理
# 2012 是閏年，2013 是平年
leap = (datetime(2012, 3, 1) - datetime(2012, 2, 28)).days # 2
normal = (datetime(2013, 3, 1) - datetime(2013, 2, 28)).days # 1
print(f"Leap 2012 diff: {leap}, Normal 2013 diff: {normal}")

# 3. 計算特定星期幾 (例如：上一個星期一)
def get_previous_byday(dayname, start=None):
    if start is None: start = datetime.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_num = start.weekday()
    target = weekdays.index(dayname)
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)

print(f"Last Monday: {get_previous_byday('Monday', datetime(2012, 8, 28))}")
