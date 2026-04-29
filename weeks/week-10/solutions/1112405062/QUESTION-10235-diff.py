"""
UVA 10235 - Simply Empowered
=========================

題目說明：
- N x M 的網格 (1 <= N, M <= 11)
- 每格是 1(空) 或 0(有插座)
- 必須用蛇(環狀/封閉迴圈)覆蓋所有空格子
- 有插座的格子(0)不能被覆蓋
- 每個空格子(1)必須被剛好一條蛇佔據

解題思路：
- 使用 DFS + 迴溯枚舉所有環狀覆蓋
- 每次選擇未覆蓋格子，嘗試形成環狀
- 用 DP + bitmask 記錄已覆蓋狀態
- 緩存每個起始格子的所有可能環，避免重複計算
"""

import sys
from functools import lru_cache

MOD = 1000000007
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    T = int(data[0].strip())
    line_idx = 1

    for case in range(1, T + 1):
        N, M = map(int, data[line_idx].split())
        line_idx += 1

        grid = []
        for _ in range(N):
            row = list(map(int, data[line_idx].split()))
            line_idx += 1
            grid.append(row)

        result = count_tilings(N, M, grid)
        print(f"Case {case}: {result}")

def count_tilings(N, M, grid):
    empty_cells = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                empty_cells.append((r, c))

    n = len(empty_cells)
    if n == 0:
        return 1

    idx_map = {cell: i for i, cell in enumerate(empty_cells)}

    @lru_cache(maxsize=None)
    def get_cycles(start_idx):
        """返回以 start_idx 為起點的所有環的位元遮罩列表"""
        sr, sc = empty_cells[start_idx]
        cycles = []

        def backtrack(r, c, path, visited):
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                    idx = idx_map.get((nr, nc))
                    if idx is None:
                        continue

                    if idx == start_idx:
                        # 回到起點，形成一個環
                        if len(path) >= 3:
                            cycle_mask = 0
                            for cell in path:
                                cycle_mask |= (1 << idx_map[cell])
                            cycles.append(cycle_mask)
                        continue

                    if idx not in visited:
                        visited.add(idx)
                        path.append((nr, nc))
                        backtrack(nr, nc, path, visited)
                        path.pop()
                        visited.remove(idx)

        backtrack(sr, sc, [(sr, sc)], {start_idx})
        return tuple(cycles)

    @lru_cache(maxsize=None)
    def dp(mask):
        if mask == (1 << n) - 1:
            return 1

        for i in range(n):
            if not (mask >> i) & 1:
                ways = 0
                for cycle_mask in get_cycles(i):
                    if (cycle_mask & mask) == 0:
                        ways = (ways + dp(mask | cycle_mask)) % MOD
                return ways

        return 0

    return dp(0)

def main():
    solve()

if __name__ == "__main__":
    main()
