from __future__ import annotations

import sys


def calculate_differences(pairs: list[tuple[int, int]]) -> list[int]:
    # 每一行只要輸出兩個數字的絕對差即可。
    return [abs(left - right) for left, right in pairs]


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    pairs: list[tuple[int, int]] = []
    for index in range(0, len(tokens), 2):
        left = int(tokens[index])
        right = int(tokens[index + 1])
        pairs.append((left, right))

    answers = calculate_differences(pairs)
    return "\n".join(str(answer) for answer in answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()