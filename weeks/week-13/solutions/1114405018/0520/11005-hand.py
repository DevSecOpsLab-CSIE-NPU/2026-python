from  __future__ import annotations

import sys

def clac_cost(number: int, base: int, costs: list[int]) -> int:
    
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
                current_cost = clac_cost(number, base, costs)
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

    sys.stdout.write("\n".join(output) + "\n")
    