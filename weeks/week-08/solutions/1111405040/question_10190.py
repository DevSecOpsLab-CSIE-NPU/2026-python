"""
UVA 10190: Divide, But Not Quite Conquer!
"""

from __future__ import annotations

import sys


def divide_sequence(number: int, divisor: int) -> list[int] | None:
    """若 number 可連續除以 divisor 到 1，回傳完整序列。"""
    if number <= 1 or divisor <= 1:
        return None

    sequence = [number]

    while number != 1:
        if number % divisor != 0:
            return None

        number //= divisor
        sequence.append(number)

    return sequence


def solve(text: str) -> str:
    """逐行處理 n m，輸出序列或 Boring!。"""
    outputs: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        number, divisor = map(int, line.split())
        sequence = divide_sequence(number, divisor)

        if sequence is None:
            outputs.append("Boring!")
        else:
            outputs.append(" ".join(str(value) for value in sequence))

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
