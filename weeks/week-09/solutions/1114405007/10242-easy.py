import sys
from collections import deque


def build_scc(graph, reverse_graph, money, is_bar):
    n = len(graph) - 1
    visited = [0] * (n + 1)
    order = []

    # 第一次走原圖，拿完成順序。
    for start in range(1, n + 1):
        if visited[start]:
            continue

        stack = [(start, 0)]
        visited[start] = 1

        while stack:
            x, idx = stack[-1]
            if idx < len(graph[x]):
                y = graph[x][idx]
                stack[-1] = (x, idx + 1)
                if not visited[y]:
                    visited[y] = 1
                    stack.append((y, 0))
            else:
                order.append(x)
                stack.pop()

    comp_id = [-1] * (n + 1)
    comp_money = []
    comp_bar = []
    comp_cnt = 0

    # 第二次走反向圖，找 SCC。
    for start in reversed(order):
        if comp_id[start] != -1:
            continue

        stack = [start]
        comp_id[start] = comp_cnt
        total = 0
        has_bar = 0

        while stack:
            x = stack.pop()
            total += money[x]
            has_bar |= is_bar[x]

            for y in reverse_graph[x]:
                if comp_id[y] == -1:
                    comp_id[y] = comp_cnt
                    stack.append(y)

        comp_money.append(total)
        comp_bar.append(has_bar)
        comp_cnt += 1

    return comp_id, comp_money, comp_bar, comp_cnt


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        reverse_graph[b].append(a)

    money = [0] * (n + 1)
    for i in range(1, n + 1):
        money[i] = int(input())

    start, p = map(int, input().split())
    bars = []
    while len(bars) < p:
        bars += list(map(int, input().split()))

    is_bar = [0] * (n + 1)
    for x in bars:
        is_bar[x] = 1

    comp_id, comp_money, comp_bar, comp_cnt = build_scc(graph, reverse_graph, money, is_bar)

    # 縮點成 DAG。
    dag = [set() for _ in range(comp_cnt)]
    for x in range(1, n + 1):
        a = comp_id[x]
        for y in graph[x]:
            b = comp_id[y]
            if a != b:
                dag[a].add(b)

    start = comp_id[start]

    # 只留下從起點可以走到的點。
    reachable = [0] * comp_cnt
    stack = [start]
    reachable[start] = 1
    while stack:
        x = stack.pop()
        for y in dag[x]:
            if not reachable[y]:
                reachable[y] = 1
                stack.append(y)

    indegree = [0] * comp_cnt
    for x in range(comp_cnt):
        if not reachable[x]:
            continue
        for y in dag[x]:
            if reachable[y]:
                indegree[y] += 1

    queue = deque()
    for i in range(comp_cnt):
        if reachable[i] and indegree[i] == 0:
            queue.append(i)

    dp = [-1] * comp_cnt
    dp[start] = comp_money[start]
    ans = 0

    # 在 DAG 上做 DP，求最大可搶金額。
    while queue:
        x = queue.popleft()

        if comp_bar[x] and dp[x] > ans:
            ans = dp[x]

        for y in dag[x]:
            if reachable[y] and dp[x] != -1:
                dp[y] = max(dp[y], dp[x] + comp_money[y])

            if reachable[y]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    queue.append(y)

    print(ans)


if __name__ == "__main__":
    main()