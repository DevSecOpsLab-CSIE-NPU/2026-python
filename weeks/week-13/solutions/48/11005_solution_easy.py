# 11005 最簡單版本 - 進位成本
# 只需要一個函數：找最便宜進位

def num_to_base(n, b):
    """將數字轉成進位"""
    if n == 0: return [0]
    d = []
    while n: d.append(n % b); n //= b
    return d[::-1]

T = int(input())
for case in range(1, T + 1):
    costs = []
    for _ in range(4): costs.extend(map(int, input().split()))
    
    Q = int(input())
    print(f"Case {case}:")
    
    for _ in range(Q):
        num = int(input())
        best = []
        min_c = float('inf')
        
        for base in range(2, 37):
            cost = sum(costs[d] for d in num_to_base(num, base))
            if cost < min_c: min_c = cost; best = [base]
            elif cost == min_c: best.append(base)
        
        print(f"Cheapest base(s) for number {num}: {' '.join(map(str, best))}")
    
    if case < T: print()
