"""UVA 11461 - Square Numbers.

這是更容易記的版本：直接把兩個整數平方根相減。
"""

from __future__ import annotations

import sys
from math import isqrt


def count_square_numbers(left: int, right: int) -> int:
    return isqrt(right) - isqrt(left - 1)


def solve(text: str) -> str:
    answers: list[str] = []
    for raw_line in text.splitlines():
        raw_line = raw_line.strip()
        if not raw_line:
            continue

        left, right = map(int, raw_line.split())
        if left == 0 and right == 0:
            break

        answers.append(str(count_square_numbers(left, right)))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()