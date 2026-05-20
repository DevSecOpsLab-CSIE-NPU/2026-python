import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    idx = 0
    cases = int(data[idx])
    idx += 1
    
    for case_num in range(1, cases + 1):
        if case_num > 1: print()
        print(f"Case {case_num}:")
        
        costs = [int(x) for x in data[idx:idx+36]]
        idx += 36
        q_count = int(data[idx])
        idx += 1
        
        for _ in range(q_count):
            num = int(data[idx])
            idx += 1
            
            best_bases = []
            min_cost = float('inf')
            
            for base in range(2, 37):
                temp, cost = num, 0
                if temp == 0:
                    cost = costs[0]
                else:
                    while temp > 0:
                        cost += costs[temp % base]
                        temp //= base
                
                if cost < min_cost:
                    min_cost = cost
                    best_bases = [base]
                elif cost == min_cost:
                    best_bases.append(base)
                    
            print(f"Cheapest base(s) for number {num}: {' '.join(map(str, best_bases))}")

if __name__ == '__main__':
    solve()
