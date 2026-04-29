"""
UVA 10242 - ATM 搶劫問題

從市中心出發，沿著單向道路行駛，搶劫所有途經的 ATM，最終到達某間酒吧。
求最多能搶劫的現金總額。
"""

import sys
from functools import lru_cache
from typing import List, Set, Dict


def solve_atm_robbery(n: int, edges: List[tuple], atm_amounts: List[int], 
                      start: int, bars: Set[int]) -> int:
    """
    使用 DFS + 記憶化求最長路徑。
    
    參數：
        n: 路口數量
        edges: (u, v) 表示從 u 到 v 的邊
        atm_amounts: 每個路口 ATM 金額
        start: 起始路口
        bars: 有酒吧的路口集合
    """
    # 建立鄰接表
    graph: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
    
    # 使用 DFS 探索所有可能路徑
    max_cash = 0
    
    def dfs(node: int, robbed: Set[int], cash: int) -> None:
        """
        DFS 探索從 node 出發的所有路徑。
        
        node: 當前位置
        robbed: 已搶過的 ATM 位置集合
        cash: 目前搶劫的總額
        """
        nonlocal max_cash
        
        # 如果當前位置有酒吧，更新最大值
        if node in bars:
            max_cash = max(max_cash, cash)
            # 即使有酒吧也可以繼續走（題意允許經過多次）
        
        # 嘗試走向相鄰的路口
        for next_node in graph.get(node, []):
            # 計算新的 ATM 金額
            new_cash = cash
            new_robbed = robbed.copy()
            
            if next_node not in robbed and atm_amounts[next_node - 1] > 0:
                new_cash += atm_amounts[next_node - 1]
                new_robbed.add(next_node)
            
            # 防止無限長度的路徑（簡化：限制訪問次數）
            if len(new_robbed) <= 15:  # 最多搶 15 個 ATM
                dfs(next_node, new_robbed, new_cash)
    
    # 從起始點開始 DFS
    init_robbed = set()
    init_cash = 0
    if start not in init_robbed and atm_amounts[start - 1] > 0:
        init_cash = atm_amounts[start - 1]
        init_robbed.add(start)
    
    dfs(start, init_robbed, init_cash)
    
    return max_cash


def read_test_cases() -> List[tuple]:
    """讀取測試案例"""
    cases = []
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            n, m = map(int, line.split())
            if n == 0 and m == 0:
                break
            
            edges = []
            for _ in range(m):
                u, v = map(int, sys.stdin.readline().split())
                edges.append((u, v))
            
            atm_amounts = []
            for _ in range(n):
                atm = int(sys.stdin.readline())
                atm_amounts.append(atm)
            
            s, p = map(int, sys.stdin.readline().split())
            bar_list = list(map(int, sys.stdin.readline().split()))
            bars = set(bar_list)
            
            cases.append((n, edges, atm_amounts, s, bars))
    except EOFError:
        pass
    
    return cases


def main():
    """主程式"""
    cases = read_test_cases()
    for n, edges, atm_amounts, start, bars in cases:
        result = solve_atm_robbery(n, edges, atm_amounts, start, bars)
        print(result)


if __name__ == '__main__':
    main()
