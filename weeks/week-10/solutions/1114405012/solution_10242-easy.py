# -*- coding: utf-8 -*-
"""
UVA 10242 - Highways 簡化版
從起點出發，沿著單向道路搶劫 ATM，最後到達酒吧
求搶劫現金最多的路線
"""

from collections import defaultdict, deque

def solve(inp):
    lines = inp.strip().split('\n')
    idx = 0
    
    n, m = map(int, lines[idx].split())
    idx += 1
    
    # 構建圖
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, lines[idx].split())
        graph[u].append(v)
        idx += 1
    
    # 讀取 ATM 現金
    atm = {}
    for i in range(1, n + 1):
        atm[i] = int(lines[idx])
        idx += 1
    
    s, p = map(int, lines[idx].split())
    idx += 1
    
    bars = set(map(int, lines[idx].split()))
    
    # DFS 搜尋最大現金
    max_cash = 0
    
    def dfs(node, cash, visited):
        nonlocal max_cash
        
        # 如果到達酒吧，記錄現金
        if node in bars:
            max_cash = max(max_cash, cash)
            # 可以繼續探索（允許回路）
        
        # 限制深度搜尋，避免無限迴圈
        if len(visited) > 20:
            return
        
        for next_node in graph[node]:
            if next_node not in visited:
                new_visited = visited | {next_node}
                dfs(next_node, cash + atm[next_node], new_visited)
    
    # 從起點開始
    dfs(s, atm[s], {s})
    
    return str(max_cash)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read()))
