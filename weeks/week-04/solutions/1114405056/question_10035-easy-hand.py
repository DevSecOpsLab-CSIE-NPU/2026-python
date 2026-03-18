"""HAND EASY - QUESTION 10035"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    results = []

    for line in text.splitlines():
        if not line.strip():
            continue

        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        carry = 0
        carry_count = 0

        while a > 0 or b > 0:
            total = a % 10 + b % 10 + carry
            if total >= 10:
                carry = 1
                carry_count += 1
            else:
                carry = 0

            a //= 10
            b //= 10

        if carry_count == 0:
            results.append("No carry operation.")
        elif carry_count == 1:
            results.append("1 carry operation.")
        else:
            results.append(f"{carry_count} carry operations.")

    return "\n".join(results)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
