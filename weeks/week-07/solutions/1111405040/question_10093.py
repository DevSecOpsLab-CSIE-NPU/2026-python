"""
UVA 10093: An Easy Problem!
"""

from __future__ import annotations

import sys


def char_value(char: str) -> int:
    """將題目中的字元轉成 0 到 61 的數值。"""
    if "0" <= char <= "9":
        return ord(char) - ord("0")
    if "A" <= char <= "Z":
        return ord(char) - ord("A") + 10
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 36
    raise ValueError(f"不支援的字元: {char}")


def extract_digits(token: str) -> list[int] | None:
    """取出符號後的數字值；若有非法字元則回傳 None。"""
    digits: list[int] = []

    for char in token.strip():
        if char in "+-":
            continue
        if char.isspace():
            continue
        if char.isdigit() or char.isalpha():
            digits.append(char_value(char))
            continue
        return None

    return digits


def minimal_base(token: str) -> int | None:
    """找出最小可行進位，找不到則回傳 None。"""
    digits = extract_digits(token)
    if digits is None or not digits:
        return None

    lowest_base = max(max(digits) + 1, 2)
    digit_sum = sum(digits)

    for base in range(lowest_base, 63):
        if digit_sum % (base - 1) == 0:
            return base

    return None


def solve(text: str) -> str:
    """逐行處理輸入，輸出最小進位或無解訊息。"""
    answers: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        base = minimal_base(line)
        if base is None:
            answers.append("such number is impossible!")
        else:
            answers.append(str(base))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
