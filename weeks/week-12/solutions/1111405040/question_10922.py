"""
UVA 10922 - 2 the 9s
"""

from __future__ import annotations

import sys


def digit_sum(number: str) -> int:
    """計算字串數字的各位數字總和。"""
    return sum(int(char) for char in number)


def nine_degree(number: str) -> int | None:
    """回傳 9-degree；若不是 9 的倍數則回傳 None。"""
    first_sum = digit_sum(number)
    if first_sum % 9 != 0:
        return None

    degree = 1
    current = first_sum
    while current != 9:
        current = digit_sum(str(current))
        degree += 1
    return degree


def describe_number(number: str) -> str:
    """依題目要求組出結果字串。"""
    degree = nine_degree(number)
    if degree is None:
        return f"{number} is not a multiple of 9."
    return f"{number} is a multiple of 9 and has 9-degree {degree}."


def solve(data: str) -> str:
    """逐行處理直到遇到 0 為止。"""
    outputs: list[str] = []
    for raw_line in data.splitlines():
        number = raw_line.strip()
        if not number or number == "0":
            if number == "0":
                break
            continue
        outputs.append(describe_number(number))
    return "\n".join(outputs)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
