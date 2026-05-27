"""UVA 12019 - Doom's Day Algorithm (year 2012)"""

from __future__ import annotations

import datetime as dt
import sys


def weekday_name_2012(month: int, day: int) -> str:
    """回傳 2012/ month/day 對應的英文星期名稱。"""
    return dt.date(2012, month, day).strftime("%A")


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    t = int(lines[0])
    out: list[str] = []
    for i in range(1, t + 1):
        m, d = map(int, lines[i].split())
        out.append(weekday_name_2012(m, d))
    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
