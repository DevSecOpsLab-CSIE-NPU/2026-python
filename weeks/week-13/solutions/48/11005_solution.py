def to_base(n, base):
    """轉換為進位表示"""
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def solve():
    T = int(input())
    for case in range(1, T + 1):
        costs = []
        for _ in range(4):
            costs.extend(map(int, input().split()))
        
        Q = int(input())
        print(f"Case {case}:")
        
        for _ in range(Q):
            num = int(input())
            min_cost = float('inf')
            best_bases = []
            
            for base in range(2, 37):
                digits = to_base(num, base)
                cost = sum(costs[d] for d in digits)
                
                if cost < min_cost:
                    min_cost = cost
                    best_bases = [base]
                elif cost == min_cost:
                    best_bases.append(base)
            
            print(f"Cheapest base(s) for number {num}: {' '.join(map(str, best_bases))}")
        
        if case < T:
            print()

if __name__ == "__main__":
    solve()
