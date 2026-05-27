import sys


def get_cost(number, base, costs):
    if number == 0:
        return costs[0]

    total = 0
    n = number

    while n > 0:
        digit = n % base
        total += costs[digit]
        n //= base

    return total


def solve(data):
    values = data.split()
    pos = 0

    t = int(values[pos])
    pos += 1

    answer = []

    for case_id in range(1, t + 1):
        costs = []

        for _ in range(36):
            costs.append(int(values[pos]))
            pos += 1

        q = int(values[pos])
        pos += 1

        answer.append(f"Case {case_id}:")

        for _ in range(q):
            number = int(values[pos])
            pos += 1

            best_cost = None
            best_bases = []

            for base in range(2, 37):
                current_cost = get_cost(number, base, costs)

                if best_cost is None or current_cost < best_cost:
                    best_cost = current_cost
                    best_bases = [base]
                elif current_cost == best_cost:
                    best_bases.append(base)

            bases_string = " ".join(str(base) for base in best_bases)
            answer.append(f"Cheapest base(s) for number {number}: {bases_string}")

        if case_id != t:
            answer.append("")

    return "\n".join(answer)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
