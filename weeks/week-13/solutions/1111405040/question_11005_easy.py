"""
UVA 11005 Cheapest Base 簡單版。
"""

from __future__ import annotations


def base_cost(number: int, base: int, costs: list[int]) -> int:
    """直接用除法把每一位拆出來計算成本。"""
    if number == 0:
        return costs[0]

    total = 0
    while number > 0:
        total += costs[number % base]
        number //= base
    return total


def solve(data: str) -> str:
    """簡單版做法：逐題、逐進位直接比。"""
    tokens = data.split()
    if not tokens:
        return ""

    test_cases = int(tokens[0])
    index = 1
    blocks: list[str] = []

    for case_number in range(1, test_cases + 1):
        costs = [int(token) for token in tokens[index:index + 36]]
        index += 36
        query_count = int(tokens[index])
        index += 1

        lines = [f"Case {case_number}:"]
        for _ in range(query_count):
            number = int(tokens[index])
            index += 1

            best_cost = None
            best_bases: list[int] = []
            for base in range(2, 37):
                current_cost = base_cost(number, base, costs)
                if best_cost is None or current_cost < best_cost:
                    best_cost = current_cost
                    best_bases = [base]
                elif current_cost == best_cost:
                    best_bases.append(base)

            lines.append(
                f"Cheapest base(s) for number {number}: "
                + " ".join(str(base) for base in best_bases)
            )

        blocks.append("\n".join(lines))

    return "\n\n".join(blocks)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
