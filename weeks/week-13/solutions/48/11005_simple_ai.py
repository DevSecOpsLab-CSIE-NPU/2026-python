# AI 教你的簡單版本 - UVA 11005 Cheapest Base
# 題目概念：找出印刷一個數字成本最低的進位制（2-36進位）

# 步驟 1: 將十進位數字轉換成特定進位的表示
def to_base(number, base):
    """
    將十進位數字轉換成指定進位的表示
    例如: to_base(255, 16) = [15, 15] 代表 0xFF
    """
    if number == 0:
        return [0]
    
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    
    # 反轉數字順序（因為是從個位開始計算）
    return digits[::-1]


# 步驟 2: 計算在特定進位下，一個數字的印刷成本
def calculate_cost(number, base, costs):
    """
    計算印刷一個數字在特定進位下的總成本
    costs: 長度36的列表，costs[i] 是字符 i 的成本
    """
    digits = to_base(number, base)
    total_cost = 0
    
    # 對每個數字位元，加上對應字符的成本
    for digit in digits:
        total_cost += costs[digit]
    
    return total_cost


# 步驟 3: 主解題邏輯
def solve():
    T = int(input())  # 測試資料組數
    
    for case_num in range(1, T + 1):
        # 讀取 36 個字符的成本（0-9, A-Z）
        costs = []
        for _ in range(4):
            costs.extend(map(int, input().split()))
        
        # 讀取查詢數量
        Q = int(input())
        
        # 輸出 Case 標題
        print(f"Case {case_num}:")
        
        # 處理每個查詢
        for _ in range(Q):
            number = int(input())
            
            # 找出所有進位中成本最低的
            min_cost = float('inf')
            best_bases = []
            
            # 嘗試所有進位（2-36）
            for base in range(2, 37):
                cost = calculate_cost(number, base, costs)
                
                # 如果找到更便宜的進位
                if cost < min_cost:
                    min_cost = cost
                    best_bases = [base]
                # 如果成本相同，也加入
                elif cost == min_cost:
                    best_bases.append(base)
            
            # 輸出結果
            bases_str = " ".join(map(str, best_bases))
            print(f"Cheapest base(s) for number {number}: {bases_str}")
        
        # 測試資料之間空一行
        if case_num < T:
            print()


# 執行
if __name__ == "__main__":
    solve()
