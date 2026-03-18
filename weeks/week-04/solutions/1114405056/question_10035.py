"""QUESTION-10035 正式版解答。"""

from __future__ import annotations

import sys


def count_carries(left: int, right: int) -> int:
    carries = 0
    carry = 0

    while left > 0 or right > 0:
        # 逐位相加，模擬手算直式加法。
        digit_sum = left % 10 + right % 10 + carry
        if digit_sum >= 10:
            carries += 1
            carry = 1
        else:
            carry = 0

        left //= 10
        right //= 10

    return carries


def format_answer(carries: int) -> str:
    if carries == 0:
        return "No carry operation."
    if carries == 1:
        return "1 carry operation."
    return f"{carries} carry operations."


def solve(text: str) -> str:
    outputs = []

    for line in text.splitlines():
        if not line.strip():
            continue

        left, right = map(int, line.split())
        if left == 0 and right == 0:
            break

        outputs.append(format_answer(count_carries(left, right)))

    return "\n".join(outputs)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
