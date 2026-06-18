# 10242 題目簡單版
# 用圖的 SCC 壓縮成 DAG，然後在 DAG 上做最長路徑 DP。

from collections import deque
from typing import List


def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    graph: List[List[int]] = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph[u].append(v)

    values = [int(next(it)) for _ in range(n)]
    start = int(next(it)) - 1
    p = int(next(it))
    bars = {int(next(it)) - 1 for _ in range(p)}

    def kosaraju() -> List[int]:
        visited = [False] * n
        stack: List[int] = []

        def dfs(u: int) -> None:
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)
            stack.append(u)

        for i in range(n):
            if not visited[i]:
                dfs(i)

        rev = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)

        comp = [-1] * n
        cid = 0

        def dfs2(u: int) -> None:
            nonlocal cid
            comp[u] = cid
            for v in rev[u]:
                if comp[v] == -1:
                    dfs2(v)

        while stack:
            u = stack.pop()
            if comp[u] == -1:
                dfs2(u)
                cid += 1

        return comp

    comp = kosaraju()
    comp_sum = [0] * (max(comp) + 1)
    for i in range(n):
        comp_sum[comp[i]] += values[i]

    dag = [[] for _ in range(len(comp_sum))]
    indegree = [0] * len(comp_sum)
    for u in range(n):
        for v in graph[u]:
            if comp[u] != comp[v]:
                dag[comp[u]].append(comp[v])
                indegree[comp[v]] += 1

    dp = [None] * len(comp_sum)
    dp[comp[start]] = comp_sum[comp[start]]
    queue = deque(i for i in range(len(comp_sum)) if indegree[i] == 0)
    order: List[int] = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in dag[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    for u in order:
        if dp[u] is None:
            continue
        for v in dag[u]:
            cand = dp[u] + comp_sum[v]
            if dp[v] is None or cand > dp[v]:
                dp[v] = cand

    answer = max(dp[comp[b]] for b in bars if dp[comp[b]] is not None)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    solve()
