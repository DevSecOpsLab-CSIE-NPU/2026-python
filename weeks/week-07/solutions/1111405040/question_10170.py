"""
UVA 10170: The Hotel with Infinite Rooms
"""

from __future__ import annotations

import sys


def total_days(start_group: int, end_group: int) -> int:
    """計算從 start_group 住到 end_group 的總天數。"""
    count = end_group - start_group + 1
    return count * (start_group + end_group) // 2


def staying_group_size(start_group: int, target_day: int) -> int:
    """找出第 target_day 天住的是多少人的旅行團。"""
    low = start_group
    high = start_group

    while total_days(start_group, high) < target_day:
        high *= 2

    while low < high:
        middle = (low + high) // 2
        if total_days(start_group, middle) >= target_day:
            high = middle
        else:
            low = middle + 1

    return low


def solve(text: str) -> str:
    """處理多筆查詢直到 EOF。"""
    answers: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        start_group, target_day = map(int, line.split())
        answers.append(str(staying_group_size(start_group, target_day)))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
