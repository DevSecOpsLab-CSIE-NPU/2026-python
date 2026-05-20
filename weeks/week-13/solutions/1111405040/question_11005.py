"""
UVA 11005 Cheapest Base。
"""

from __future__ import annotations


DIGIT_COUNT = 36


def cost_in_base(number: int, base: int, costs: list[int]) -> int:
    """計算數字在指定進位下的印刷成本。"""
    if number == 0:
        return costs[0]

    total = 0
    value = number
    while value > 0:
        total += costs[value % base]
        value //= base
    return total


def cheapest_bases(number: int, costs: list[int]) -> list[int]:
    """找出成本最低的所有進位。"""
    best_cost: int | None = None
    best_bases: list[int] = []

    for base in range(2, DIGIT_COUNT + 1):
        current_cost = cost_in_base(number, base, costs)
        if best_cost is None or current_cost < best_cost:
            best_cost = current_cost
            best_bases = [base]
        elif current_cost == best_cost:
            best_bases.append(base)

    return best_bases


def solve(data: str) -> str:
    """依題目格式處理多組測資。"""
    tokens = data.split()
    if not tokens:
        return ""

    test_cases = int(tokens[0])
    index = 1
    outputs: list[str] = []

    for case_number in range(1, test_cases + 1):
        costs = [int(token) for token in tokens[index:index + DIGIT_COUNT]]
        index += DIGIT_COUNT

        query_count = int(tokens[index])
        index += 1

        lines = [f"Case {case_number}:"]
        for _ in range(query_count):
            number = int(tokens[index])
            index += 1
            bases = cheapest_bases(number, costs)
            base_text = " ".join(str(base) for base in bases)
            lines.append(f"Cheapest base(s) for number {number}: {base_text}")

        outputs.append("\n".join(lines))

    return "\n\n".join(outputs)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
