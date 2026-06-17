"""
手寫版：UVA 11461 — Square Numbers
"""

import math


def count_squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)


def solve():
    import sys
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        out.append(str(count_squares(a, b)))
    print("\n".join(out))


if __name__ == "__main__":
    solve()
