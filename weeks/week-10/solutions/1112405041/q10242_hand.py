import sys

# 手打版本：Tarjan + DAG DP 解決魔改搶劫題
sys.setrecursionlimit(200000)

def solve():
    raw = sys.stdin.read().split()
    if not raw: return
    it = iter(raw)
    try:
        N = int(next(it))
        M = int(next(it))
    except StopIteration: return

    g = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = int(next(it)), int(next(it))
        g[u].append(v)

    val = [0] * (N+1)
    for i in range(1, N+1):
        val[i] = int(next(it))

    S = int(next(it))
    P = int(next(it))
    bars = set()
    for _ in range(P):
        bars.add(int(next(it)))

    dfn = [0] * (N+1)
    low = [0] * (N+1)
    stk = []
    ins = [False] * (N+1)
    sid = [0] * (N+1)
    cnt = 0
    tim = 0

    def tarjan(u):
        nonlocal tim, cnt
        tim += 1
        dfn[u] = low[u] = tim
        stk.append(u)
        ins[u] = True
        for v in g[u]:
            if not dfn[v]:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif ins[v]:
                low[u] = min(low[u], dfn[v])
        if low[u] == dfn[u]:
            cnt += 1
            while True:
                x = stk.pop()
                ins[x] = False
                sid[x] = cnt
                if x == u: break

    for i in range(1, N+1):
        if not dfn[i]: tarjan(i)

    s_val = [0] * (cnt + 1)
    s_bar = [False] * (cnt + 1)
    dag = [set() for _ in range(cnt + 1)]
    for u in range(1, N+1):
        u_sid = sid[u]
        s_val[u_sid] += val[u]
        if u in bars: s_bar[u_sid] = True
        for v in g[u]:
            if sid[v] != u_sid: dag[u_sid].add(sid[v])

    memo = {}
    def dfs_dag(u):
        if u in memo: return memo[u]
        res = -1e18
        if s_bar[u]: res = s_val[u]
        for v in dag[u]:
            sub = dfs_dag(v)
            if sub >= 0: res = max(res, s_val[u] + sub)
        memo[u] = res
        return res

    ans = dfs_dag(sid[S])
    print(int(max(0, ans)))

if __name__ == "__main__": solve()
