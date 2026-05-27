"""
UVA 12019 — 容易記憶版

直接使用 Python 內建的 datetime 模組，
不用背 Doomsday 日期，最容易記憶。
"""

import datetime


def day_of_week(month, day):
    """
    計算 2012 年某月某日是星期幾（內建函式版）

    使用 datetime.date 搭配 strftime('%A')，
    一行程式碼搞定，完全不用記演算法。
    """
    # datetime 會自動處理閏年及月份天數
    return datetime.date(2012, month, day).strftime("%A")


def solve() -> None:
    """讀取標準輸入，輸出每筆日期對應的星期幾"""
    t = int(input().strip())
    for _ in range(t):
        m, d = map(int, input().split())
        print(day_of_week(m, d))


if __name__ == "__main__":
    solve()
