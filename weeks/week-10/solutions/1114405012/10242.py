from __future__ import annotations

import sys
from collections import deque


def kosaraju(component_graph: list[list[int]]) -> list[int]:
    # 建反向圖，供第二次 DFS 使用。
    n = len(component_graph)
    reverse_graph = [[] for _ in range(n)]
    for node in range(n):
        for nxt in component_graph[node]:
            reverse_graph[nxt].append(node)

    # 第一次 DFS：取得完成時間序。
    order: list[int] = []
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        stack = [(start, 0)]
        visited[start] = True
        while stack:
            node, index = stack[-1]
            if index < len(component_graph[node]):
                nxt = component_graph[node][index]
                stack[-1] = (node, index + 1)
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
                stack.pop()

    # 第二次 DFS：按照反向完成序切出 SCC 編號。
    component_id = [-1] * n
    current_component = 0
    for start in reversed(order):
        if component_id[start] != -1:
            continue
        queue = [start]
        component_id[start] = current_component
        for node in queue:
            for nxt in reverse_graph[node]:
                if component_id[nxt] == -1:
                    component_id[nxt] = current_component
                    queue.append(nxt)
        current_component += 1

    return component_id


def solve_case(node_count: int, edges: list[tuple[int, int]], values: list[int], start: int, bars: list[int]) -> int:
    # 原圖建好後先做 SCC 壓縮。
    graph = [[] for _ in range(node_count)]
    for source, target in edges:
        graph[source].append(target)

    component_id = kosaraju(graph)
    component_count = max(component_id) + 1

    # 同一個 SCC 內可互通，等價於可以把該 SCC 金額一次拿完。
    component_value = [0] * component_count
    for node, value in enumerate(values):
        component_value[component_id[node]] += value

    # 建凝縮 DAG，後續做最大路徑 DP。
    condensed = [[] for _ in range(component_count)]
    indegree = [0] * component_count
    for source, target in edges:
        left = component_id[source]
        right = component_id[target]
        if left != right:
            condensed[left].append(right)
            indegree[right] += 1

    start_component = component_id[start]
    bar_components = {component_id[bar] for bar in bars}

    # DAG 拓樸排序。
    queue = deque(node for node in range(component_count) if indegree[node] == 0)
    topo: list[int] = []
    while queue:
        node = queue.popleft()
        topo.append(node)
        for nxt in condensed[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    # 從起點 SCC 出發，做可達路徑的最大累積金額。
    negative_infinity = -10**30
    best = [negative_infinity] * component_count
    best[start_component] = component_value[start_component]

    for node in topo:
        if best[node] == negative_infinity:
            continue
        for nxt in condensed[node]:
            candidate = best[node] + component_value[nxt]
            if candidate > best[nxt]:
                best[nxt] = candidate

    return max(best[component] for component in bar_components)


def main() -> None:
    # 題目只有一筆圖資料，這裡保留 while 是為了統一 token 讀法。
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return

    index = 0
    outputs: list[str] = []
    while index < len(tokens):
        node_count = tokens[index]
        index += 1
        edge_count = tokens[index]
        index += 1
        edges = []
        for _ in range(edge_count):
            source = tokens[index] - 1
            target = tokens[index + 1] - 1
            index += 2
            edges.append((source, target))
        values = tokens[index:index + node_count]
        index += node_count
        start = tokens[index] - 1
        bar_count = tokens[index + 1]
        index += 2
        bars = [tokens[index + offset] - 1 for offset in range(bar_count)]
        index += bar_count
        outputs.append(str(solve_case(node_count, edges, values, start, bars)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()