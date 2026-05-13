from __future__ import annotations

import sys


def digit_sum(text):
    return sum(int(char) for char in text)


def nine_degree(text):
    current = digit_sum(text)
    if current % 9 != 0:
        return None
    degree = 1
    while current != 9:
        current = digit_sum(str(current))
        degree += 1
    return degree


def describe_number(text):
    degree = nine_degree(text)
    if degree is None:
        return f"{text} is not a multiple of 9."
    return f"9-degree of {text} is {degree}."


def solve():
    outputs = []
    for text in sys.stdin.read().split():
        if text == "0":
            break
        outputs.append(describe_number(text))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
