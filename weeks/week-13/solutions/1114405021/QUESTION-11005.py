#!/usr/bin/env python3
import sys

def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]
    s = 0
    while n > 0:
        s += costs[n % base]
        n //= base
    return s

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    for case in range(1, T+1):
        costs = [int(next(it)) for _ in range(36)]
        q = int(next(it))
        print(f"Case {case}:")
        for _ in range(q):
            n = int(next(it))
            best = None
            bases = []
            for b in range(2, 37):
                c = cost_in_base(n, b, costs)
                if best is None or c < best:
                    best = c
                    bases = [b]
                elif c == best:
                    bases.append(b)
            bases_str = " ".join(str(x) for x in bases)
            print(f"Cheapest base(s) for number {n}: {bases_str}")

if __name__ == '__main__':
    solve()
#!/usr/bin/env python3
import sys

def cheapest_bases(costs, n):
    res = []
    for base in range(2,37):
        x = n
        total = 0
        if x == 0:
            total = costs[0]
        else:
            while x>0:
                d = x % base
                total += costs[d]
                x //= base
        res.append((base, total))
    mincost = min(t for b,t in res)
    return [b for b,t in res if t==mincost]

def main():
    data = sys.stdin.read().strip().split()
    if not data: 
        return
    it = iter(data)
    tc = int(next(it))
    out_lines = []
    for ci in range(1, tc+1):
        costs = [int(next(it)) for _ in range(36)]
        q = int(next(it))
        out_lines.append(f"Case {ci}:")
        for _ in range(q):
            n = int(next(it))
            bases = cheapest_bases(costs, n)
            out_lines.append(f"Cheapest base(s) for number {n}: {' '.join(str(b) for b in bases)}")
        if ci!=tc:
            out_lines.append("")
    print('\n'.join(out_lines))

if __name__=='__main__':
    main()
