"""UVA 10812 — Beat the Spread! 的手打版。

這份版本保留明確的變數名稱與逐步判斷，
看起來比較像人工一步一步寫出來的程式。
"""

from __future__ import annotations

import sys


def main() -> None:
    """主程式：依序讀取每組資料，算出兩隊分數。"""

    tokens = sys.stdin.read().split()
    if not tokens:
        return

    test_case_count = int(tokens[0])
    current_index = 1
    results: list[str] = []

    for _ in range(test_case_count):
        total_score = int(tokens[current_index])
        score_difference = int(tokens[current_index + 1])
        current_index += 2

        # 先處理最明顯的不合法狀況：總和小於差值。
        if total_score < score_difference:
            results.append("impossible")
            continue

        # 由公式推回高分：high = (S + D) / 2。
        sum_plus_diff = total_score + score_difference
        if sum_plus_diff % 2 != 0:
            results.append("impossible")
            continue

        higher_score = sum_plus_diff // 2
        lower_score = total_score - higher_score

        # 題目要求不能出現負分，所以這裡再做一次保護。
        if lower_score < 0:
            results.append("impossible")
            continue

        results.append(f"{higher_score} {lower_score}")

    sys.stdout.write("\n".join(results))
    if results:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
