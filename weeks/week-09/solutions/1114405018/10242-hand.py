import sys


def solve(text):
    a = list(map(int, text.split()))
    if not a:
        return ""

    it = iter(a)
    n, m = next(it), next(it)

    g = [[] for _ in range(n + 1)]
    rg = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = next(it), next(it)
        g[u].append(v)
        rg[v].append(u)

    money = [0] + [next(it) for _ in range(n)]
    s, p = next(it), next(it)
    bars = {next(it) for _ in range(p)}

    sys.setrecursionlimit(1000000)

    vis, order = [0] * (n + 1), []

    def dfs1(u):
        vis[u] = 1
        for v in g[u]:
            if not vis[v]:
                dfs1(v)
        order.append(u)

    for i in range(1, n + 1):
        if not vis[i]:
            dfs1(i)

    comp, sm, has_bar = [0] * (n + 1), [], []

    def dfs2(u, cid):
        comp[u] = cid
        sm[cid] += money[u]
        has_bar[cid] |= u in bars
        for v in rg[u]:
            if not comp[v]:
                dfs2(v, cid)

    for u in reversed(order):
        if not comp[u]:
            sm.append(0)
            has_bar.append(False)
            dfs2(u, len(sm) - 1)

    k = len(sm)
    dag = [set() for _ in range(k)]
    for u in range(1, n + 1):
        cu = comp[u]
        for v in g[u]:
            cv = comp[v]
            if cu != cv:
                dag[cu].add(cv)

    start = comp[s]
    reach = [0] * k
    st = [start]
    reach[start] = 1
    while st:
        u = st.pop()
        for v in dag[u]:
            if not reach[v]:
                reach[v] = 1
                st.append(v)

    indeg = [0] * k
    for u in range(k):
        if reach[u]:
            for v in dag[u]:
                if reach[v]:
                    indeg[v] += 1

    neg = -10**30
    dp = [neg] * k
    dp[start] = sm[start]
    q = [u for u in range(k) if reach[u] and indeg[u] == 0]

    for u in q:
        if dp[u] != neg:
            for v in dag[u]:
                if reach[v] and dp[u] + sm[v] > dp[v]:
                    dp[v] = dp[u] + sm[v]
        for v in dag[u]:
            if reach[v]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

    ans = max((dp[i] for i in range(k) if reach[i] and has_bar[i]), default=0)
    return str(ans) + "\n"


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()