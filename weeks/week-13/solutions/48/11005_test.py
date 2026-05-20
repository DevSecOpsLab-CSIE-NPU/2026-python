"""
UVA 11005 Cheapest Base 測試程式
"""

def to_base(n, base):
    """轉換為進位表示"""
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def solve_test(input_data):
    """運行測試的求解函數"""
    lines = input_data.strip().split('\n')
    line_idx = 0
    
    T = int(lines[line_idx])
    line_idx += 1
    results = []
    
    for case in range(1, T + 1):
        costs = []
        for _ in range(4):
            costs.extend(map(int, lines[line_idx].split()))
            line_idx += 1
        
        Q = int(lines[line_idx])
        line_idx += 1
        
        results.append(f"Case {case}:")
        
        for _ in range(Q):
            num = int(lines[line_idx])
            line_idx += 1
            
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
            
            results.append(f"Cheapest base(s) for number {num}: {' '.join(map(str, best_bases))}")
        
        if case < T:
            results.append("")
    
    return "\n".join(results)


# 測試用例
test_input = """1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1
15
"""

print("=" * 60)
print("UVA 11005 Cheapest Base - 測試程式")
print("=" * 60)
print("\n【測試輸入】")
print(test_input)
print("\n【實際輸出】")
output = solve_test(test_input)
print(output)

# 測試 2
test_input2 = """1
1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18
19 20 21 22 23 24 25 26 27
28 29 30 31 32 33 34 35 36
2
15
255
"""

print("\n" + "=" * 60)
print("【測試 2】")
print("=" * 60)
print("\n【測試輸入】")
print(test_input2)
print("\n【實際輸出】")
output2 = solve_test(test_input2)
print(output2)
