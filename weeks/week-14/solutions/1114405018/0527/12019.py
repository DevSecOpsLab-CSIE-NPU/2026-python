"""UVA 12019 - Doom's Day Algorithm.

本題固定在 2012 年，所以最簡單的寫法就是直接用 Python 的日期工具。
只要把月份與日期轉成 2012 年的實際日期，就能直接查出星期幾。
"""

from __future__ import annotations

from datetime import date
import sys


WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out_lines: list[str] = []

    for _ in range(t):
        m = int(data[idx])
        d = int(data[idx + 1])
        idx += 2

        # 直接建立 2012 年的日期物件，再用 weekday() 取出星期索引。
        weekday_index = date(2012, m, d).weekday()
        out_lines.append(WEEKDAYS[weekday_index])

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()