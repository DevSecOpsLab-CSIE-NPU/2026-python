#!/usr/bin/env python3
import sys

def to_costs(n, base, costs):
    if n == 0:
        return costs[0]
    s = 0
    while n:
        s += costs[n % base]
        n //= base
    return s

def solve():
    parts = sys.stdin.read().split()
    if not parts:
        return
    p = 0
    T = int(parts[p]); p+=1
    for case in range(1, T+1):
        costs = list(map(int, parts[p:p+36])); p+=36
        q = int(parts[p]); p+=1
        print(f"Case {case}:")
        for _ in range(q):
            n = int(parts[p]); p+=1
            best = None; bases = []
            for b in range(2,37):
                c = to_costs(n, b, costs)
                if best is None or c < best:
                    best = c; bases = [b]
                elif c == best:
                    bases.append(b)
            print("Cheapest base(s) for number {}: {}".format(n, ' '.join(map(str,bases))))

if __name__ == '__main__':
    solve()
#!/usr/bin/env python3
# 手打版本（風格略有不同）
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    tc = int(data[idx]); idx+=1
    out = []
    for ci in range(1, tc+1):
        costs = list(map(int, data[idx:idx+36])); idx+=36
        q = int(data[idx]); idx+=1
        out.append(f"Case {ci}:")
        for _ in range(q):
            n = int(data[idx]); idx+=1
            best = None
            best_bases = []
            for b in range(2,37):
                x = n
                total = 0
                if x==0:
                    total = costs[0]
                else:
                    while x>0:
                        total += costs[x % b]
                        x //= b
                if best is None or total < best:
                    best = total
                    best_bases = [b]
                elif total == best:
                    best_bases.append(b)
            out.append(f"Cheapest base(s) for number {n}: {' '.join(map(str,best_bases))}")
        if ci!=tc:
            out.append("")
    print('\n'.join(out))

if __name__=='__main__':
    main()
