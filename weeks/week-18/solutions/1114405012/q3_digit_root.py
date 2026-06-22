"""Week 18 Q3: digit root in an arbitrary base.

For student ID 1114405012, the base parameter is base = 16.
"""

from __future__ import annotations

import sys
from typing import List


BASE = 16


def digit_root(value: int, base: int) -> int:
    """Repeatedly sum digits in the given base until one digit remains."""

    if base < 2:
        raise ValueError("base must be at least 2")
    if value < 0:
        raise ValueError("value must be non-negative")

    while value >= base:
        digit_sum = 0
        while value > 0:
            value, digit = divmod(value, base)
            digit_sum += digit
        value = digit_sum
    return value


def parse_values(tokens: List[str]) -> List[int]:
    return [int(token) for token in tokens]


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    values = parse_values(tokens)
    outputs = [str(digit_root(value, BASE)) for value in values]
    return "\n".join(outputs)


def main() -> None:
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output + "\n")


if __name__ == "__main__":
    main()