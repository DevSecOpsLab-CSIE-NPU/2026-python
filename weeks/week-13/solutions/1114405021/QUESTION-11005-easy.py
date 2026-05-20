#!/usr/bin/env python3
# 更簡單且有繁體中文詳細註解的版本
import sys

# 將整數 n 以 base 進位表示，每個數位對應 costs 的花費，回傳總花費
def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]
    s = 0
    while n > 0:
        s += costs[n % base]
        n //= base
    return s

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    for tc in range(1, T+1):
        # 讀入 36 個字元的成本（0-9, A-Z）
        costs = [int(next(it)) for _ in range(36)]
        q = int(next(it))
        print(f"Case {tc}:")
        for _ in range(q):
            n = int(next(it))
            best = None
            best_bases = []
            # 嘗試所有進位 2~36，求出表示成本
            for b in range(2, 37):
                c = cost_in_base(n, b, costs)
                if best is None or c < best:
                    best = c
                    best_bases = [b]
                elif c == best:
                    best_bases.append(b)
            print(f"Cheapest base(s) for number {n}: {' '.join(map(str,best_bases))}")

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# 簡潔易懂版本（附繁體中文註解）
import sys

# 將數字 n 在各進位 2..36 下轉成數位並計算總成本
def cheapest_bases(costs, n):
    results = []
    for base in range(2, 37):
        if n == 0:
            cost = costs[0]
        else:
            cost = 0
            x = n
            while x > 0:
                d = x % base
                cost += costs[d]
                x //= base
        results.append((base, cost))
    # 取最小成本的所有進位
    mincost = min(c for b,c in results)
    return [b for b,c in results if c == mincost]

def main():
    # 從標準輸入讀取所有數字
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return
    it = iter(tokens)
    tc = int(next(it))
    out = []
    for case in range(1, tc+1):
        costs = [int(next(it)) for _ in range(36)]
        q = int(next(it))
        out.append(f"Case {case}:")
        for _ in range(q):
            n = int(next(it))
            bases = cheapest_bases(costs, n)
            out.append(f"Cheapest base(s) for number {n}: {' '.join(map(str,bases))}")
        if case != tc:
            out.append("")
    print('\n'.join(out))

if __name__ == '__main__':
    main()
