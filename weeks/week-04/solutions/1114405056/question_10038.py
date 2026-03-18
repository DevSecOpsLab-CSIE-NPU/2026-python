"""QUESTION-10038 正式版解答。"""

from __future__ import annotations

import sys


def is_jolly(sequence: list[int]) -> bool:
    if len(sequence) <= 1:
        return True

    # 合法的相鄰差值應該剛好涵蓋 1 到 n - 1。
    diffs = {abs(sequence[index] - sequence[index - 1]) for index in range(1, len(sequence))}
    return diffs == set(range(1, len(sequence)))


def solve(text: str) -> str:
    outputs = []

    for line in text.splitlines():
        if not line.strip():
            continue

        numbers = list(map(int, line.split()))
        count = numbers[0]
        sequence = numbers[1 : 1 + count]
        outputs.append("Jolly" if is_jolly(sequence) else "Not jolly")

    return "\n".join(outputs)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
