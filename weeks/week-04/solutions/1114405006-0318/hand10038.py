from __future__ import annotations

import sys


def is_jolly(seq: list[int]) -> bool:
    n = len(seq)
    if n <= 1:
        return True

    diffs = set()
    for i in range(1, n):
        diffs.add(abs(seq[i] - seq[i - 1]))

    return diffs == set(range(1, n))


def solve(data: str) -> str:
    answers = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1 : 1 + n]
        answers.append("Jolly" if is_jolly(seq) else "Not jolly")

    if not answers:
        return ""

    return "\n".join(answers) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()