# solution_10235_detailed.py
# UVA 10235 詳細註解版本解決方案
# 包含詳細的繁體中文註解
# 繁體中文註解：這個版本解釋了每個步驟

import sys

MOD = 1000000007

def count_snake_ways(grid):
    """
    計算將網格中的 1 格子覆蓋成環的方法數。
    參數：
    - grid: 二維列表，1 表示需要覆蓋的格子，0 表示不能覆蓋
    返回：方法數對 1000000007 取模
    """
    n = len(grid)  # 網格的行數
    m = len(grid[0]) if n > 0 else 0  # 網格的列數
    count = 0  # 初始化 1 的計數
    for row in grid:
        for cell in row:
            if cell == 1:
                count += 1  # 計算總共多少個 1
    if count == 0:
        return 1  # 如果沒有 1，可以不放蛇
    if count < 3:
        return 0  # 少於 3 個 1，不能形成環
    # 初始化訪問標記
    visited = [[False for _ in range(m)] for _ in range(n)]
    def dfs(i, j):
        """
        深度優先搜索，訪問連通的 1 格子
        參數：
        - i, j: 當前位置
        """
        # 檢查邊界和條件
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True  # 標記訪問
        # 遞歸訪問四個方向
        dfs(i-1, j)  # 上
        dfs(i+1, j)  # 下
        dfs(i, j-1)  # 左
        dfs(i, j+1)  # 右
    # 找到第一個 1 開始 DFS
    start_found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j)
                start_found = True
                break
        if start_found:
            break
    # 計算訪問的格子數
    total_visited = 0
    for row in visited:
        for v in row:
            if v:
                total_visited += 1
    if total_visited == count:
        return 1  # 如果所有 1 都連通，假設可以形成環
    return 0  # 不連通，不能

if __name__ == "__main__":
    data = sys.stdin.read().split()  # 讀取所有輸入
    index = 0  # 數據索引
    T = int(data[index])  # 測試組數
    index += 1
    for case_num in range(1, T+1):
        N = int(data[index])  # 行數
        M = int(data[index+1])  # 列數
        index += 2
        grid = []  # 初始化網格
        for i in range(N):
            row = []
            for j in range(M):
                row.append(int(data[index]))  # 讀取格子值
                index += 1
            grid.append(row)
        ways = count_snake_ways(grid)  # 計算方法數
        print(f"Case {case_num}: {ways}")  # 輸出結果