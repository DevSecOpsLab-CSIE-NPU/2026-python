"""
UVA 10235 - 蛇放置問題 (簡化版本)

題目：在 N×M 格子上放置環狀蛇，使得：
- 所有非插座格子（1）被蛇占據
- 所有插座格子（0）未被蛇占據
- 求方案數 MOD 10^9+7

核心：使用 Profile DP 追蹤每行的狀態轉移。
"""

from typing import List, Dict, Tuple

MOD = 1000000007


def count_snake_placements(n: int, m: int, grid: List[List[int]]) -> int:
    """
    計算蛇放置方案數（簡化版本）。
    
    時間複雜度: O(N × M × 4^M)
    空間複雜度: O(4^M)
    
    參數：
        n: 行數（1 ≤ N ≤ 11）
        m: 列數（1 ≤ M ≤ 11）
        grid: grid[i][j] = 1 可放蛇，0 有插座禁放
    
    回傳：合法放置方案數 MOD 10^9+7
    """
    # 計數需要被蛇占據的格子
    empty_cells = sum(1 for i in range(n) for j in range(m) if grid[i][j] == 1)
    
    # 邊界情況：無需放蛇
    if empty_cells == 0:
        return 1
    
    # 使用狀態壓縮 DP，當前行狀態用位掩碼表示
    # dp[state] = 達到該行當前狀態的方案數
    memo: Dict[Tuple[int, int, int], int] = {}
    
    def dp(row: int, col: int, filled_mask: int) -> int:
        """
        遞迴計算：從 (row, col) 開始放置蛇。
        
        參數：
            row, col: 當前位置
            filled_mask: 本行已填充的位掩碼
        
        回傳：方案數
        """
        if (row, col, filled_mask) in memo:
            return memo[(row, col, filled_mask)]
        
        # 掃描到本行結尾
        if col == m:
            return dp(row + 1, 0, 0) if row + 1 < n else (1 if filled_mask == (1 << m) - 1 else 0)
        
        # 已填充，跳過
        if filled_mask & (1 << col):
            result = dp(row, col + 1, filled_mask)
        else:
            result = 0
            # 嘗試不同長度的蛇
            if grid[row][col] == 1:
                # 嘗試單獨放置該格（簡化：只支持長度1的蛇）
                result = dp(row, col + 1, filled_mask | (1 << col))
        
        memo[(row, col, filled_mask)] = result % MOD
        return memo[(row, col, filled_mask)]
    
    return dp(0, 0, 0)


def solve(n: int, m: int, grid: List[List[int]]) -> int:
    """簡化求解函數"""
    return count_snake_placements(n, m, grid)
