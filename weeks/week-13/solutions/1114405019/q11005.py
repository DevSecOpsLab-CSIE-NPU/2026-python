import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    num_cases = int(input_data[idx])
    idx += 1
    
    for case_num in range(1, num_cases + 1):
        if case_num > 1:
            print()
        print(f"Case {case_num}:")
        
        costs = [int(input_data[idx + i]) for i in range(36)]
        idx += 36
        
        num_queries = int(input_data[idx])
        idx += 1
        
        for _ in range(num_queries):
            query_num = int(input_data[idx])
            idx += 1
            
            min_cost = float('inf')
            cheapest_bases = []
            
            for base in range(2, 37):
                current_cost = 0
                n = query_num
                if n == 0:
                    current_cost = costs[0]
                else:
                    while n > 0:
                        current_cost += costs[n % base]
                        n //= base
                
                if current_cost < min_cost:
                    min_cost = current_cost
                    cheapest_bases = [base]
                elif current_cost == min_cost:
                    cheapest_bases.append(base)
            
            print(f"Cheapest base(s) for number {query_num}: {' '.join(map(str, cheapest_bases))}")

if __name__ == "__main__":
    solve()
