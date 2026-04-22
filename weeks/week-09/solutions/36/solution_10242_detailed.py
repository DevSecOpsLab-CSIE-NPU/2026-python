# solution_10242_detailed.py
# UVA 10242 詳細註解版本解決方案
# 包含詳細的繁體中文註解

import sys

def max_robbery(n, edges, atm, s, bars):
    """
    計算從市中心出發，到達酒吧的最大搶劫金額。
    參數：
    - n: 路口數量
    - edges: 道路列表，每個是 (起點, 終點)
    - atm: 每個路口的 ATM 金額列表
    - s: 市中心路口編號
    - bars: 酒吧路口編號列表
    返回：最大金額
    """
    graph = [[] for _ in range(n+1)]  # 初始化圖，索引從 1 到 n
    for u, v in edges:
        graph[u].append(v)  # 添加有向邊
    def dfs(u, robbed):
        """
        深度優先搜索，計算從路口 u 開始的最大金額。
        參數：
        - u: 當前路口
        - robbed: 已經搶到的金額
        返回：最大金額
        """
        max_r = robbed + atm[u-1]  # 加上當前路口的 ATM 金額
        for v in graph[u]:
            # 遞歸到下一個路口
            max_r = max(max_r, dfs(v, max_r))
        return max_r
    max_rob = 0  # 初始化最大金額
    for bar in bars:
        # 計算從 s 到每個酒吧的最大金額，取最大
        max_rob = max(max_rob, dfs(s, 0))
    return max_rob

if __name__ == "__main__":
    data = sys.stdin.read().split()  # 讀取所有輸入數據
    index = 0  # 數據索引
    n = int(data[index])  # 路口數量
    m = int(data[index+1])  # 道路數量
    index += 2
    edges = []  # 道路列表
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
    atm = []  # ATM 金額列表
    for _ in range(n):
        atm.append(int(data[index]))
        index += 1
    s = int(data[index])  # 市中心
    p = int(data[index+1])  # 酒吧數量
    index += 2
    bars = []  # 酒吧列表
    for _ in range(p):
        bars.append(int(data[index]))
        index += 1
    print(max_robbery(n, edges, atm, s, bars))  # 輸出結果