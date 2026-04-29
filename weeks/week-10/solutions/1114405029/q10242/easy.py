import sys
from collections import deque


def add_edge(head, to, nxt, idx, u, v):
    """
    使用陣列方式建立鄰接串列。

    head[u]：
    - u 這個點的第一條邊編號

    to[idx]：
    - 第 idx 條邊連到哪個點

    nxt[idx]：
    - 第 idx 條邊的下一條邊編號
    """
    to[idx] = v
    nxt[idx] = head[u]
    head[u] = idx


def solve():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    # 原圖
    head = [-1] * (n + 1)
    to = [0] * m
    nxt = [0] * m

    # 反圖
    rev_head = [-1] * (n + 1)
    rev_to = [0] * m
    rev_nxt = [0] * m

    # 記錄所有邊，之後建立縮點 DAG 會用到
    edges_u = [0] * m
    edges_v = [0] * m

    for i in range(m):
        u, v = map(int, input().split())

        edges_u[i] = u
        edges_v[i] = v

        add_edge(head, to, nxt, i, u, v)
        add_edge(rev_head, rev_to, rev_nxt, i, v, u)

    money = [0] * (n + 1)

    for i in range(1, n + 1):
        money[i] = int(input())

    start_node, bar_count = map(int, input().split())
    bar_nodes = list(map(int, input().split()))

    is_bar_node = [False] * (n + 1)

    for node in bar_nodes:
        is_bar_node[node] = True

    # ------------------------------------------------------------
    # 第一步：在原圖上做 DFS，求 finishing order
    # ------------------------------------------------------------
    visited = [False] * (n + 1)
    order = []

    for start in range(1, n + 1):
        if visited[start]:
            continue

        visited[start] = True
        stack = [(start, head[start])]

        while stack:
            u, edge_idx = stack[-1]

            # 這個點的所有邊都走完，加入 finishing order
            if edge_idx == -1:
                order.append(u)
                stack.pop()
                continue

            # 更新目前點下一次要看的邊
            stack[-1] = (u, nxt[edge_idx])

            v = to[edge_idx]

            if not visited[v]:
                visited[v] = True
                stack.append((v, head[v]))

    # ------------------------------------------------------------
    # 第二步：按照 finishing order 反向，在反圖上找 SCC
    # ------------------------------------------------------------
    comp_id = [0] * (n + 1)
    comp_count = 0

    # SCC 編號從 1 開始，所以第 0 格不用
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

    # ------------------------------------------------------------
    # 第三步：建立縮點後的 DAG
    # ------------------------------------------------------------
    dag = [[] for _ in range(comp_count + 1)]
    indegree = [0] * (comp_count + 1)

    for i in range(m):
        u_comp = comp_id[edges_u[i]]
        v_comp = comp_id[edges_v[i]]

        # 不同 SCC 之間才需要連邊
        if u_comp != v_comp:
            dag[u_comp].append(v_comp)
            indegree[v_comp] += 1

    # ------------------------------------------------------------
    # 第四步：在 DAG 上做拓樸排序 + 最長路 DP
    # ------------------------------------------------------------
    start_comp = comp_id[start_node]

    # dp[c] 表示從起點 SCC 走到 SCC c 時，最多可以拿到多少錢
    dp = [-1] * (comp_count + 1)
    dp[start_comp] = comp_money[start_comp]

    queue = deque()

    for comp in range(1, comp_count + 1):
        if indegree[comp] == 0:
            queue.append(comp)

    while queue:
        u = queue.popleft()

        for v in dag[u]:
            # 只有從起點可以走到的 SCC 才需要更新
            if dp[u] != -1:
                candidate = dp[u] + comp_money[v]

                if candidate > dp[v]:
                    dp[v] = candidate

            indegree[v] -= 1

            if indegree[v] == 0:
                queue.append(v)

    # ------------------------------------------------------------
    # 第五步：答案是所有有酒吧 SCC 中，dp 最大的值
    # ------------------------------------------------------------
    answer = 0

    for comp in range(1, comp_count + 1):
        if comp_has_bar[comp] and dp[comp] > answer:
            answer = dp[comp]

    print(answer)


if __name__ == "__main__":
    solve()