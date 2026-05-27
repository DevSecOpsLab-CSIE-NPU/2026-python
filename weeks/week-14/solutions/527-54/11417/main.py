import sys


def calculate_cost(number, base, costs):
    if number == 0:
        return costs[0]

    total_cost = 0

    while number > 0:
        digit = number % base
        total_cost += costs[digit]
        number //= base

    return total_cost


def find_cheapest_bases(number, costs):
    min_cost = None
    cheapest = []

    for base in range(2, 37):
        cost = calculate_cost(number, base, costs)

        if min_cost is None or cost < min_cost:
            min_cost = cost
            cheapest = [base]
        elif cost == min_cost:
            cheapest.append(base)

    return cheapest


def solve(data):
    tokens = data.split()
    idx = 0

    test_cases = int(tokens[idx])
    idx += 1

    output = []

    for case_num in range(1, test_cases + 1):
        costs = list(map(int, tokens[idx:idx + 36]))
        idx += 36

        query_count = int(tokens[idx])
        idx += 1

        output.append(f"Case {case_num}:")

        for _ in range(query_count):
            number = int(tokens[idx])
            idx += 1

            bases = find_cheapest_bases(number, costs)
            bases_text = " ".join(map(str, bases))
            output.append(f"Cheapest base(s) for number {number}: {bases_text}")

        if case_num != test_cases:
            output.append("")

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
