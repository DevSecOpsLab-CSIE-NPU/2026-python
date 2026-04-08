from __future__ import annotations

import sys
from collections import defaultdict


def solve(data: str) -> str:
    values = [int(x) for x in data.split()]
    if not values:
        return ""

    n = values[0]
    s = values[1 : 1 + n]

    sum2: dict[int, int] = defaultdict(int)
    for a in s:
        for b in s:
            sum2[a + b] += 1

    sum3: dict[int, int] = defaultdict(int)
    for ab, cnt in sum2.items():
        for c in s:
            sum3[ab + c] += cnt

    total = 0
    for f in s:
        ways = 0
        for ab, cnt in sum2.items():
            ways += cnt * sum3.get(f - ab, 0)
        total += ways

    return str(total)


if __name__ == "__main__":
    out = solve(sys.stdin.read())
    if out:
        sys.stdout.write(out)
