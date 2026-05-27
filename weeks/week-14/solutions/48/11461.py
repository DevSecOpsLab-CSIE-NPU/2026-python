"""UVA 11461 - Square Numbers.

這個版本把區間內平方數的數量拆成兩個整數平方根來算。
"""

from __future__ import annotations

import sys
from math import isqrt


def count_square_numbers(left: int, right: int) -> int:
    """回傳閉區間 [left, right] 裡有幾個完全平方數。"""

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