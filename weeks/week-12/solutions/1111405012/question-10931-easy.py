"""UVA 10931（簡單版）"""

from __future__ import annotations

import sys


def format_binary_parity(number):
    binary_text = format(number, "b")
    return binary_text, binary_text.count("1")


def describe_number(number):
    binary_text, count = format_binary_parity(number)
    return f"The parity of {binary_text} is {count} (mod 2)."


def solve():
    outputs = []
    for token in sys.stdin.read().split():
        number = int(token)
        if number == 0:
            break
        outputs.append(describe_number(number))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
