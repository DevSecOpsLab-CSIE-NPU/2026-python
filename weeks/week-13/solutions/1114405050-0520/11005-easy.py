import sys

def main():
    # 1. 讀取全部輸入並切割成串列
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 2. 建立迭代器，之後只要呼叫 next(tokens) 就可以一直拿到下一個資料
    # 這是解 CPE 非常好用的無腦讀取技巧，不用自己算 index！
    tokens = iter(input_data)
    
    num_cases = int(next(tokens))
    
    for case_num in range(1, num_cases + 1):
        # 測資之間空一行 (第一組前面不空)
        if case_num > 1:
            print()
            
        # 連續讀取 36 個成本
        costs = [int(next(tokens)) for _ in range(36)]
        print(f"Case {case_num}:")
        
        # 讀取查詢次數
        num_queries = int(next(tokens))
        for _ in range(num_queries):
            query = int(next(tokens))
            
            # 特例：0 在所有進位制都只印 '0'，成本都一樣
            if query == 0:
                best_bases = list(range(2, 37))
            else:
                min_cost = float('inf')
                best_bases = []
                
                # 測試 2~36 進位
                for base in range(2, 37):
                    temp, current_cost = query, 0
                    while temp > 0:
                        current_cost += costs[temp % base] # 累加當前位數的成本
                        temp //= base                      # 降階
                        
                    if current_cost < min_cost:
                        min_cost = current_cost
                        best_bases = [base]
                    elif current_cost == min_cost:
                        best_bases.append(base)
                        
            print(f"Cheapest base(s) for number {query}: {' '.join(map(str, best_bases))}")

if __name__ == '__main__':
    main()