"""
題目：UVA 11005 - Cheapest Base
找出印刷一個數字成本最低的進位制
"""

def convert_to_base(n, base):
    """將十進位數n轉換為指定進位"""
    if n == 0:
        return [0]
    
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    
    return digits[::-1]

def get_digit_cost(digit, costs):
    """取得指定數字的成本
    0-9對應costs[0-9]
    A-Z對應costs[10-35]
    """
    return costs[digit]

def calculate_cost(digits, costs):
    """計算將digits中的所有數字印刷出來的總成本"""
    return sum(get_digit_cost(d, costs) for d in digits)

# 讀取測試資料組數
t = int(input())

for case_num in range(1, t + 1):
    # 讀取36個字元的成本
    costs = []
    for i in range(4):
        costs.extend(map(int, input().split()))
    
    # 讀取查詢數量
    q = int(input())
    
    # 輸出案例編號
    print(f"Case {case_num}:")
    
    # 處理每個查詢
    for _ in range(q):
        n = int(input())
        
        # 特殊情況: n == 0
        if n == 0:
            print(f"Cheapest base(s) for number {n}: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36")
            continue
        
        # 嘗試每個進位制(2-36)
        min_cost = float('inf')
        best_bases = []
        
        for base in range(2, 37):
            # 轉換為該進位制
            digits = convert_to_base(n, base)
            
            # 計算成本
            cost = calculate_cost(digits, costs)
            
            # 更新最低成本和對應的進位制
            if cost < min_cost:
                min_cost = cost
                best_bases = [base]
            elif cost == min_cost:
                best_bases.append(base)
        
        # 輸出結果
        bases_str = ' '.join(map(str, best_bases))
        print(f"Cheapest base(s) for number {n}: {bases_str}")
    
    # 測試資料之間空一行
    if case_num < t:
        print()
