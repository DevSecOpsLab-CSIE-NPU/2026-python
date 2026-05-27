"""
UVA 12019 - Doom's Day Algorithm

題目重點：
輸入多個日期 m d，判斷這個日期在 2011 年是星期幾。
題目固定年份是 2011，所以不用處理其他年份。

解法想法：
這題可以手算 Doomsday，但 Python 內建 datetime 已經能正確計算日期星期。
datetime.date(2011, month, day).weekday() 會回傳 0 到 6：
0 是 Monday，1 是 Tuesday，依此類推到 6 是 Sunday。
因此準備一個星期名稱串列，就能用 index 直接取得答案。
"""

import datetime
import sys
from typing import List, TextIO


# weekday() 回傳的數字剛好可以對應到這個串列的位置。
WEEKDAYS: List[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def weekday_2011(month: int, day: int) -> str:
    """回傳 2011 年指定月日的星期名稱。"""
    date = datetime.date(2011, month, day)
    weekday_index = date.weekday()
    return WEEKDAYS[weekday_index]


def solve(input_stream: TextIO = sys.stdin) -> str:
    """讀取 T 筆日期資料，回傳每筆日期的星期。"""
    tokens = input_stream.read().split()
    test_count = int(tokens[0])
    output = []

    # tokens[0] 是測資筆數，後面每兩個 token 是一組 month day。
    index = 1
    for _ in range(test_count):
        month = int(tokens[index])
        day = int(tokens[index + 1])

        output.append(weekday_2011(month, day))
        index += 2

    return "\n".join(output)


if __name__ == "__main__":
    print(solve())
