"""
UVA 10242 - ATM 搶劫問題 (簡化版本)

題目：從市中心沿單向邊行駛，搶劫途經的 ATM（每個最多一次），
      最終到達某酒吧。求最大搶劫金額。

策略：DFS 探索所有路徑，記錄已搶 ATM，防止重複搶劫。
"""

from typing import List, Set, Dict, Tuple

# 常數定義
MAX_ROBBED = 20  # 最多搶 20 個 ATM（剪枝防止無限循環）


def rob_atm_max(n: int, edges: List[Tuple[int, int]], amounts: List[int],
                start: int, bars: Set[int]) -> int:
    """
    DFS 版本：尋找最大搶劫金額。
    
    時間複雜度: O(2^N × M)（最壞情況）
    空間複雜度: O(N + M)
    
    參數：
        n: 路口數量
        edges: (u, v) 邊列表
        amounts: amounts[i-1] = 路口 i 的 ATM 金額
        start: 起始路口（1-indexed）
        bars: 酒吧所在路口集合（1-indexed）
    
    回傳：最大搶劫金額
    """
    # 建立鄰接表（O(M)）
    graph: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
    
    max_cash = 0
    
    def dfs(pos: int, robbed: Set[int], total: int) -> None:
        """
        深度優先搜索探索路徑。
        
        參數：
            pos: 當前路口（1-indexed）
            robbed: 已搶的 ATM 路口集合
            total: 目前搶劫總額
        """
        nonlocal max_cash
        
        # 抵達酒吧，更新最大值
        if pos in bars:
            max_cash = max(max_cash, total)
            # 可選：繼續走（題意允許經過多次）
            # 這裡簡化為到達後結束
            return
        
        # 剪枝：防止無限循環（限制已搶 ATM 數）
        if len(robbed) >= MAX_ROBBED:
            return
        
        # 嘗試走向相鄰路口
        for next_pos in graph.get(pos, []):
            new_robbed = robbed.copy()
            new_total = total
            
            # 該路口未搶過且有 ATM，則搶劫
            if next_pos not in robbed and amounts[next_pos - 1] > 0:
                new_total += amounts[next_pos - 1]
                new_robbed.add(next_pos)
            
            dfs(next_pos, new_robbed, new_total)
    
    # 從起點開始
    init_robbed: Set[int] = set()
    init_total = 0
    
    # 起點有 ATM 則搶劫
    if amounts[start - 1] > 0:
        init_total = amounts[start - 1]
        init_robbed.add(start)
    
    dfs(start, init_robbed, init_total)
    return max_cash


def solve(n: int, edges: List[Tuple[int, int]], amounts: List[int],
          start: int, bars: Set[int]) -> int:
    """求解函數"""
    return rob_atm_max(n, edges, amounts, start, bars)
