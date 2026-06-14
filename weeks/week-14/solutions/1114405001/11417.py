"""UVA 11417 - GCD.

題目要計算 1 <= i < j <= N 時，所有 gcd(i, j) 的總和。
N 只有 500 以內，所以直接枚舉就能穩定通過。
"""

from __future__ import annotations

import math
import sys
from typing import Iterable


def sum_of_gcd(n: int) -> int:
    """回傳 1 <= i < j <= n 的 gcd 總和。"""

    total = 0
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            total += math.gcd(left, right)
    return total


def solve(lines: Iterable[str]) -> list[str]:
    answers: list[str] = []
    for token in " ".join(line.strip() for line in lines).split():
        n = int(token)
        if n == 0:
            break
        answers.append(str(sum_of_gcd(n)))
    return answers


def main() -> None:
    output = solve(sys.stdin)
    sys.stdout.write("\n".join(output))
    if output:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()