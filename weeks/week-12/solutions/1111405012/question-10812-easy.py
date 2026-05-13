"""UVA 10812 - Beat the Spread!（簡單版）"""

from __future__ import annotations

import sys


def solve_case(total_score: int, score_diff: int) -> tuple[int, int] | None:
    """用很直覺的方式推回兩隊比分。"""

    # 先檢查是否有基本上不可能的情況。
    if total_score < score_diff:
        return None

    # 若總和加上分差是奇數，分數無法拆成整數。
    if (total_score + score_diff) % 2 != 0:
        return None

    bigger_score = (total_score + score_diff) // 2
    smaller_score = total_score - bigger_score

    # 小分不能是負數。
    if smaller_score < 0:
        return None

    return bigger_score, smaller_score


def format_result(result: tuple[int, int] | None) -> str:
    """把結果轉成題目要求的文字。"""

    if result is None:
        return "impossible"

    bigger_score, smaller_score = result
    return f"{bigger_score} {smaller_score}"


def solve() -> None:
    """處理多筆測資並輸出答案。"""

    data = sys.stdin.read().split()
    if not data:
        return

    case_count = int(data[0])
    outputs: list[str] = []
    pointer = 1

    for _ in range(case_count):
        total_score = int(data[pointer])
        score_diff = int(data[pointer + 1])
        pointer += 2
        outputs.append(format_result(solve_case(total_score, score_diff)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
