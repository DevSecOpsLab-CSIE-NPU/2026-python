# solution_10235_easy.py
# UVA 10235 簡單版本解決方案
# 使用簡單的連通檢查，更容易記憶
# 繁體中文註解：這個版本用簡單的 DFS 檢查連通性

import sys

MOD = 1000000007

def count_snake_ways(grid):
    count = sum(sum(row) for row in grid)
    if count == 0:
        return 1
    if count < 3:
        return 0
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    visited = [[False] * m for _ in range(n)]
    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j)
                break
        else:
            continue
        break
    total_visited = sum(sum(row) for row in visited)
    if total_visited == count:
        return 1
    return 0

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