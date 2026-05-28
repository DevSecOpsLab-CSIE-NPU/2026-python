"""UVA 11005 Cheapest Base - easy 版。

寫法盡量簡單：
1. 直接把每個十進位數字轉成各進位表示。
2. 一邊轉換，一邊加總印刷成本。
3. 找出成本最小的進位制。
"""

from __future__ import annotations

import sys


def calc_cost(number: int, base: int, costs: list[int]) -> int:
    """計算 number 在 base 進位下的印刷成本。"""
    if number == 0:
        return costs[0]

    total = 0
    while number > 0:
        number, digit = divmod(number, base)
        total += costs[digit]
    return total


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    test_cases = data[0]
    index = 1
    output: list[str] = []

    for case_number in range(1, test_cases + 1):
        costs = data[index : index + 36]
        index += 36

        query_count = data[index]
        index += 1

        output.append(f"Case {case_number}:")

        for _ in range(query_count):
            number = data[index]
            index += 1

            best_cost = None
            best_bases: list[int] = []

            for base in range(2, 37):
                current_cost = calc_cost(number, base, costs)
                if best_cost is None or current_cost < best_cost:
                    best_cost = current_cost
                    best_bases = [base]
                elif current_cost == best_cost:
                    best_bases.append(base)

            output.append(
                f"Cheapest base(s) for number {number}: "
                + " ".join(str(base) for base in best_bases)
            )

        if case_number != test_cases:
            output.append("")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()