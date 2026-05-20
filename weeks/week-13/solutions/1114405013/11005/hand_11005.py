import sys

def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]

    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total

def solve(text):
    arr = text.split()
    p = 0

    t = int(arr[p])
    p += 1

    out = []

    for case_id in range(1, t + 1):
        costs = list(map(int, arr[p : p + 36]))
        p += 36

        q = int(arr[p])
        p += 1

        out.append(f"Case {case_id}:")

        for _ in range(q):
            n = int(arr[p])
            p += 1

            best_cost = None
            best_bases = []

            for base in range(2, 37):
                c = cost_in_base(n, base, costs)

                if best_cost is None or c < best_cost:
                    best_cost = c
                    best_bases = [base]
                elif c == best_cost:
                    best_bases.append(base)

            out.append(
                f"Cheapest base(s) for number {n}: {' '.join(map(str, best_bases))}"
            )

        if case_id != t:
            out.append("")

    return "\n".join(out)

def main():
    print(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()