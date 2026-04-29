from __future__ import annotations

from bisect import bisect_left
import sys


MAX_TRIALS = 63
MAX_BALLS = 100
LIMIT = 10**19


def precompute() -> list[list[int]]:
    table = [[0] * (MAX_BALLS + 1) for _ in range(MAX_TRIALS + 1)]
    for trials in range(1, MAX_TRIALS + 1):
        for balls in range(1, MAX_BALLS + 1):
            value = table[trials - 1][balls - 1] + 1 + table[trials - 1][balls]
            table[trials][balls] = value if value < LIMIT else LIMIT
    return table


TABLE = precompute()


def minimum_trials(balls: int, floors: int) -> str:
    column = [TABLE[trials][balls] for trials in range(MAX_TRIALS + 1)]
    index = bisect_left(column, floors)
    if index <= MAX_TRIALS:
        return str(index)
    return "More than 63 trials needed."


def solve(data: str) -> str:
    tokens = data.split()
    pointer = 0
    outputs: list[str] = []

    while pointer + 1 < len(tokens):
        balls = int(tokens[pointer])
        floors = int(tokens[pointer + 1])
        pointer += 2
        if balls == 0:
            break
        outputs.append(minimum_trials(min(balls, MAX_BALLS), floors))

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()