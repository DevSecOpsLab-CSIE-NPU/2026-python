# -*- coding: utf-8 -*-
import sys

def solve():
    """
    UVA 11005 — Cheapest Base 解題主程式
    """
    # 讀取所有輸入的 token
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = token_generator()
    
    # 取得測試資料組數
    try:
        t_str = next(tokens)
        num_cases = int(t_str)
    except StopIteration:
        return

    for case_idx in range(1, num_cases + 1):
        # 讀取 36 個字元的成本
        costs = []
        for _ in range(36):
            costs.append(int(next(tokens)))
        
        # 讀取查詢數量
        num_queries = int(next(tokens))
        
        # 輸出 Case 標頭，注意測試資料組之間要有一個空行
        if case_idx > 1:
            print()
        print(f"Case {case_idx}:")
        
        # 處理每個查詢
        for _ in range(num_queries):
            n = int(next(tokens))
            min_cost = float('inf')
            cheapest_bases = []
            
            # 測試 2 到 36 進位
            for base in range(2, 37):
                cost = 0
                if n == 0:
                    cost = costs[0]
                else:
                    temp = n
                    while temp > 0:
                        digit = temp % base
                        cost += costs[digit]
                        temp //= base
                
                if cost < min_cost:
                    min_cost = cost
                    cheapest_bases = [base]
                elif cost == min_cost:
                    cheapest_bases.append(base)
            
            # 格式化輸出答案
            bases_str = " ".join(map(str, cheapest_bases))
            print(f"Cheapest base(s) for number {n}: {bases_str}")

if __name__ == "__main__":
    solve()
