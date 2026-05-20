import sys

# 1. 讀取所有輸入，直接變成一個「乾淨的整數陣列」
data = list(map(int, sys.stdin.read().split()))

if data:
    num_cases = data[0]
    idx = 1  # 用來追蹤目前讀取到 data 的哪一個位置

    for case_idx in range(1, num_cases + 1):
        # 換行處理：除了第一組外，每組開頭先印空行
        if case_idx > 1: print()
        print(f"Case {case_idx}:")
        
        # 2. 用切片直接拿取 36 個字元的成本
        costs = data[idx : idx + 36]
        num_queries = data[idx + 36]
        
        # 移動指標到查詢數字的起點
        idx += 37
        
        # 3. 處理每一個查詢
        for _ in range(num_queries):
            target = data[idx]
            idx += 1
            
            # 用一個列表儲存 2~36 進位的總成本
            ans_costs = []
            
            for base in range(2, 37):
                cost = 0
                n = target
                
                # 記憶口訣：只要 n 還能除，就一直「取餘數、找成本、除下去」
                while n > 0:
                    cost += costs[n % base]
                    n //= base
                
                # 0 的特例：如果 target 是 0，迴圈不會執行，成本直接是 costs[0]
                if target == 0: 
                    cost = costs[0]
                    
                ans_costs.append(cost)
            
            # 4. 找出最低成本，並利用「列表推導式」優雅地撈出答案
            min_c = min(ans_costs)
            cheapest = [str(b) for b in range(2, 37) if ans_costs[b - 2] == min_c]
            
            print(f"Cheapest base(s) for number {target}: {' '.join(cheapest)}")