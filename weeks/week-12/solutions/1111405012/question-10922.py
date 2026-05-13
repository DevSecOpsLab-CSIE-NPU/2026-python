"""UVA 10922 - 2 the 9s"""

from __future__ import annotations

import sys


def digit_sum(text: str) -> int:
    """計算字串表示的大整數各位數總和。"""

    return sum(int(char) for char in text)


def nine_degree(text: str) -> int | None:
    """回傳 9-degree；若不是 9 的倍數則回傳 None。"""

    current = digit_sum(text)
    if current % 9 != 0:
        return None

    degree = 1
    while current != 9:
        current = digit_sum(str(current))
        degree += 1
    return degree


def describe_number(text: str) -> str:
    """依題目要求格式化單筆答案。"""

    degree = nine_degree(text)
    if degree is None:
        return f"{text} is not a multiple of 9."
    return f"9-degree of {text} is {degree}."


def solve() -> None:
    """逐行讀取輸入，遇到 0 即結束。"""

    outputs: list[str] = []
    for line in sys.stdin.read().split():
        if line == "0":
            break
        outputs.append(describe_number(line))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
