import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    tokens = iter(input_data)
    num_cases = int(next(tokens))
    
    for case_num in range(1, num_cases + 1):
        if case_num > 1: print()
        costs = [int(next(tokens)) for _ in range(36)]
        print(f"Case {case_num}:")
        
        num_queries = int(next(tokens))
        for _ in range(num_queries):
            query = int(next(tokens))
            if query == 0:
                best_bases = list(range(2, 37))
            else:
                min_cost = float('inf')
                best_bases = []
                for base in range(2, 37):
                    temp, current_cost = query, 0
                    while temp > 0:
                        current_cost += costs[temp % base]
                        temp //= base
                    if current_cost < min_cost:
                        min_cost = current_cost
                        best_bases = [base]
                    elif current_cost == min_cost:
                        best_bases.append(base)
            print(f"Cheapest base(s) for number {query}: {' '.join(map(str, best_bases))}")

if __name__ == '__main__':
    main()