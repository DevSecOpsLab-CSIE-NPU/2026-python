# -*- coding: utf-8 -*-
import sys

def solve():
    # 使用 sys.stdin.read().split() 一次讀入所有空格分隔的 token
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for case in range(1, t + 1):
        # 讀取 36 個字元的印刷成本
        costs = [int(x) for x in input_data[idx : idx + 36]]
        idx += 36
        
        # 讀取查詢數量
        q = int(input_data[idx])
        idx += 1
        
        if case > 1:
            print()
        print(f"Case {case}:")
        
        for _ in range(q):
            n = int(input_data[idx])
            idx += 1
            
            min_cost = float('inf')
            best_bases = []
            
            # 遍歷 2 到 36 進位
            for b in range(2, 37):
                cost = 0
                temp = n
                if temp == 0:
                    cost = costs[0]
                else:
                    while temp > 0:
                        cost += costs[temp % b]
                        temp //= b
                
                if cost < min_cost:
                    min_cost = cost
                    best_bases = [b]
                elif cost == min_cost:
                    best_bases.append(b)
            
            print(f"Cheapest base(s) for number {n}: " + " ".join(map(str, best_bases)))

if __name__ == "__main__":
    solve()
