from __future__ import annotations

import sys


def _count_carries(a: int, b: int) -> int:
    """逐位相加，回傳加法過程中的進位次數。"""
    carry = 0
    carry_count = 0

    while a > 0 or b > 0:
        digit_sum = (a % 10) + (b % 10) + carry
        if digit_sum >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

        a //= 10
        b //= 10

    return carry_count


def solve(data: str) -> str:
    """
    UVA 10035 - Primary Arithmetic
    讀取多筆 (a, b)，遇到 0 0 結束。
    """
    tokens = data.split()
    result_lines: list[str] = []

    for i in range(0, len(tokens) - 1, 2):
        a = int(tokens[i])
        b = int(tokens[i + 1])

        if a == 0 and b == 0:
            break

        carry_count = _count_carries(a, b)

        if carry_count == 0:
            result_lines.append("No carry operation.")
        elif carry_count == 1:
            result_lines.append("1 carry operation.")
        else:
            result_lines.append(f"{carry_count} carry operations.")

    return "\n".join(result_lines)


def main() -> None:
    raw_input = sys.stdin.read()
    sys.stdout.write(solve(raw_input))


if __name__ == "__main__":
    main()
