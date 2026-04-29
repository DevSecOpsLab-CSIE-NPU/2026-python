"""
UVA 10235 - Simply Empowered (Easy Version)
=====================================

題目說明：
- 小 P 家裡的地板是 N x M 的網格
- 每個格子可能是 1 (空) 或 0 (有插座)
- 蛇是咬著自己尾巴的環狀
- 有插座的格子不能被蛇佔據
- 每個空格子必須被一條蛇佔據

解題思路（簡單版）：
- 把空格子分成若干組
- 每組必須形成一個封閉環狀（至少 3 格）
- 使用 DFS + 迴溯枚舉所有分組方式
- 用 bitmask 記錄已覆蓋的格子
- 用 memoization (lru_cache) 避免重複計算
"""

import sys
from functools import lru_cache

MOD = 1000000007          # 輸出結果需取此模數
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 四個方向：右、下、左、上

def solve():
    """主函式：讀取輸入、處理測資、輸出結果"""
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    
    T = int(data[0].strip())   # 測資筆數
    idx = 1               # 目前讀取的行索引
    
    for case in range(1, T + 1):
        # --- 讀取 N, M ---
        N, M = map(int, data[idx].split())
        idx += 1
        
        # --- 讀取網格 ---
        # grid[r][c] = 1 表示空格子，= 0 表示有插座
        grid = [list(map(int, data[idx + i].split())) for i in range(N)]
        idx += N
        
        # --- 計算答案 ---
        ans = count(N, M, grid)
        print(f"Case {case}: {ans}")

def count(N, M, grid):
    """
    計算所有合法放置蛇的方法數量
    
    參數：
    - N, M: 網格大小
    - grid: 網格內容，1=空格子, 0=有插座
    
    回傳：方法數（MOD 1000000007）
    """
    # --- 收集所有空格子 ---
    # cells[i] = (row, col) 表示第 i 個空格子的座標
    cells = [(r, c) for r in range(N) for c in range(M) if grid[r][c] == 1]
    n = len(cells)     # 空格子數量
    
    if n == 0:
        return 1     # 沒有空格子，只有一種擺法（不放蛇）
    
    # --- 建立座標到索引的映射 ---
    # pos_to_idx[(r,c)] = i 表示座標 (r,c) 是第 i 個空格子
    pos_to_idx = {cells[i]: i for i in range(n)}
    
    @lru_cache(maxsize=None)
    def dfs(mask):
        """
        DP 遞迴：嘗試覆蓋剩餘空格
        
        參數：
        - mask: bitmask，表示哪些格子已被覆蓋
               bit i = 1 表示第 i 個格子已被覆蓋
        
        回傳：剩餘格子的合法覆蓋方法數
        """
        # 所有格子都已覆蓋，搜尋完成！
        if mask == (1 << n) - 1:
            return 1
        
        ways = 0
        
        # 找到第一個尚未覆蓋的格子當作起點
        first = 0
        for i in range(n):
            if not (mask >> i) & 1:
                first = i
                break
        
        # 從這個起點嘗試形成各種環狀
        r, c = cells[first]
        for cyc in make_cycle(first, mask, N, M, grid, cells, pos_to_idx):
            # 把這個環狀的格子都標記為已覆蓋
            new_mask = mask
            for j in cyc:
                new_mask |= (1 << j)
            # 繼續覆蓋剩下的格子
            ways = (ways + dfs(new_mask)) % MOD
        
        return ways
    
    def make_cycle(start, used, N, M, grid, cells, pos_to_idx):
        """
        找出以第 start 個格子為起點的所有可能環狀
        
        參數：
        - start: 起點格子的索引
        - used: 目前已使用的格子 (bitmask)
        - N, M: 網格大小
        - grid: 網格內容
        - cells: 所有空格子座標��表
        - pos_to_idx: 座標到索引的映射
        
        回傳：所有可能環狀的列表，每個環狀是一串格子索引
        """
        cycles = []
        
        def go(r, c, path, seen):
            """
            DFS 遞迴：嘗試延伸路徑
            
            參數：
            - r, c: 目前位置
            - path: 到目前為止經過的格子座標列表
            - seen: 已訪問的格子集合
            """
            # 路徑至少 3 格 且 回到起點 → 形成環狀！
            if len(path) >= 3 and (r, c) == cells[start]:
                # 確認路徑上沒有重複格子
                if len(set(path)) == len(path):
                    # 把環狀的座標轉換為索引
                    cycle_idx = [pos_to_idx[p] for p in path]
                    cycles.append(cycle_idx)
                return
            
            # 四個方向嘗試延伸
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # 檢查邊界、網格內容、是否已訪問
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                    p = (nr, nc)
                    if p in pos_to_idx and p not in seen:
                        # 繼續延伸
                        go(nr, nc, path + [p], seen | {p})
        
        # 從起點開始 DFS
        sr, sc = cells[start]
        go(sr, sc, [cells[start]], {cells[start]})
        
        return cycles
    
    return dfs(0)

if __name__ == "__main__":
    solve()