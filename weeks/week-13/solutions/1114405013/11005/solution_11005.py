from __future__ import annotations

import sys
from typing import List


def representation_cost(number: int, base: int, costs: List[int]) -> int:
    """計算 number 在指定進位下的總印刷成本。"""
    # 題目規定 0 也要被印出，因此成本就是字元 0 的成本。
    if number == 0:
        return costs[0]

    total = 0
    value = number

    # 逐位取餘數，餘數就是該位的數字值，直接對應到成本陣列。
    while value > 0:
        digit = value % base
        total += costs[digit]
        value //= base

    return total


def cheapest_bases(number: int, costs: List[int]) -> List[int]:
    """回傳 number 在 2~36 進位中成本最低的所有進位（升序）。"""
    best_cost = None
    best_list: List[int] = []

    for base in range(2, 37):
        current_cost = representation_cost(number, base, costs)

        if best_cost is None or current_cost < best_cost:
            best_cost = current_cost
            best_list = [base]
        elif current_cost == best_cost:
            best_list.append(base)

    return best_list


def format_case_output(number: int, bases: List[int]) -> str:
    """把單一查詢格式化成題目要求的輸出文字。"""
    return f"Cheapest base(s) for number {number}: {' '.join(map(str, bases))}"


def solve(data: str) -> str:
    """讀取整份輸入字串並回傳完整輸出字串。"""
    tokens = data.split()
    idx = 0

    test_cases = int(tokens[idx])
    idx += 1

    lines: List[str] = []

    for case_no in range(1, test_cases + 1):
        # 每組有 36 個成本值，依序對應 0~35（即 0~9, A~Z）。
        costs = list(map(int, tokens[idx : idx + 36]))
        idx += 36

        query_count = int(tokens[idx])
        idx += 1

        lines.append(f"Case {case_no}:")

        for _ in range(query_count):
            number = int(tokens[idx])
            idx += 1

            bases = cheapest_bases(number, costs)
            lines.append(format_case_output(number, bases))

        # 題目要求「測資之間空一行」，也就是 case 與 case 間放空字串。
        if case_no != test_cases:
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
