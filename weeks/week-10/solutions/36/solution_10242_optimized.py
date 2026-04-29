# solution_10242_optimized.py
# UVA 10242 優化解決方案
# 計算從起點到酒吧的最大搶劫金額
# 優化重點：使用記憶化搜索 (DFS + memo) 避免重複計算；正確處理訪問狀態

import sys
from functools import lru_cache

def solve_max_robbery(n, edges, atm_list, start, bars):
    """
    使用記憶化搜索計算最大搶劫金額
    - 優化：避免重複訪問相同節點，使用 memo 記錄已計算的結果
    """
    # 建圖（使用鄰接表表示）
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
    
    # 轉換為 tuple 以便用於 memo
    atm = tuple(atm_list)
    bar_set = frozenset(bars)
    
    @lru_cache(maxsize=None)
    def dfs(node, visited_mask):
        """
        DFS 搜索最大金額
        - node: 當前節點
        - visited_mask: 訪問過的節點集合（用位掩碼表示）
        """
        current_money = atm[node - 1]
        max_money = current_money
        
        # 如果到達酒吧，返回當前金額
        if node in bar_set:
            return max_money
        
        # 探索相鄰節點
        for next_node in graph[node]:
            if not (visited_mask & (1 << next_node)):
                # 標記為已訪問
                new_mask = visited_mask | (1 << next_node)
                max_money = max(max_money, current_money + dfs(next_node, new_mask))
        
        return max_money
    
    # 從起點開始，起點已訪問
    initial_mask = 1 << start
    return dfs(start, initial_mask)

def main():
    """主程式"""
    data = sys.stdin.read().split()
    index = 0
    
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
    
    atm = []
    for _ in range(n):
        atm.append(int(data[index]))
        index += 1
    
    s = int(data[index])
    p = int(data[index + 1])
    index += 2
    
    bars = []
    for _ in range(p):
        bars.append(int(data[index]))
        index += 1
    
    result = solve_max_robbery(n, edges, atm, s, bars)
    print(result)

if __name__ == "__main__":
    main()
