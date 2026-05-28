"""UVA 11005 Cheapest Base

這支程式會讀入 36 個字元的印刷成本，
再針對每個查詢數字找出成本最低的進位制。
"""

from __future__ import annotations

import sys


def to_digits(number: int, base: int) -> list[int]:
    """把十進位整數轉成指定進位的數字列表。"""
    if number == 0:
        return [0]

    digits: list[int] = []
    while number > 0:
        number, remainder = divmod(number, base)
        digits.append(remainder)

    digits.reverse()
    return digits


def total_cost(number: int, base: int, costs: list[int]) -> int:
    """計算某個數字在指定進位下的總印刷成本。"""
    return sum(costs[digit] for digit in to_digits(number, base))


def cheapest_bases(number: int, costs: list[int]) -> list[int]:
    """找出印刷該數字時成本最低的所有進位制。"""
    best_cost = None
    best_bases: list[int] = []

    for base in range(2, 37):
        current_cost = total_cost(number, base, costs)
        if best_cost is None or current_cost < best_cost:
            best_cost = current_cost
            best_bases = [base]
        elif current_cost == best_cost:
            best_bases.append(base)

    return best_bases


def solve() -> None:
    """主流程：讀入資料並輸出答案。"""
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    values = list(map(int, data))
    index = 0
    test_cases = values[index]
    index += 1

    answers: list[str] = []

    for case_number in range(1, test_cases + 1):
        costs = values[index : index + 36]
        index += 36

        query_count = values[index]
        index += 1

        answers.append(f"Case {case_number}:")

        for _ in range(query_count):
            number = values[index]
            index += 1

            bases = cheapest_bases(number, costs)
            bases_text = " ".join(str(base) for base in bases)
            answers.append(f"Cheapest base(s) for number {number}: {bases_text}")

        if case_number != test_cases:
            answers.append("")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()