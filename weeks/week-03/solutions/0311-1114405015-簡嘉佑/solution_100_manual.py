"""
UVA 100 - The 3n + 1 Problem (manual version)

Given multiple input pairs i, j, find the maximum Collatz cycle length
within the inclusive range [min(i, j), max(i, j)], and output:
"i j max_cycle" while preserving the original input order for i and j.
"""

from __future__ import annotations

import sys


def cycle_length(n: int, memo: dict[int, int]) -> int:
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        nxt = n // 2
    else:
        nxt = 3 * n + 1

    memo[n] = 1 + cycle_length(nxt, memo)
    return memo[n]


def max_cycle_length(i: int, j: int) -> int:
    lo = min(i, j)
    hi = max(i, j)

    memo: dict[int, int] = {1: 1}
    best = 0
    for n in range(lo, hi + 1):
        best = max(best, cycle_length(n, memo))
    return best


def format_output_line(i: int, j: int) -> str:
    return f"{i} {j} {max_cycle_length(i, j)}"


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        i, j = map(int, line.split())
        print(format_output_line(i, j))


if __name__ == "__main__":
    main()
