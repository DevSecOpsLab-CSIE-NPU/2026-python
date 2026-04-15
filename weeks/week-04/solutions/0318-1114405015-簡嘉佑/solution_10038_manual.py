"""
UVA 10038 - Jolly Jumpers (manual version)

Problem summary:
  For a sequence of length n, it is Jolly if the set of absolute
  differences between consecutive numbers is exactly {1, 2, ..., n-1}.
"""

from __future__ import annotations

import sys


def is_jolly_sequence(nums: list[int]) -> bool:
    n = len(nums)
    if n <= 1:
        return True

    diffs: set[int] = set()
    for i in range(n - 1):
        d = abs(nums[i] - nums[i + 1])
        if d < 1 or d > n - 1:
            return False
        diffs.add(d)

    return diffs == set(range(1, n))


def judge_line(n: int, nums: list[int]) -> str:
    if n != len(nums):
        return "Not jolly"
    return "Jolly" if is_jolly_sequence(nums) else "Not jolly"


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        values = list(map(int, line.split()))
        n = values[0]
        nums = values[1:]
        print(judge_line(n, nums))


if __name__ == "__main__":
    main()
