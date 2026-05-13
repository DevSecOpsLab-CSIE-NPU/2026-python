"""UVA 10929"""

from __future__ import annotations

import sys


def is_multiple_of_11(text: str) -> bool:
    """利用 11 的交錯和判斷倍數。"""

    difference = 0
    for index, char in enumerate(reversed(text)):
        digit = int(char)
        if index % 2 == 0:
            difference += digit
        else:
            difference -= digit
    return difference % 11 == 0


def describe_number(text: str) -> str:
    """回傳題目要求的完整句子。"""

    if is_multiple_of_11(text):
        return f"{text} is a multiple of 11."
    return f"{text} is not a multiple of 11."


def solve() -> None:
    """逐行讀入，遇到 0 即停止。"""

    outputs: list[str] = []
    for line in sys.stdin.read().split():
        if line == "0":
            break
        outputs.append(describe_number(line))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
