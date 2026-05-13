"""UVA 10929（簡單版）"""

from __future__ import annotations

import sys


def is_multiple_of_11(text):
    difference = 0
    for index, char in enumerate(reversed(text)):
        digit = int(char)
        if index % 2 == 0:
            difference += digit
        else:
            difference -= digit
    return difference % 11 == 0


def describe_number(text):
    if is_multiple_of_11(text):
        return f"{text} is a multiple of 11."
    return f"{text} is not a multiple of 11."


def solve():
    outputs = []
    for text in sys.stdin.read().split():
        if text == "0":
            break
        outputs.append(describe_number(text))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
