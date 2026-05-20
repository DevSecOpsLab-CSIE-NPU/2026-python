"""UVA 11005 - Cheapest Base (easy version with detailed comments)."""

from __future__ import annotations

import sys


def calc_cost(number: int, base: int, cost_table: list[int]) -> int:
    """計算 number 在 base 進位下的印刷成本。"""
    if number == 0:
        return cost_table[0]

    total_cost = 0

    # 只要 number 還沒除完，就持續取出最低位數字。
    while number > 0:
        digit = number % base
        total_cost += cost_table[digit]
        number //= base

    return total_cost


def main() -> None:
    # 題目的輸入全部都是整數，所以直接一次讀進來再切割。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    case_count = data[0]
    pos = 1
    output: list[str] = []

    for case_no in range(1, case_count + 1):
        # 36 個字元成本：0-9、A-Z。
        cost_table = data[pos:pos + 36]
        pos += 36

        # 接下來是查詢數量，後面再接每個查詢的十進位數字。
        query_count = data[pos]
        pos += 1

        if case_no > 1:
            output.append("")
        output.append(f"Case {case_no}:")

        for _ in range(query_count):
            number = data[pos]
            pos += 1

            # 先從最小成本開始比較，再把所有同成本的進位制一起記下來。
            best_cost = None
            best_bases: list[str] = []

            for base in range(2, 37):
                current_cost = calc_cost(number, base, cost_table)
                if best_cost is None or current_cost < best_cost:
                    best_cost = current_cost
                    best_bases = [str(base)]
                elif current_cost == best_cost:
                    best_bases.append(str(base))

            output.append(
                f"Cheapest base(s) for number {number}: {' '.join(best_bases)}"
            )

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()