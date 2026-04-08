"""
UVA 10093: An Easy Problem!（簡單版）
"""

from __future__ import annotations

import sys


def value_of(char: str) -> int:
    """把字元換成題目定義的數值。"""
    if "0" <= char <= "9":
        return ord(char) - 48
    if "A" <= char <= "Z":
        return ord(char) - 55
    return ord(char) - 61


def solve(text: str) -> str:
    """利用數位和判斷最小可行進位。"""
    outputs: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        digits: list[int] = []
        valid = True

        for char in line:
            if char in "+-":
                continue
            if char.isdigit() or char.isalpha():
                digits.append(value_of(char))
            else:
                valid = False
                break

        if not valid or not digits:
            outputs.append("such number is impossible!")
            continue

        start_base = max(max(digits) + 1, 2)
        total = sum(digits)
        answer: str | None = None

        for base in range(start_base, 63):
            if total % (base - 1) == 0:
                answer = str(base)
                break

        outputs.append(answer or "such number is impossible!")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
