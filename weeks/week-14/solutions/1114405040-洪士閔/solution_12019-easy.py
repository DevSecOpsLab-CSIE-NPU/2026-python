# UVA 12019 - Doom's Day Algorithm
#
# 這是比較簡單、好記的寫法。
#
# 題目要求：
# 輸入 2011 年的某個月、某一天，輸出那天是星期幾。
#
# 最簡單的做法：
# 直接使用 Python 內建的 datetime 模組。
# datetime.date(2011, month, day) 可以建立一個日期物件。
# .weekday() 可以取得星期幾：
#   0 -> Monday
#   1 -> Tuesday
#   2 -> Wednesday
#   3 -> Thursday
#   4 -> Friday
#   5 -> Saturday
#   6 -> Sunday

import datetime


weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

t = int(input())

for _ in range(t):
    month, day = map(int, input().split())

    # 題目固定是 2011 年，所以年份直接寫 2011。
    date = datetime.date(2011, month, day)

    # weekday_index 會是 0 到 6，可以直接當作 weekdays 的索引。
    weekday_index = date.weekday()
    print(weekdays[weekday_index])
