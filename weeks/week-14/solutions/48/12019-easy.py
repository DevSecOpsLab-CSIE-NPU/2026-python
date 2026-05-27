"""UVA 12019 - Doom's Day Algorithm.

更容易記的寫法：直接把 date() 查出來，再對應英文星期。
"""

from __future__ import annotations

import sys
from datetime import date


WEEKDAY_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def weekday_name(month: int, day: int) -> str:
    return WEEKDAY_NAMES[date(2012, month, day).weekday()]


def solve(text: str) -> str:
    tokens = text.split()
    if not tokens:
        return ""

    test_count = int(tokens[0])
    index = 1
    answers: list[str] = []

    for _ in range(test_count):
        month = int(tokens[index])
        day = int(tokens[index + 1])
        index += 2
        answers.append(weekday_name(month, day))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()