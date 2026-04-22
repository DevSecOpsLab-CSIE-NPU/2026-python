# solution_10242_easy.py
# UVA 10242 簡單版本解決方案
# 使用簡單 DFS，更容易記憶
# 繁體中文註解：這個版本用簡單的 DFS 計算最大金額

import sys

def max_robbery(n, edges, atm, s, bars):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
    def dfs(u, robbed):
        max_r = robbed + atm[u-1]
        for v in graph[u]:
            max_r = max(max_r, dfs(v, max_r))
        return max_r
    max_rob = 0
    for bar in bars:
        max_rob = max(max_rob, dfs(s, 0))
    return max_rob

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