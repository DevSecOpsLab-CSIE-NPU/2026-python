import sys
from collections import deque


def add_edge(head, to, nxt, idx, u, v):
    # 使用陣列式鄰接串列（forward star）加一條邊 u -> v
    to[idx] = v
    nxt[idx] = head[u]
    head[u] = idx


def solve():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    # 原圖與反圖都要建
    head = [-1] * (n + 1)
    rev_head = [-1] * (n + 1)

    to = [0] * m
    nxt = [0] * m
    rev_to = [0] * m
    rev_nxt = [0] * m

    # 保留原始邊，之後建縮點圖會用到
    edges_u = [0] * m
    edges_v = [0] * m

    for i in range(m):
        u, v = map(int, input().split())
        edges_u[i] = u
        edges_v[i] = v

        add_edge(head, to, nxt, i, u, v)
        add_edge(rev_head, rev_to, rev_nxt, i, v, u)

    # 每個點的 ATM 金額
    money = [0] * (n + 1)
    for i in range(1, n + 1):
        money[i] = int(input())

    # S 是起點，P 是酒吧數量
    s, p = map(int, input().split())
    bars_nodes = list(map(int, input().split()))

    is_bar_node = [False] * (n + 1)
    for x in bars_nodes:
        is_bar_node[x] = True

    # ============================================================
    # 第一步：在原圖上做非遞迴 DFS，求 finishing order
    # ============================================================
    visited = [False] * (n + 1)
    order = []

    for start in range(1, n + 1):
        if visited[start]:
            continue

        visited[start] = True

        # stack 內存：(目前節點, 下一條準備看的邊)
        stack = [(start, head[start])]

        while stack:
            u, edge_idx = stack[-1]

            # 若這個點的所有出邊都看完了
            # 就可以把它加入 finishing order
            if edge_idx == -1:
                order.append(u)
                stack.pop()
                continue

            # 把目前節點的「下一條要看的邊」往後移
            stack[-1] = (u, nxt[edge_idx])
            v = to[edge_idx]

            if not visited[v]:
                visited[v] = True
                stack.append((v, head[v]))

    # ============================================================
    # 第二步：依 finishing order 反過來，在反圖上找 SCC
    # ============================================================
    comp_id = [0] * (n + 1)
    comp_count = 0

    # 讓 SCC 編號從 1 開始，所以第 0 格先占位
    comp_money = [0]
    comp_has_bar = [False]

    for start in reversed(order):
        if comp_id[start] != 0:
            continue

        comp_count += 1
        total_money = 0
        has_bar = False

        stack = [start]
        comp_id[start] = comp_count

        while stack:
            u = stack.pop()

            total_money += money[u]
            if is_bar_node[u]:
                has_bar = True

            edge_idx = rev_head[u]
            while edge_idx != -1:
                v = rev_to[edge_idx]
                if comp_id[v] == 0:
                    comp_id[v] = comp_count
                    stack.append(v)
                edge_idx = rev_nxt[edge_idx]

        comp_money.append(total_money)
        comp_has_bar.append(has_bar)

    # ============================================================
    # 建立 SCC 縮點後的 DAG
    # ============================================================
    dag = [[] for _ in range(comp_count + 1)]
    indeg = [0] * (comp_count + 1)

    for i in range(m):
        cu = comp_id[edges_u[i]]
        cv = comp_id[edges_v[i]]

        # 同一個 SCC 內的邊不用加到縮點圖
        if cu != cv:
            dag[cu].append(cv)
            indeg[cv] += 1

    # ============================================================
    # 在 DAG 上做最長路 DP
    # dp[c] = 從起點 SCC 走到 c 時，最多能拿多少錢
    # ============================================================
    start_comp = comp_id[s]
    dp = [-1] * (comp_count + 1)
    dp[start_comp] = comp_money[start_comp]

    # 先做拓樸排序
    q = deque()
    for c in range(1, comp_count + 1):
        if indeg[c] == 0:
            q.append(c)

    while q:
        u = q.popleft()

        for v in dag[u]:
            # 只有當 u 可達時，才能拿它更新 v
            if dp[u] != -1:
                cand = dp[u] + comp_money[v]
                if cand > dp[v]:
                    dp[v] = cand

            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # 在所有含有酒吧的 SCC 中取最大值
    ans = 0
    for c in range(1, comp_count + 1):
        if comp_has_bar[c] and dp[c] > ans:
            ans = dp[c]

    print(ans)


if __name__ == "__main__":
    solve()