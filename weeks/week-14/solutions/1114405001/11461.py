"""UVA 11461 - Square Numbers.

用整數平方根 isqrt 直接算區間內有幾個完全平方數：
count = floor(sqrt(b)) - floor(sqrt(a - 1))
"""

from __future__ import annotations

import math
import sys
from typing import Iterable


def count_squares(a: int, b: int) -> int:
    """回傳閉區間 [a, b] 中完全平方數的個數。"""

    if a > b:
        raise ValueError("a must be <= b")
    return math.isqrt(b) - math.isqrt(a - 1)


def solve(lines: Iterable[str]) -> list[str]:
    answers: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        answers.append(str(count_squares(a, b)))
    return answers


def main() -> None:
    output = solve(sys.stdin)
    sys.stdout.write("\n".join(output))
    if output:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()