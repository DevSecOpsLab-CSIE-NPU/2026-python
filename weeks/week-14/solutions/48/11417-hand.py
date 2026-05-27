"""UVA 11417 - GCD.

手打版：直接用雙迴圈加總 gcd，寫法比較像考場上會打的樣子。
"""

from __future__ import annotations

import sys
from math import gcd


def sum_gcd_pairs(n: int) -> int:
    total = 0

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)

    return total


def solve(text: str) -> str:
    result: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        n = int(line)
        if n == 0:
            break

        result.append(str(sum_gcd_pairs(n)))

    return "\n".join(result)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()