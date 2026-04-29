# solution_10242.py
# UVA 10242 解決方案
# 計算從市中心到酒吧的最大搶劫金額
# 繁體中文註解：這個程式使用 DP 計算圖上的最大金額路徑

import sys

def max_robbery(n, edges, atm, s, bars):
    # 建圖
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
    # 簡單 DFS，忽略重複訪問的複雜性
    def dfs(u, robbed, visited):
        if u in visited:
            return robbed
        visited.add(u)
        max_r = robbed + atm[u-1]
        for v in graph[u]:
            max_r = max(max_r, dfs(v, max_r, visited.copy()))
        return max_r
    max_rob = 0
    for bar in bars:
        max_rob = max(max_rob, dfs(s, 0, set()))
    return max_rob

# 主程式
if __name__ == "__main__":
    data = sys.stdin.read().split()
    index = 0
    n = int(data[index])
    m = int(data[index+1])
    index += 2
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
    atm = []
    for _ in range(n):
        atm.append(int(data[index]))
        index += 1
    s = int(data[index])
    p = int(data[index+1])
    index += 2
    bars = []
    for _ in range(p):
        bars.append(int(data[index]))
        index += 1
    print(max_robbery(n, edges, atm, s, bars))