from __future__ import annotations

import sys
from collections import deque


def kosaraju(graph: list[list[int]]) -> list[int]:
    n = len(graph)

    # 建反向圖。
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            rev[v].append(u)

    # 第一次 DFS：收集完成序。
    order: list[int] = []
    vis = [False] * n
    for s in range(n):
        if vis[s]:
            continue
        stack = [(s, 0)]
        vis[s] = True
        while stack:
            u, k = stack[-1]
            if k < len(graph[u]):
                v = graph[u][k]
                stack[-1] = (u, k + 1)
                if not vis[v]:
                    vis[v] = True
                    stack.append((v, 0))
            else:
                order.append(u)
                stack.pop()

    # 第二次 DFS：在反向圖切 SCC。
    comp = [-1] * n
    cid = 0
    for s in reversed(order):
        if comp[s] != -1:
            continue
        q = [s]
        comp[s] = cid
        for u in q:
            for v in rev[u]:
                if comp[v] == -1:
                    comp[v] = cid
                    q.append(v)
        cid += 1

    return comp


def solve_case(n: int, edges: list[tuple[int, int]], money: list[int], start: int, bars: list[int]) -> int:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    comp = kosaraju(graph)
    comp_n = max(comp) + 1

    # 每個 SCC 的總金額。
    comp_money = [0] * comp_n
    for i, val in enumerate(money):
        comp_money[comp[i]] += val

    # 建 SCC 凝縮 DAG。
    dag = [[] for _ in range(comp_n)]
    indeg = [0] * comp_n
    for u, v in edges:
        cu = comp[u]
        cv = comp[v]
        if cu != cv:
            dag[cu].append(cv)
            indeg[cv] += 1

    s_comp = comp[start]
    bar_comps = {comp[x] for x in bars}

    # 拓樸排序。
    q = deque(i for i in range(comp_n) if indeg[i] == 0)
    topo: list[int] = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in dag[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # DAG 上最大路徑 DP。
    NEG = -10**30
    dp = [NEG] * comp_n
    dp[s_comp] = comp_money[s_comp]

    for u in topo:
        if dp[u] == NEG:
            continue
        for v in dag[u]:
            dp[v] = max(dp[v], dp[u] + comp_money[v])

    return max(dp[c] for c in bar_comps)


def main() -> None:
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return

    idx = 0
    out: list[str] = []

    while idx < len(nums):
        n = nums[idx]
        m = nums[idx + 1]
        idx += 2

        edges: list[tuple[int, int]] = []
        for _ in range(m):
            u = nums[idx] - 1
            v = nums[idx + 1] - 1
            idx += 2
            edges.append((u, v))

        money = nums[idx:idx + n]
        idx += n

        start = nums[idx] - 1
        p = nums[idx + 1]
        idx += 2

        bars = [nums[idx + i] - 1 for i in range(p)]
        idx += p

        out.append(str(solve_case(n, edges, money, start, bars)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()