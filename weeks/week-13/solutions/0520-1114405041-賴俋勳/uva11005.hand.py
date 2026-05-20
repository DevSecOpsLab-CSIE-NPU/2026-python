import sys


def digit_cost(value: int, base: int, costs: list[int]) -> int:
    if value == 0:
        return costs[0]
    total = 0
    while value > 0:
        value, digit = divmod(value, base)
        total += costs[digit]
    return total


def solve(data: list[int]) -> str:
    index = 0
    case_count = data[index]
    index += 1
    output: list[str] = []

    for case_no in range(1, case_count + 1):
        costs = data[index:index + 36]
        index += 36
        query_count = data[index]
        index += 1

        if case_no > 1:
            output.append("")
        output.append(f"Case {case_no}:")

        for _ in range(query_count):
            number = data[index]
            index += 1
            best_cost = None
            best_bases = []

            for base in range(2, 37):
                cost = digit_cost(number, base, costs)
                if best_cost is None or cost < best_cost:
                    best_cost = cost
                    best_bases = [str(base)]
                elif cost == best_cost:
                    best_bases.append(str(base))

            output.append(f"Cheapest base(s) for number {number}: {' '.join(best_bases)}")

    return "\n".join(output)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()