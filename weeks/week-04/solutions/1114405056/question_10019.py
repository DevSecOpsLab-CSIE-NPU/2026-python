"""QUESTION-10019 正式版解答。

依照題目內容，這題實際上是輸入兩個整數，
輸出兩者的絕對差值。
"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    outputs = []

    for line in text.splitlines():
        if not line.strip():
            continue
        left, right = map(int, line.split())
        # 題目只要求正數差值，直接取絕對值即可。
        outputs.append(str(abs(left - right)))

    return "\n".join(outputs)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
