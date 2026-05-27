from __future__ import annotions

from datetime import date
import sys

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        m = int(data[idx]); d = int(data[idx+1]); idx += 2
        wd = date(2012, m, d).weekday()
        out.append(WEEKDAYS[wd])

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
    