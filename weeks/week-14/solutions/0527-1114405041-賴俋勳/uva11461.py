"""UVA 11461 - Square Numbers"""

from __future__ import annotations

import math
import sys


def count_squares(a: int, b: int) -> int:
    """計算區間 [a, b] 內完全平方數個數。"""
    return math.isqrt(b) - math.isqrt(a - 1)


def solve(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        out.append(str(count_squares(a, b)))
    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
