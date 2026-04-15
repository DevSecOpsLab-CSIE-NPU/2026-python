"""
UVA 299 - Train Swapping (manual version)

For each train arrangement, compute the minimum number of adjacent swaps
needed to sort cars in increasing order.
This equals the inversion count:
number of pairs (i, j) where i < j and a[i] > a[j].
"""

from __future__ import annotations

import sys


def min_adjacent_swaps(train: list[int]) -> int:
    swaps = 0
    n = len(train)

    for i in range(n):
        for j in range(i + 1, n):
            if train[i] > train[j]:
                swaps += 1

    return swaps


def format_output(swaps: int) -> str:
    return f"Optimal train swapping takes {swaps} swaps."


def solve_case(train: list[int]) -> str:
    return format_output(min_adjacent_swaps(train))


def main() -> None:
    first = sys.stdin.readline().strip()
    if not first:
        return

    t = int(first)
    for _ in range(t):
        line = sys.stdin.readline().strip()
        while line == "":
            line = sys.stdin.readline().strip()
        _l = int(line)

        train_line = sys.stdin.readline().strip()
        while train_line == "":
            train_line = sys.stdin.readline().strip()
        train = list(map(int, train_line.split()))

        print(solve_case(train))


if __name__ == "__main__":
    main()
