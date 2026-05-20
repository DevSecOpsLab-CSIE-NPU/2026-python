import sys
data = list(map(int, sys.stdin.read().split()))
if data:
    num_cases = data[0]
    idx = 1  
    for case_idx in range(1, num_cases + 1):
        if case_idx > 1: print()
        print(f"Case {case_idx}:")
        costs = data[idx : idx + 36]
        num_queries = data[idx + 36]
        idx += 37
        for _ in range(num_queries):
            target = data[idx]
            idx += 1
            ans_costs = []
            for base in range(2, 37):
                cost = 0
                n = target
                while n > 0:
                    cost += costs[n % base]
                    n //= base
                if target == 0: 
                    cost = costs[0]
                ans_costs.append(cost)
            min_c = min(ans_costs)
            cheapest = [str(b) for b in range(2, 37) if ans_costs[b - 2] == min_c]
            print(f"Cheapest base(s) for number {target}: {' '.join(cheapest)}")