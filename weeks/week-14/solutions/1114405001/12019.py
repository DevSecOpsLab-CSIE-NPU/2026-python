"""UVA 12019 - Doom's Day Algorithm.

這題只考 2012 年，所以直接用 Python 標準函式庫的 date 來算最穩。
weekday() 會回傳 Monday=0 ... Sunday=6，對照題目輸出即可。
"""

from __future__ import annotations

from datetime import date
import sys
from typing import Iterable


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
    """回傳 2012 年指定日期的星期名稱。"""

    return WEEKDAY_NAMES[date(2012, month, day).weekday()]


def solve(lines: Iterable[str]) -> list[str]:
    iterator = iter(line.strip() for line in lines if line.strip())
    case_count = int(next(iterator, "0"))
    answers: list[str] = []

    for _ in range(case_count):
        month, day = map(int, next(iterator).split())
        answers.append(weekday_name(month, day))

    return answers


def main() -> None:
    output = solve(sys.stdin)
    sys.stdout.write("\n".join(output))
    if output:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()