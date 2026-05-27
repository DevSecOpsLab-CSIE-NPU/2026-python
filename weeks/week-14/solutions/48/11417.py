"""UVA 11417 - GCD.

這個版本把計算流程拆成兩層，方便看清楚每一組數字的累加。
"""

from __future__ import annotations

import sys
from math import gcd


def sum_gcd_pairs(limit: int) -> int:
    """計算所有 1 <= i < j <= limit 的 gcd 總和。"""

    total = 0
    for first in range(1, limit):
        for second in range(first + 1, limit + 1):
            total += gcd(first, second)
    return total


def solve(text: str) -> str:
    """逐行讀入 N，遇到 0 就停止。"""

    answers: list[str] = []
    for raw_line in text.splitlines():
        raw_line = raw_line.strip()
        if not raw_line:
            continue

        limit = int(raw_line)
        if limit == 0:
            break

        answers.append(str(sum_gcd_pairs(limit)))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()