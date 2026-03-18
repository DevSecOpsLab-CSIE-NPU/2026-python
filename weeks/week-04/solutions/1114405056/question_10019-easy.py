"""QUESTION-10019 easy 版。

這題沒有陷阱，每讀到一行兩個整數，
就直接算 `abs(a - b)`。
由於題目可能一路讀到 EOF，所以用逐行處理最自然。
"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    answer = []

    for line in text.splitlines():
        if not line.strip():
            continue

        a, b = map(int, line.split())
        answer.append(str(abs(a - b)))

    return "\n".join(answer)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
