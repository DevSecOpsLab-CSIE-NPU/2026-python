from __future__ import annotations

import sys


def calculate_differences(pairs: list[tuple[int, int]]) -> list[int]:
    # This problem is straightforward.
    # For each pair, compute the absolute difference.
    answers: list[int] = []

    for left, right in pairs:
        answers.append(abs(left - right))

    return answers


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    pairs: list[tuple[int, int]] = []

    # There is no test case count, so read the input two numbers at a time.
    index = 0
    while index < len(parts):
        left = int(parts[index])
        right = int(parts[index + 1])
        pairs.append((left, right))
        index += 2

    outputs = calculate_differences(pairs)
    return "\n".join(str(value) for value in outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()