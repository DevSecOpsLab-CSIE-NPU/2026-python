import sys


def solve(data):
    nums = [int(x) for x in data.split()]
    if not nums:
        return ""

    it = iter(nums)
    n = next(it)
    m = next(it)

    g = [[] for _ in range(n + 1)]
    rg = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        g[u].append(v)
        rg[v].append(u)

    cash = [0] * (n + 1)
    for i in range(1, n + 1):
        cash[i] = next(it)

    start = next(it)
    p = next(it)
    is_bar = [False] * (n + 1)
    for _ in range(p):
        is_bar[next(it)] = True

    seen = [False] * (n + 1)
    order = []
    for s in range(1, n + 1):
        if seen[s]:
            continue
        stack = [(s, 0)]
        seen[s] = True
        while stack:
            u, idx = stack[-1]
            if idx < len(g[u]):
                v = g[u][idx]
                stack[-1] = (u, idx + 1)
                if not seen[v]:
                    seen[v] = True
                    stack.append((v, 0))
            else:
                order.append(u)
                stack.pop()

    comp = [-1] * (n + 1)
    comp_sum = []
    comp_has_bar = []
    for s in reversed(order):
        if comp[s] != -1:
            continue
        cid = len(comp_sum)
        comp_sum.append(0)
        comp_has_bar.append(False)
        stack = [s]
        comp[s] = cid
        while stack:
            u = stack.pop()
            comp_sum[cid] += cash[u]
            if is_bar[u]:
                comp_has_bar[cid] = True
            for v in rg[u]:
                if comp[v] == -1:
                    comp[v] = cid
                    stack.append(v)

    cnum = len(comp_sum)
    dag = [set() for _ in range(cnum)]
    for u in range(1, n + 1):
        cu = comp[u]
        for v in g[u]:
            cv = comp[v]
            if cu != cv:
                dag[cu].add(cv)

    start_c = comp[start]
    reachable = [False] * cnum
    stack = [start_c]
    reachable[start_c] = True
    while stack:
        u = stack.pop()
        for v in dag[u]:
            if not reachable[v]:
                reachable[v] = True
                stack.append(v)

    indeg = [0] * cnum
    for u in range(cnum):
        if not reachable[u]:
            continue
        for v in dag[u]:
            if reachable[v]:
                indeg[v] += 1

    from collections import deque

    q = deque(i for i in range(cnum) if reachable[i] and indeg[i] == 0)
    NEG = -10**18
    dp = [NEG] * cnum
    dp[start_c] = comp_sum[start_c]

    while q:
        u = q.popleft()
        for v in dag[u]:
            if not reachable[v]:
                continue
            if dp[u] != NEG:
                dp[v] = max(dp[v], dp[u] + comp_sum[v])
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    ans = 0
    for cid in range(cnum):
        if reachable[cid] and comp_has_bar[cid]:
            ans = max(ans, dp[cid])
    return str(ans)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
