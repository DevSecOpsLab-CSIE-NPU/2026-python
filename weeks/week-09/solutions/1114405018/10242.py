import sys


def parse_input(text):
    vals = text.strip().split()
    if not vals:
        return None

    it = iter(vals)
    n = int(next(it))
    m = int(next(it))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))

    money = [0] * (n + 1)
    for i in range(1, n + 1):
        money[i] = int(next(it))

    start = int(next(it))
    p = int(next(it))
    bars = [int(next(it)) for _ in range(p)]

    return n, edges, money, start, bars


def solve(text):
    parsed = parse_input(text)
    if parsed is None:
        return ""

    n, edges, money, start, bars = parsed

    # 建圖與反圖（Kosaraju 需要）
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)

    # ---------- 第一次 DFS：取得 finishing order ----------
    visited = [False] * (n + 1)
    order = []

    for s in range(1, n + 1):
        if visited[s]:
            continue

        # 迭代版 DFS，避免遞迴深度限制
        stack = [(s, 0)]
        visited[s] = True

        while stack:
            node, idx = stack[-1]
            if idx < len(graph[node]):
                nxt = graph[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
                stack.pop()

    # ---------- 第二次 DFS（反圖）：切 SCC ----------
    comp_id = [-1] * (n + 1)
    comp_money = []
    comp_has_bar = []
    bars_set = set(bars)

    for s in reversed(order):
        if comp_id[s] != -1:
            continue

        cid = len(comp_money)
        comp_money.append(0)
        comp_has_bar.append(False)

        stack = [s]
        comp_id[s] = cid

        while stack:
            node = stack.pop()
            comp_money[cid] += money[node]
            if node in bars_set:
                comp_has_bar[cid] = True

            for nxt in rev_graph[node]:
                if comp_id[nxt] == -1:
                    comp_id[nxt] = cid
                    stack.append(nxt)

    comp_n = len(comp_money)

    # ---------- 縮點成 DAG ----------
    dag = [set() for _ in range(comp_n)]
    indeg = [0] * comp_n

    for u, v in edges:
        cu = comp_id[u]
        cv = comp_id[v]
        if cu != cv and cv not in dag[cu]:
            dag[cu].add(cv)
            indeg[cv] += 1

    # ---------- 只保留從起點 SCC 可達的部分 ----------
    start_c = comp_id[start]
    reachable = [False] * comp_n
    stack = [start_c]
    reachable[start_c] = True

    while stack:
        x = stack.pop()
        for y in dag[x]:
            if not reachable[y]:
                reachable[y] = True
                stack.append(y)

    # ---------- DAG 上做最大路徑 DP ----------
    # dp[c] = 走到 SCC c 時可搶最大金額（僅限從 start 可達）
    NEG = -10**30
    dp = [NEG] * comp_n
    dp[start_c] = comp_money[start_c]

    # 對可達子圖做拓樸排序（Kahn）
    indeg_r = [0] * comp_n
    for u in range(comp_n):
        if not reachable[u]:
            continue
        for v in dag[u]:
            if reachable[v]:
                indeg_r[v] += 1

    queue = [u for u in range(comp_n) if reachable[u] and indeg_r[u] == 0]
    q_idx = 0

    while q_idx < len(queue):
        u = queue[q_idx]
        q_idx += 1

        if dp[u] != NEG:
            for v in dag[u]:
                if reachable[v]:
                    cand = dp[u] + comp_money[v]
                    if cand > dp[v]:
                        dp[v] = cand

        for v in dag[u]:
            if reachable[v]:
                indeg_r[v] -= 1
                if indeg_r[v] == 0:
                    queue.append(v)

    # ---------- 在「可達酒吧 SCC」中取最大 ----------
    ans = 0
    for c in range(comp_n):
        if reachable[c] and comp_has_bar[c] and dp[c] > ans:
            ans = dp[c]

    return str(ans) + "\n"


def main():
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
