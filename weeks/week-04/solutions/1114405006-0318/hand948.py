from __future__ import annotations

import sys


def judge(diff: int) -> str:
    if diff < 0:
        return "<"
    if diff > 0:
        return ">"
    return "="


def check(coin: int, weight: int, records: list[tuple[list[int], list[int], str]]) -> bool:
    for left, right, result in records:
        diff = 0
        if coin in left:
            diff += weight
        if coin in right:
            diff -= weight
        if judge(diff) != result:
            return False
    return True


def solve(data: str) -> str:
    tokens = data.split()
    pos = 0
    t = int(tokens[pos])
    pos += 1
    answers = []

    for _ in range(t):
        n = int(tokens[pos])
        k = int(tokens[pos + 1])
        pos += 2

        records = []
        for _ in range(k):
            cnt = int(tokens[pos])
            pos += 1
            left = list(map(int, tokens[pos : pos + cnt]))
            pos += cnt
            right = list(map(int, tokens[pos : pos + cnt]))
            pos += cnt
            result = tokens[pos]
            pos += 1
            records.append((left, right, result))

        candidates = []
        for coin in range(1, n + 1):
            if check(coin, 1, records) or check(coin, -1, records):
                candidates.append(coin)

        answers.append(str(candidates[0] if len(candidates) == 1 else 0))

    return "\n\n".join(answers) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()