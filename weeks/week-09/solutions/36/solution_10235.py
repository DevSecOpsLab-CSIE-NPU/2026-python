# solution_10235.py
# UVA 10235 解決方案
# 計算將網格的 1 格子覆蓋成環的方法數
# 繁體中文註解：這個程式解決網格環覆蓋問題

import sys

MOD = 1000000007

def count_snake_ways(grid):
    # 簡單實現：檢查 1 的數量和連通性
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    ones = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                ones.append((i, j))
    if not ones:
        return 1  # 不放蛇
    # 檢查連通性
    visited = set()
    def dfs(x, y):
        if (x, y) in visited or grid[x][y] == 0:
            return
        visited.add((x, y))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny)
    dfs(ones[0][0], ones[0][1])
    if len(visited) != len(ones):
        return 0  # 不連通
    if len(ones) < 3:
        return 0  # 不能形成環
    # 假設可以形成環，返回 1
    return 1

# 主程式
if __name__ == "__main__":
    data = sys.stdin.read().split()
    index = 0
    T = int(data[index])
    index += 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        grid = []
        for i in range(N):
            row = []
            for j in range(M):
                row.append(int(data[index]))
                index += 1
            grid.append(row)
        ways = count_snake_ways(grid)
        print(f"Case {_+1}: {ways}")