"""
UVA 10929 - You can say 11
"""

from __future__ import annotations

import sys


def is_multiple_of_11(number: str) -> bool:
    """用逐位取餘數的方式判斷是否為 11 的倍數。"""
    remainder = 0
    for char in number:
        remainder = (remainder * 10 + int(char)) % 11
    return remainder == 0


def describe_number(number: str) -> str:
    """組出題目要求的輸出文字。"""
    if is_multiple_of_11(number):
        return f"{number} is a multiple of 11."
    return f"{number} is not a multiple of 11."


def solve(data: str) -> str:
    """處理直到遇到 0 為止的多筆輸入。"""
    outputs: list[str] = []
    for raw_line in data.splitlines():
        number = raw_line.strip()
        if not number:
            continue
        if number == "0":
            break
        outputs.append(describe_number(number))
    return "\n".join(outputs)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
