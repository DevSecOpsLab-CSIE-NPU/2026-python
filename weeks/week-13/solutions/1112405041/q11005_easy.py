# AI 教學版: 2-36 進位成本計算法
import sys
def get_cost(n, base, costs):
    if n == 0: return costs[0]
    t = 0
    while n > 0:
        t += costs[n % base]
        n //= base
    return t
def solve():
    d = sys.stdin.read().split()
    if not d: return
    tc = int(d[0])
    p = 1
    for t in range(1, tc + 1):
        if t > 1: print()
        print(f"Case {t}:")
        costs = list(map(int, d[p:p+36]))
        p += 36
        qn = int(d[p])
        p += 1
        for _ in range(qn):
            n = int(d[p]); p += 1
            mc = float('inf'); bs = []
            for b in range(2, 37):
                c = get_cost(n, b, costs)
                if c < mc: mc = c; bs = [b]
                elif c == mc: bs.append(b)
            print(f"Cheapest base(s) for number {n}: {' '.join(map(str, bs))}")
if __name__ == '__main__': solve()
