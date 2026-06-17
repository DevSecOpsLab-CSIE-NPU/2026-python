import sys

def solve():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    idx = 1
    out = []
    for case in range(1, t + 1):
        costs = []
        for _ in range(4):
            costs.extend(map(int, data[idx].split()))
            idx += 1
        q = int(data[idx])
        idx += 1
        out.append(f"Case {case}:")
        for _ in range(q):
            n = int(data[idx])
            idx += 1
            best = []
            best_cost = float('inf')
            for base in range(2, 37):
                temp, total = n, 0
                if temp == 0:
                    total = costs[0]
                while temp > 0:
                    total += costs[temp % base]
                    temp //= base
                if total < best_cost:
                    best_cost = total
                    best = [base]
                elif total == best_cost:
                    best.append(base)
            out.append(f"Cheapest base(s) for number {n}: " + " ".join(map(str, best)))
        if case < t:
            out.append("")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()