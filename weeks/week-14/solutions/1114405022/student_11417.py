"""
手寫版：UVA 11417 — GCD
"""

import math


def gcd_sum(n):
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve():
    import sys
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        out.append(str(gcd_sum(n)))
    print("\n".join(out))


if __name__ == "__main__":
    solve()
