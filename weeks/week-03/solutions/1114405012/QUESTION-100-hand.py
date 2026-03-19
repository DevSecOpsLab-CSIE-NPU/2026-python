#!/usr/bin/env python3
"""UVA 100 手打版。

輸入多組 i, j，輸出 i j 與區間內最大的 cycle length。
"""

import sys


def cycle_length(n: int, memo: dict[int, int]) -> int:
    """計算單一數字的 cycle length，使用快取避免重複計算。"""
    original = n
    path: list[int] = []

    while n not in memo:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    length = memo[n]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[original]


def main() -> None:
    memo = {1: 1}
    result: list[str] = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        i, j = map(int, line.split())
        left = min(i, j)
        right = max(i, j)

        best = 0
        for value in range(left, right + 1):
            now = cycle_length(value, memo)
            if now > best:
                best = now

        result.append(f"{i} {j} {best}")

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    main()
