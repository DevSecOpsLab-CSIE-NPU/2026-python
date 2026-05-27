"""UVA 11461 - Square Numbers.

手打版：只要會整數平方根，就能很快算出區間內有幾個完全平方數。
"""

from __future__ import annotations

import sys
from math import isqrt


def count_square_numbers(left: int, right: int) -> int:
    return isqrt(right) - isqrt(left - 1)


def solve(text: str) -> str:
    result: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        left, right = map(int, line.split())
        if left == 0 and right == 0:
            break

        result.append(str(count_square_numbers(left, right)))

    return "\n".join(result)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()