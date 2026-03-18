"""HAND EASY - QUESTION 10038"""

from __future__ import annotations

import sys


def check_jolly(sequence: list[int]) -> bool:
    n = len(sequence)
    if n <= 1:
        return True

    seen = [False] * n

    for index in range(1, n):
        diff = abs(sequence[index] - sequence[index - 1])
        if diff < 1 or diff >= n or seen[diff]:
            return False
        seen[diff] = True

    for diff in range(1, n):
        if not seen[diff]:
            return False

    return True


def solve(text: str) -> str:
    answers = []

    for line in text.splitlines():
        if not line.strip():
            continue

        data = list(map(int, line.split()))
        n = data[0]
        sequence = data[1 : 1 + n]
        answers.append("Jolly" if check_jolly(sequence) else "Not jolly")

    return "\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
