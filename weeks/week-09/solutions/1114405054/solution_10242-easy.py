#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
題目 10242 簡化版: ATM 搶劫 (SIMPLIFIED)
用更簡潔的方式實現圖論搜索

核心邏輯：
1. 從起點出發
2. DFS 探索所有可能的路徑
3. 在到達酒吧時記錄金額
4. 返回最大值
"""

from collections import defaultdict, deque

def solve_10242():
    """簡化版：BFS 尋找最大金額"""
    n, m = map(int, input().split())

    # 建立圖
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)

    # 讀取金額
    atm_values = [int(input()) for _ in range(n)]

    # 讀取起點和酒吧
    start, p = map(int, input().split())
    start -= 1
    bars = set(int(x) - 1 for x in input().split())

    # BFS
    max_money = 0
    visited = set()
    queue = deque([(start, frozenset([start]))])
    visited.add((start, frozenset([start])))

    while queue:
        node, robbed = queue.popleft()

        # 檢查是否在酒吧
        if node in bars:
            max_money = max(max_money, sum(atm_values[x] for x in robbed))

        # 探索相鄰
        for next_node in graph[node]:
            new_robbed = robbed | frozenset([next_node])
            state = (next_node, new_robbed)

            if state not in visited and len(visited) < 10000:
                visited.add(state)
                queue.append(state)

    return max_money


if __name__ == '__main__':
    result = solve_10242()
    print(result)
