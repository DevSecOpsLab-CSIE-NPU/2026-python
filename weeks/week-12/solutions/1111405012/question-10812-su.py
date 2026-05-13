from __future__ import annotations

import sys


def solve_case(total_score: int, score_diff: int):
    if total_score < score_diff:
        return None
    if (total_score + score_diff) % 2:
        return None
    high_score = (total_score + score_diff) // 2
    low_score = total_score - high_score
    if low_score < 0:
        return None
    return high_score, low_score


def format_result(result):
    if result is None:
        return "impossible"
    return f"{result[0]} {result[1]}"


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    count = int(data[0])
    index = 1
    outputs = []
    for _ in range(count):
        total_score = int(data[index])
        score_diff = int(data[index + 1])
        outputs.append(format_result(solve_case(total_score, score_diff)))
        index += 2
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
