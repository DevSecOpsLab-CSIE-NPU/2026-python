from __future__ import annotations
import sys
from collections import Counter


def count_six(values: list[int]) -> int:
    s3 = Counter()
    for a in values:
        for b in values:
            ab = a + b
            for c in values:
                s3[ab + c] += 1
    s2 = Counter()
    for d in values:
        for e in values:
            s2[d + e] += 1
    total = 0
    for x, cx in s3.items():
        m = 0
        for f in values:
            m += s2.get(f - x, 0)
        total += cx * m
    return total


def solve(data: str) -> str:
    t = data.strip().split()
    if not t:
        return ""
    n = int(t[0])
    vals = list(map(int, t[1 : 1 + n]))
    return str(count_six(vals))


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
