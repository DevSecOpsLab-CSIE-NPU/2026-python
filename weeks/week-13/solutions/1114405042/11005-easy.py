"""
UVA 11005 - Cheapest Base（easy 版本）

這一版刻意把流程寫得更直覺：
1. 讀入所有成本
2. 對每個查詢數字，從 base 2 一路試到 base 36
3. 算出每個 base 的成本
4. 保留最低成本的 base 全部輸出

如果要在考試現場快速重現，這種寫法比較好記：
「先枚舉進位，再把數字拆位相加」。
"""

from __future__ import annotations

import sys


def calc_cost(number: int, base: int, costs: list[int]) -> int:
    """計算某個十進位數字在指定進位下的印刷成本。"""

    # 0 的表示法固定就是一個 0，所以直接回傳成本即可。
    if number == 0:
        return costs[0]

    total = 0
    while number > 0:
        remainder = number % base
        total += costs[remainder]
        number //= base
    return total


def find_best_bases(number: int, costs: list[int]) -> list[int]:
    """找出所有最低成本的進位制，結果依照題意由小到大排列。"""

    best_cost = None
    answers: list[int] = []

    for base in range(2, 37):
        current_cost = calc_cost(number, base, costs)
        if best_cost is None or current_cost < best_cost:
            best_cost = current_cost
            answers = [base]
        elif current_cost == best_cost:
            answers.append(base)

    return answers


def main() -> None:
    """讀入題目格式並輸出標準答案。"""

    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    index = 0
    case_count = int(tokens[index])
    index += 1
    output_lines: list[str] = []

    for case_no in range(1, case_count + 1):
        # 題目每組固定給 36 個成本值，順序是 0-9、A-Z。
        costs = [int(tokens[index + i]) for i in range(36)]
        index += 36

        query_count = int(tokens[index])
        index += 1

        output_lines.append(f"Case {case_no}:")
        for _ in range(query_count):
            number = int(tokens[index])
            index += 1
            best_bases = find_best_bases(number, costs)
            output_lines.append(
                f"Cheapest base(s) for number {number}: {' '.join(map(str, best_bases))}"
            )

        if case_no != case_count:
            output_lines.append("")

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()