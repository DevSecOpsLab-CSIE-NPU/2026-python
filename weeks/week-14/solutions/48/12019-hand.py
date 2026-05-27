"""UVA 12019 - Doom's Day Algorithm.

手打版：2012 年的日期直接交給 Python `date`，再把星期轉成英文。
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
    weekday_index = date(2012, month, day).weekday()
    return WEEKDAY_NAMES[weekday_index]


def solve(text: str) -> str:
    tokens = text.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    index = 1
    result: list[str] = []

    for _ in range(t):
        month = int(tokens[index])
        day = int(tokens[index + 1])
        index += 2
        result.append(weekday_name(month, day))

    return "\n".join(result)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()