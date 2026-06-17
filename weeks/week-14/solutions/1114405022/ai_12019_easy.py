"""
UVA 12019 — Doom's Day Algorithm 的簡單版。

做法：直接使用 Python 的 datetime 模組，因為題目限定在 2012 年，
所以只要把月份和日期組成 date，再查 weekday() 就可以了。
"""

import datetime


WEEKDAY_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def weekday_name(m: int, d: int) -> str:
    """回傳 2012 年 m/d 對應的星期英文全名。"""
    return WEEKDAY_NAMES[datetime.date(2012, m, d).weekday()]


def solve() -> None:
    """讀取多組測資並輸出答案。"""
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    t = int(lines[0])
    out = []
    for i in range(1, t + 1):
        m, d = map(int, lines[i].split())
        out.append(weekday_name(m, d))

    print("\n".join(out))


if __name__ == "__main__":
    solve()
