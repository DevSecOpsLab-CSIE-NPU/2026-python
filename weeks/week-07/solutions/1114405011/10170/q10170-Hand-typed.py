from __future__ import annotations
import math
import sys


def f(s: int, d: int) -> int:
    t = d + (s - 1) * s // 2
    k = (math.isqrt(1 + 8 * t) - 1) // 2
    while k * (k + 1) // 2 < t:
        k += 1
    while k > s and (k - 1) * k // 2 >= t:
        k -= 1
    return k


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        out.append(str(f(s, d)))
    return "\n".join(out)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
