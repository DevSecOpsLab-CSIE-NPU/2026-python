import sys
from collections import deque

"""
優化說明：
- 將 SCC、DAG 建構、可達性與 DP 拆成清楚且可重用的函式。
- DP 只處理從起點可達的元件，避免不必要計算。
- 圖遍歷採疊代寫法，降低遞迴深度風險。
"""


def kosaraju(graph, reverse_graph, money, bars):
    node_count = len(graph) - 1
    visited = [False] * (node_count + 1)
    finish_order = []

    for start in range(1, node_count + 1):
        if visited[start]:
            continue

        stack = [(start, 0)]
        visited[start] = True

        while stack:
            node, edge_index = stack[-1]
            if edge_index < len(graph[node]):
                neighbor = graph[node][edge_index]
                stack[-1] = (node, edge_index + 1)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, 0))
            else:
                finish_order.append(node)
                stack.pop()

    component_id = [-1] * (node_count + 1)
    component_money = []
    component_has_bar = []

    for start in reversed(finish_order):
        if component_id[start] != -1:
            continue

        total_money = 0
        has_bar = False
        current_component = len(component_money)
        stack = [start]
        component_id[start] = current_component

        while stack:
            node = stack.pop()
            total_money += money[node]
            has_bar |= bars[node]
            for neighbor in reverse_graph[node]:
                if component_id[neighbor] == -1:
                    component_id[neighbor] = current_component
                    stack.append(neighbor)

        component_money.append(total_money)
        component_has_bar.append(has_bar)

    return component_id, component_money, component_has_bar


def build_condensed_graph(graph, component_id, component_count):
    dag = [set() for _ in range(component_count)]
    for node in range(1, len(graph)):
        source_component = component_id[node]
        for neighbor in graph[node]:
            target_component = component_id[neighbor]
            if source_component != target_component:
                dag[source_component].add(target_component)
    return dag


def reachable_components(dag, start):
    reachable = [False] * len(dag)
    stack = [start]
    reachable[start] = True

    while stack:
        component = stack.pop()
        for neighbor in dag[component]:
            if not reachable[neighbor]:
                reachable[neighbor] = True
                stack.append(neighbor)

    return reachable


def best_loot(graph, reverse_graph, money, start, bars):
    component_id, component_money, component_has_bar = kosaraju(graph, reverse_graph, money, bars)
    dag = build_condensed_graph(graph, component_id, len(component_money))
    start_component = component_id[start]
    reachable = reachable_components(dag, start_component)

    indegree = [0] * len(dag)
    for component, neighbors in enumerate(dag):
        if not reachable[component]:
            continue
        for neighbor in neighbors:
            if reachable[neighbor]:
                indegree[neighbor] += 1

    queue = deque(
        component for component in range(len(dag)) if reachable[component] and indegree[component] == 0
    )

    dp = [-1] * len(dag)
    dp[start_component] = component_money[start_component]
    answer = 0

    while queue:
        component = queue.popleft()
        if component_has_bar[component] and dp[component] > answer:
            answer = dp[component]

        for neighbor in dag[component]:
            if reachable[neighbor] and dp[component] != -1:
                dp[neighbor] = max(dp[neighbor], dp[component] + component_money[neighbor])
            if reachable[neighbor]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

    return answer


def solve(reader):
    node_count, edge_count = map(int, reader.readline().split())
    graph = [[] for _ in range(node_count + 1)]
    reverse_graph = [[] for _ in range(node_count + 1)]

    for _ in range(edge_count):
        start, end = map(int, reader.readline().split())
        graph[start].append(end)
        reverse_graph[end].append(start)

    money = [0] * (node_count + 1)
    for node in range(1, node_count + 1):
        money[node] = int(reader.readline())

    start, bar_count = map(int, reader.readline().split())
    bar_nodes = []
    while len(bar_nodes) < bar_count:
        bar_nodes.extend(map(int, reader.readline().split()))

    bars = [False] * (node_count + 1)
    for node in bar_nodes:
        bars[node] = True

    return str(best_loot(graph, reverse_graph, money, start, bars))


def main():
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    main()