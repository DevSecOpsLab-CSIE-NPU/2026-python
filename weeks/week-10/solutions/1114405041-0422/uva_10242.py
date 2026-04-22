from __future__ import annotations

import sys


def solve(data: str) -> str:
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

    money = [0] * (n + 1)
    for i in range(1, n + 1):
        money[i] = next(it)

    s = next(it)
    p = next(it)
    bars = [False] * (n + 1)
    for _ in range(p):
        bars[next(it)] = True

    # 第一趟：計算 finishing order（迭代版 DFS，避免遞迴爆棧）
    visited = [False] * (n + 1)
    order: list[int] = []
    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack: list[tuple[int, int]] = [(start, 0)]
        visited[start] = True
        while stack:
            node, idx = stack[-1]
            if idx < len(g[node]):
                nxt = g[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
                stack.pop()

    # 第二趟：在反圖上找 SCC
    comp_id = [-1] * (n + 1)
    comp_sum: list[int] = []
    comp_bar: list[bool] = []

    for start in reversed(order):
        if comp_id[start] != -1:
            continue
        cid = len(comp_sum)
        comp_sum.append(0)
        comp_bar.append(False)
        stack = [start]
        comp_id[start] = cid
        while stack:
            node = stack.pop()
            comp_sum[cid] += money[node]
            if bars[node]:
                comp_bar[cid] = True
            for prev in rg[node]:
                if comp_id[prev] == -1:
                    comp_id[prev] = cid
                    stack.append(prev)

    cnum = len(comp_sum)
    dag = [set() for _ in range(cnum)]
    for u in range(1, n + 1):
        cu = comp_id[u]
        for v in g[u]:
            cv = comp_id[v]
            if cu != cv:
                dag[cu].add(cv)

    start_comp = comp_id[s]

    # 只在可達的 SCC 上做 DP
    reachable = [False] * cnum
    stack = [start_comp]
    reachable[start_comp] = True
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
    dp[start_comp] = comp_sum[start_comp]

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
        if reachable[cid] and comp_bar[cid] and dp[cid] > ans:
            ans = dp[cid]

    return str(ans)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
