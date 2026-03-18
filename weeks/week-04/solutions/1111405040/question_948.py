"""
UVA 948 - Fibonaccimal Base
"""

from __future__ import annotations

from typing import List


def build_fib_numbers(limit: int) -> List[int]:
    """建立不超過 limit 的 Fibonacci 數列：1, 2, 3, 5, ...。"""
    if limit < 1:
        return [1]

    fib_numbers = [1, 2]
    while fib_numbers[-1] + fib_numbers[-2] <= limit:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers


def fibonaccimal_representation(number: int) -> str:
    """將正整數轉成 Fibonaccimal Base 字串。"""
    fib_numbers = build_fib_numbers(number)
    remaining = number
    digits: List[str] = []
    started = False

    for fib_number in reversed(fib_numbers):
        if fib_number <= remaining:
            digits.append("1")
            remaining -= fib_number
            started = True
        elif started:
            digits.append("0")

    return "".join(digits) if digits else "0"


def solve(text: str) -> str:
    """依題目格式轉換多筆整數。"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    case_count = int(lines[0])
    numbers = [int(value) for value in lines[1 : 1 + case_count]]
    results = [f"{number} = {fibonaccimal_representation(number)} (fib)" for number in numbers]
    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
