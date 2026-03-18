"""HAND EASY - QUESTION 10019"""

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
