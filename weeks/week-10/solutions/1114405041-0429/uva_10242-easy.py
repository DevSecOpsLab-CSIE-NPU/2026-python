from __future__ import annotations

from collections import deque
import sys


def build_scc(
    graph: list[list[int]],
    reverse_graph: list[list[int]],
    cash: list[int],
    bars: list[bool],
) -> tuple[list[int], list[int], list[bool]]:
    node_count = len(graph) - 1
    visited = [False] * (node_count + 1)
    finish_order: list[int] = []

    for start in range(1, node_count + 1):
        if visited[start]:
            continue
        stack: list[tuple[int, int]] = [(start, 0)]
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

    component_of = [-1] * (node_count + 1)
    component_cash: list[int] = []
    component_has_bar: list[bool] = []

    for start in reversed(finish_order):
        if component_of[start] != -1:
            continue
        component_id = len(component_cash)
        component_cash.append(0)
        component_has_bar.append(False)
        stack = [start]
        component_of[start] = component_id

        while stack:
            node = stack.pop()
            component_cash[component_id] += cash[node]
            component_has_bar[component_id] = component_has_bar[component_id] or bars[node]
            for neighbor in reverse_graph[node]:
                if component_of[neighbor] == -1:
                    component_of[neighbor] = component_id
                    stack.append(neighbor)

    return component_of, component_cash, component_has_bar


def solve(data: str) -> str:
    values = [int(token) for token in data.split()]
    if not values:
        return ""

    iterator = iter(values)
    node_count = next(iterator)
    edge_count = next(iterator)

    graph = [[] for _ in range(node_count + 1)]
    reverse_graph = [[] for _ in range(node_count + 1)]
    for _ in range(edge_count):
        start = next(iterator)
        end = next(iterator)
        graph[start].append(end)
        reverse_graph[end].append(start)

    cash = [0] * (node_count + 1)
    for node in range(1, node_count + 1):
        cash[node] = next(iterator)

    start_node = next(iterator)
    bar_count = next(iterator)
    bars = [False] * (node_count + 1)
    for _ in range(bar_count):
        bars[next(iterator)] = True

    component_of, component_cash, component_has_bar = build_scc(graph, reverse_graph, cash, bars)
    component_count = len(component_cash)
    dag = [set() for _ in range(component_count)]

    for node in range(1, node_count + 1):
        start_component = component_of[node]
        for neighbor in graph[node]:
            end_component = component_of[neighbor]
            if start_component != end_component:
                dag[start_component].add(end_component)

    start_component = component_of[start_node]
    reachable = [False] * component_count
    stack = [start_component]
    reachable[start_component] = True
    while stack:
        component = stack.pop()
        for neighbor in dag[component]:
            if not reachable[neighbor]:
                reachable[neighbor] = True
                stack.append(neighbor)

    indegree = [0] * component_count
    for component in range(component_count):
        if not reachable[component]:
            continue
        for neighbor in dag[component]:
            if reachable[neighbor]:
                indegree[neighbor] += 1

    negative_inf = -10**18
    best_cash = [negative_inf] * component_count
    best_cash[start_component] = component_cash[start_component]
    queue = deque(
        component
        for component in range(component_count)
        if reachable[component] and indegree[component] == 0
    )

    while queue:
        component = queue.popleft()
        for neighbor in dag[component]:
            if not reachable[neighbor]:
                continue
            if best_cash[component] != negative_inf:
                candidate = best_cash[component] + component_cash[neighbor]
                if candidate > best_cash[neighbor]:
                    best_cash[neighbor] = candidate
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    answer = 0
    for component in range(component_count):
        if reachable[component] and component_has_bar[component]:
            answer = max(answer, best_cash[component])
    return str(answer)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()