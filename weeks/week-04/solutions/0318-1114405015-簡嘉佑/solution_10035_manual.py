"""
UVA 10035 - Primary Arithmetic (manual version)

Problem summary:
  Given two non-negative integers, count how many carry operations happen
  when adding them in decimal form.

Output format:
  0 carry  -> "No carry operation."
  1 carry  -> "1 carry operation."
  N carries -> "N carry operations."
"""

from __future__ import annotations

import sys


def count_carries(a: int, b: int) -> int:
    carries = 0
    carry = 0

    while a > 0 or b > 0:
        total = (a % 10) + (b % 10) + carry
        carry = 1 if total >= 10 else 0
        if carry:
            carries += 1
        a //= 10
        b //= 10

    return carries


def format_result(carries: int) -> str:
    if carries == 0:
        return "No carry operation."
    if carries == 1:
        return "1 carry operation."
    return f"{carries} carry operations."


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        print(format_result(count_carries(a, b)))


if __name__ == "__main__":
    main()
