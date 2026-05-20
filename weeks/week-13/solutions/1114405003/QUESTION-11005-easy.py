"""
題目：UVA 11005 - Cheapest Base (簡化版)
找出印刷一個數字成本最低的進位制

核心邏輯:
1. 獲得36個字元(0-9, A-Z)的印刷成本
2. 對每個可能的進位制(2到36):
   - 將十進位數轉換為該進位制
   - 計算各位數字的成本總和
3. 找出成本最低的進位制(如果多個並列則全部輸出)
"""

# 讀取測試資料組數
t = int(input())

for case_num in range(1, t + 1):
    # 讀取36個字元的成本(0-9九個,分4行讀入)
    costs = []
    for i in range(4):
        costs.extend(map(int, input().split()))  # 讀入9個成本,加入列表
    
    # 讀取此組測試的查詢數量
    q = int(input())
    
    # 輸出案例編號
    print(f"Case {case_num}:")
    
    # 處理每一個要查詢的十進位數
    for _ in range(q):
        n = int(input())  # 要轉換的十進位數
        
        # 初始化
        min_cost = float('inf')  # 最小成本
        best_bases = []  # 成本最低的進位制清單
        
        # 逐一嘗試每個進位制(2進位到36進位)
        for base in range(2, 37):
            # 將n轉換為該進位制,得到各位數字
            temp = n
            digits = []
            while temp > 0:
                digits.append(temp % base)  # 取得最低位數字
                temp //= base  # 移除最低位
            
            # 計算該進位制表示的成本
            cost = sum(costs[d] for d in digits)
            
            # 如果這個進位制的成本更低,更新最小成本和進位制清單
            if cost < min_cost:
                min_cost = cost
                best_bases = [base]
            # 如果成本相同,加入清單
            elif cost == min_cost:
                best_bases.append(base)
        
        # 輸出結果
        bases_str = ' '.join(map(str, best_bases))
        print(f"Cheapest base(s) for number {n}: {bases_str}")
    
    # 多個測試資料之間輸出空行
    if case_num < t:
        print()
