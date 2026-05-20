import sys

def solve():
    # 讀取所有輸入標準輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    # 讀取測試資料組數
    num_cases = int(next(iterator))
    
    for case_idx in range(1, num_cases + 1):
        # 輸出 Case 標頭
        print(f"Case {case_idx}:")
        
        # 讀取 36 個字元的印刷成本 (0-9, A-Z)
        costs = []
        for _ in range(36):
            costs.append(int(next(iterator)))
            
        # 讀取查詢數量
        num_queries = int(next(iterator))
        
        # 處理每一個查詢數字
        for _ in range(num_queries):
            target_num = int(next(iterator))
            
            # 用來紀錄 2 到 36 進位的總成本
            # base_costs[b] 將代表進位制 b 的成本
            base_costs = {}
            
            for base in range(2, 37):
                current_cost = 0
                temp_num = target_num
                
                # 特例處理：如果數字是 0，其成本就是 costs[0]
                if temp_num == 0:
                    current_cost = costs[0]
                else:
                    # 進行進位制轉換並累加成本
                    while temp_num > 0:
                        remainder = temp_num % base
                        current_cost += costs[remainder]
                        temp_num //= base
                
                base_costs[base] = current_cost
            
            # 找出 2 到 36 進位中的最低成本
            min_cost = min(base_costs.values())
            
            # 找出所有符合最低成本的進位制
            cheapest_bases = [str(b) for b in range(2, 37) if base_costs[b] == min_cost]
            
            # 格式化輸出結果
            print(f"Cheapest base(s) for number {target_num}: {' '.join(cheapest_bases)}")
            
        # 測試資料之間需要空一行（最後一組不需要額外空行）
        if case_idx < num_cases:
            print()

if __name__ == "__main__":
    solve()