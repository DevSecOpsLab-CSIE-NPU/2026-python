"""
UVA 11005 - Cheapest Base（easy 版）

想法很單純：
1. 對每個查詢數字，把 2 到 36 進位全部算一次。
2. 把該進位下每一位數字的印刷成本加總。
3. 找出成本最小的所有進位制，依照由小到大輸出。

這題的核心只在「把十進位數字轉成任意進位」，所以可以直接用
除法與取餘數一路拆位數。
"""

import sys


def digit_cost(value: int, base: int, costs: list[int]) -> int:
    """計算 value 在 base 進位下的總印刷成本。"""
    if value == 0:
        return costs[0]

    total = 0
    while value > 0:
        value, digit = divmod(value, base)
        total += costs[digit]
    return total


def solve(data: list[int]) -> str:
    """依題目的輸出格式整理結果。"""
    index = 0
    case_count = data[index]
    index += 1
    output: list[str] = []

    for case_no in range(1, case_count + 1):
        # 每組測資先讀入 36 個字元成本，對應 0~9、A~Z。
        costs = data[index:index + 36]
        index += 36

        query_count = data[index]
        index += 1

        # 多組測資之間要空一行。
        if case_no > 1:
            output.append("")
        output.append(f"Case {case_no}:")

        for _ in range(query_count):
            number = data[index]
            index += 1

            # 逐一試算所有進位，保留最便宜的進位們。
            best_cost = None
            best_bases: list[str] = []
            for base in range(2, 37):
                cost = digit_cost(number, base, costs)
                if best_cost is None or cost < best_cost:
                    best_cost = cost
                    best_bases = [str(base)]
                elif cost == best_cost:
                    best_bases.append(str(base))

            output.append(
                f"Cheapest base(s) for number {number}: {' '.join(best_bases)}"
            )

    return "\n".join(output)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()