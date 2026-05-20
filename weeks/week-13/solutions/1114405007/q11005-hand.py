import sys


def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]

    total = 0
    while n > 0:
        n, d = divmod(n, base)
        total += costs[d]
    return total


def solve(text):
    arr = text.split()
    if not arr:
        return ""

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

            best = 10**18
            ans = []

            for base in range(2, 37):
                c = cost_in_base(n, base, costs)
                if c < best:
                    best = c
                    ans = [base]
                elif c == best:
                    ans.append(base)

            out.append(
                f"Cheapest base(s) for number {n}: " + " ".join(map(str, ans))
            )

        if case_id != t:
            out.append("")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
