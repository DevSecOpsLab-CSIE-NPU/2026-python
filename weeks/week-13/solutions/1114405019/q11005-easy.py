import sys

# 這個程式用來解決 UVA 11005 - Cheapest Base 題目
# 題目要求：給定 0-9, A-Z 每個字元的印刷成本，
# 對於給定的數字，找出在進位制 2 到 36 之中，哪一個進位制的總成本最低。

def solve():
    # 使用 sys.stdin.read().split() 一次讀取所有輸入，方便處理空白和換行
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    # 第一行是測試資料的組數
    num_cases = int(input_data[idx])
    idx += 1
    
    for case_num in range(1, num_cases + 1):
        # 輸出 Case 編號
        if case_num > 1:
            print() # 測試資料之間空一行
        print(f"Case {case_num}:")
        
        # 讀取 36 個字元的成本 (0-9, A-Z)
        costs = []
        for _ in range(36):
            costs.append(int(input_data[idx]))
            idx += 1
            
        # 讀取查詢數量
        num_queries = int(input_data[idx])
        idx += 1
        
        for _ in range(num_queries):
            query_num = int(input_data[idx])
            idx += 1
            
            min_cost = float('inf')
            cheapest_bases = []
            
            # 測試進位制 2 到 36
            for base in range(2, 37):
                current_cost = 0
                temp_num = query_num
                
                # 特殊處理 0 的情況
                if temp_num == 0:
                    current_cost = costs[0]
                else:
                    # 將數字轉換成該進位制並計算成本
                    while temp_num > 0:
                        digit = temp_num % base
                        current_cost += costs[digit]
                        temp_num //= base
                
                # 判斷是否為目前最低成本
                if current_cost < min_cost:
                    min_cost = current_cost
                    cheapest_bases = [base]
                elif current_cost == min_cost:
                    cheapest_bases.append(base)
            
            # 格式化輸出結果
            bases_str = " ".join(map(str, cheapest_bases))
            print(f"Cheapest base(s) for number {query_num}: {bases_str}")

if __name__ == "__main__":
    solve()
