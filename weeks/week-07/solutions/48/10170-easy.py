"""10170 的好記憶版本。

只要把每一團住的天數加起來，
找出第一個累積天數不小於 D 的團體即可。
"""

from __future__ import annotations

import sys


def solve_one(start: int, day: int) -> int:
    total_days = 0
    people = start

    while total_days < day:
        total_days += people
        if total_days >= day:
            return people
        people += 1

    return people


def solve(text: str) -> str:
    numbers = list(map(int, text.split()))
    if not numbers:
        return ""

    answers = []
    for index in range(0, len(numbers), 2):
        answers.append(str(solve_one(numbers[index], numbers[index + 1])))
    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()