import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline
    line = input().split()
    if not line:
        return
    n, m = map(int, line)
    graph = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        edges.append((u, v))
    money = [0] + [int(input().strip()) for _ in range(n)]
    s, p = map(int, input().split())
    bars = list(map(int, input().split()))

    # 優化點：先用 Tarjan 把 SCC 壓縮成 DAG，後續只做一次拓樸 DP。
    idx = 0
    dfn = [0] * (n + 1)
    low = [0] * (n + 1)
    in_stack = [False] * (n + 1)
    stack = []
    comp_id = [-1] * (n + 1)
    comp_cnt = 0

    def tarjan(u):
        nonlocal idx, comp_cnt
        idx += 1
        dfn[u] = low[u] = idx
        stack.append(u)
        in_stack[u] = True
        for v in graph[u]:
            if dfn[v] == 0:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])
        if low[u] == dfn[u]:
            while True:
                x = stack.pop()
                in_stack[x] = False
                comp_id[x] = comp_cnt
                if x == u:
                    break
            comp_cnt += 1

    for v in range(1, n + 1):
        if dfn[v] == 0:
            tarjan(v)

    comp_money = [0] * comp_cnt
    for v in range(1, n + 1):
        comp_money[comp_id[v]] += money[v]

    # 優化點：去重邊後再建 DAG，避免重複轉移造成額外成本。
    dag = [[] for _ in range(comp_cnt)]
    indeg = [0] * comp_cnt
    edge_set = set()
    for u, v in edges:
        cu, cv = comp_id[u], comp_id[v]
        if cu != cv and (cu, cv) not in edge_set:
            edge_set.add((cu, cv))
            dag[cu].append(cv)
            indeg[cv] += 1

    q = deque(i for i in range(comp_cnt) if indeg[i] == 0)
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in dag[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    start_comp = comp_id[s]
    neg = -10**30
    dp = [neg] * comp_cnt
    dp[start_comp] = comp_money[start_comp]
    for u in topo:
        if dp[u] == neg:
            continue
        for v in dag[u]:
            cand = dp[u] + comp_money[v]
            if cand > dp[v]:
                dp[v] = cand

    ans = 0
    for b in bars:
        cb = comp_id[b]
        if dp[cb] > ans:
            ans = dp[cb]
    print(ans)

if __name__ == "__main__":
    solve()
