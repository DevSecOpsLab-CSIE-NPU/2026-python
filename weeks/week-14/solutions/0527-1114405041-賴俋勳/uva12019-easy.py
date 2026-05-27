# UVA 12019（好記版）
# 題目固定 2012 年，直接用 datetime 轉星期最直覺。

import datetime as dt
import sys


def name_of_week(m, d):
    return dt.date(2012, m, d).strftime("%A")


def solve(text):
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    t = int(lines[0])
    out = []
    for i in range(1, t + 1):
        m, d = map(int, lines[i].split())
        out.append(name_of_week(m, d))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
