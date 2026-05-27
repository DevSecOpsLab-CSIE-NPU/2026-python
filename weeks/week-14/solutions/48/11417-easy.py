"""UVA 11417 - GCD.

這是更容易背誦的版本：直接用一行總和式寫出來。
"""

from __future__ import annotations

import sys
from math import gcd


def sum_gcd_pairs(limit: int) -> int:
    """用生成式直接把所有 gcd 加總。"""

    return sum(gcd(first, second) for first in range(1, limit) for second in range(first + 1, limit + 1))


def solve(text: str) -> str:
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