import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    graph = [[] for _ in range(N)]
    rev = [[] for _ in range(N)]
    for _ in range(M):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph[u].append(v)
        rev[v].append(u)
    
    values = [int(next(it)) for _ in range(N)]
    S = int(next(it)) - 1
    P = int(next(it))
    bars = [int(next(it)) - 1 for _ in range(P)]
    
    ans = max_money(N, graph, rev, values, S, bars)
    print(ans)

def max_money(N, graph, rev, values, start, bars):
    visited = [False] * N
    order = []
    
    def dfs1(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs1(w)
        order.append(v)
    
    for v in range(N):
        if not visited[v]:
            dfs1(v)

    scc_id = [-1] * N
    scc_val = []
    
    def dfs2(v):
        scc_id[v] = len(scc_val)
        total = values[v]
        for w in rev[v]:
            if scc_id[w] == -1:
                total += dfs2(w)
        return total
    
    for v in reversed(order):
        if scc_id[v] == -1:
            scc_val.append(dfs2(v))
    
    K = len(scc_val)
    scc_graph = [set() for _ in range(K)]
    scc_bar = [False] * K
    
    for i in range(N):
        for j in graph[i]:
            if scc_id[i] != scc_id[j]:
                scc_graph[scc_id[i]].add(scc_id[j])
    
    for b in bars:
        scc_bar[scc_id[b]] = True
    
    start_scc = scc_id[start]
    
    dp = [-float('inf')] * K
    dp[start_scc] = 0
    
    for _ in range(K):
        for u in range(K):
            if dp[u] != -float('inf'):
                for v in scc_graph[u]:
                    if dp[v] < dp[u] + scc_val[v]:
                        dp[v] = dp[u] + scc_val[v]
    
    ans = 0
    for i in range(K):
        if scc_bar[i] and dp[i] > ans:
            ans = dp[i]
    
    return ans

if __name__ == "__main__":
    solve()