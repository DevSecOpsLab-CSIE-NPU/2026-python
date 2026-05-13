"""UVA 10812 - Beat the Spread!"""

from __future__ import annotations

import sys


def solve_case(total_score: int, score_diff: int) -> tuple[int, int] | None:
    """根據總分與分差，回傳較大分與較小分。"""

    if total_score < score_diff:
        return None
    if (total_score + score_diff) % 2 != 0:
        return None

    high_score = (total_score + score_diff) // 2
    low_score = total_score - high_score

    if low_score < 0:
        return None
    return high_score, low_score


def format_result(result: tuple[int, int] | None) -> str:
    """將單筆答案轉成輸出字串。"""

    if result is None:
        return "impossible"
    high_score, low_score = result
    return f"{high_score} {low_score}"


def solve() -> None:
    """讀入所有測資並輸出答案。"""

    tokens = sys.stdin.read().split()
    if not tokens:
        return

    case_count = int(tokens[0])
    outputs: list[str] = []
    index = 1

    for _ in range(case_count):
        total_score = int(tokens[index])
        score_diff = int(tokens[index + 1])
        index += 2
        outputs.append(format_result(solve_case(total_score, score_diff)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
