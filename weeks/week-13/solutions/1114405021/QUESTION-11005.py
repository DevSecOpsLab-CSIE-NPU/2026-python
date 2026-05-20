"""UVA 11005 - Cheapest Base"""

from __future__ import annotations

import sys


def digits_cost(number: int, base: int, costs: list[int]) -> int:
    if number == 0:
        return costs[0]

    total = 0
    while number > 0:
        total += costs[number % base]
        number //= base
    return total


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    case_count = data[0]
    index = 1
    answers: list[str] = []

    for case_id in range(1, case_count + 1):
        costs = data[index:index + 36]
        index += 36
        query_count = data[index]
        index += 1

        if case_id > 1:
            answers.append("")
        answers.append(f"Case {case_id}:")

        for _ in range(query_count):
            number = data[index]
            index += 1

            best_cost = None
            best_bases: list[str] = []

            for base in range(2, 37):
                cost = digits_cost(number, base, costs)
                if best_cost is None or cost < best_cost:
                    best_cost = cost
                    best_bases = [str(base)]
                elif cost == best_cost:
                    best_bases.append(str(base))

            answers.append(
                f"Cheapest base(s) for number {number}: {' '.join(best_bases)}"
            )

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()