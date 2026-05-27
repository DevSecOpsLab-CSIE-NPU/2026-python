"""UVA 11417 - GCD"""

from __future__ import annotations

import math
import sys


def gcd_sum(n: int) -> int:
    """計算 1 <= i < j <= n 的 gcd(i, j) 總和。"""
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        out.append(str(gcd_sum(n)))
    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
