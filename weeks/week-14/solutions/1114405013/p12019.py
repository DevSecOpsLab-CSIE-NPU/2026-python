"""
UVA 12019 — Doom's Day Algorithm（世界末日演算法）
ZeroJudge f709

功能：使用 Doom's Day 演算法計算 2012 年任意日期是星期幾
"""

# 2012 年每個月的 Doomsday 參考日期
# Doomsday 定義為該月最後一個偶數日
DOOMSDAY = {
    1: 10,   # 1 月 10 日
    2: 21,   # 2 月 21 日
    3: 7,    # 3 月 7 日
    4: 4,    # 4 月 4 日
    5: 9,    # 5 月 9 日
    6: 6,    # 6 月 6 日
    7: 11,   # 7 月 11 日
    8: 8,    # 8 月 8 日
    9: 5,    # 9 月 5 日
    10: 10,  # 10 月 10 日
    11: 7,   # 11 月 7 日
    12: 12,  # 12 月 12 日
}

# 星期對照表，索引 0 對應 Wednesday（2012 年 Doomsday）
WEEKDAYS = [
    "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday", "Monday", "Tuesday",
]


def day_of_week(month, day):
    """
    計算 2012 年某月某日是星期幾

    參數：
        month: int — 月份（1~12）
        day: int   — 日期

    回傳值：
        str — 星期幾的英文全名
    """
    # 計算目標日期與該月 Doomsday 的差距
    diff = day - DOOMSDAY[month]
    # Doomsday 是 Wednesday（索引 0），加上差距即可
    return WEEKDAYS[diff % 7]


def solve() -> None:
    """讀取標準輸入，輸出每筆日期對應的星期幾"""
    t = int(input().strip())
    for _ in range(t):
        m, d = map(int, input().split())
        print(day_of_week(m, d))


if __name__ == "__main__":
    solve()
