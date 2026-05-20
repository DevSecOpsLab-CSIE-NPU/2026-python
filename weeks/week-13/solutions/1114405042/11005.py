"""
UVA 11005 - Cheapest Base

題意重點：
給定 0 到 9、A 到 Z 共 36 個字元的印刷成本，
對每個十進位整數 N，枚舉 2 到 36 進位下的表示法成本，
找出成本最低的進位制；若有多個進位制成本相同，全部輸出。

這一版採用「先把數字拆成各進位的每一位，再加總成本」的方式，
程式結構偏清楚，適合搭配 unit test 驗證。
"""

from __future__ import annotations

import sys
from typing import Iterable


def digit_costs_for_base(number: int, base: int, costs: list[int]) -> int:
    """計算 number 在指定 base 下的印刷總成本。

    這裡使用重複除法：
    - 每次取出最低位數字 number % base
    - 加上該位數字對應的印刷成本
    - 再把 number //= base 繼續處理

    特別注意 number = 0 的情況：
    0 在任何進位制下都只會印出一個字元 0，所以成本就是 costs[0]。
    """

    if number == 0:
        return costs[0]

    total = 0
    current = number
    while current > 0:
        digit = current % base
        total += costs[digit]
        current //= base
    return total


def cheapest_bases(number: int, costs: list[int]) -> list[int]:
    """回傳使 number 成本最低的所有進位制（由小到大）。"""

    best_cost = None
    best_bases: list[int] = []

    for base in range(2, 37):
        current_cost = digit_costs_for_base(number, base, costs)
        if best_cost is None or current_cost < best_cost:
            best_cost = current_cost
            best_bases = [base]
        elif current_cost == best_cost:
            best_bases.append(base)

    return best_bases


def solve(tokens: Iterable[str]) -> str:
    """依照題目格式處理所有測資，並回傳完整輸出字串。"""

    iterator = iter(tokens)
    case_count = int(next(iterator))
    output_lines: list[str] = []

    for case_index in range(1, case_count + 1):
        # 題目固定給 36 個成本值，依序對應 0-9 與 A-Z。
        costs = [int(next(iterator)) for _ in range(36)]
        query_count = int(next(iterator))

        output_lines.append(f"Case {case_index}:")
        for _ in range(query_count):
            number = int(next(iterator))
            bases = cheapest_bases(number, costs)
            bases_text = " ".join(map(str, bases))
            output_lines.append(
                f"Cheapest base(s) for number {number}: {bases_text}"
            )

        if case_index != case_count:
            output_lines.append("")

    return "\n".join(output_lines)


def main() -> None:
    """程式進入點：讀入標準輸入、計算答案、輸出結果。"""

    data = sys.stdin.buffer.read().split()
    if not data:
        return
    sys.stdout.write(solve(token.decode() for token in data))


if __name__ == "__main__":
    main()