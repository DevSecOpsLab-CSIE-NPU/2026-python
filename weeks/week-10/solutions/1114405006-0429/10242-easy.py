"""UVA 10242 / ZeroJudge a235：ATM 搶掠計畫的簡單版。

這份程式用比較直白的方式寫：
先做 SCC，再把 SCC 縮成 DAG，最後在 DAG 上找可達酒吧的最大金額。
"""

from __future__ import annotations

from collections import deque
import sys


class FastScanner:
    """逐一讀取整數，避免一次 split 造成太多記憶體使用。"""

    def __init__(self, data: bytes) -> None:
        self.data = data
        self.index = 0
        self.length = len(data)

    def next_int(self) -> int | None:
        while self.index < self.length and self.data[self.index] <= 32:
            self.index += 1

        if self.index >= self.length:
            return None

        number = 0
        while self.index < self.length and self.data[self.index] > 32:
            number = number * 10 + (self.data[self.index] - 48)
            self.index += 1
        return number


def build_scc(
    graph: list[list[int]], reverse_graph: list[list[int]], weights: list[int]
) -> tuple[list[int], list[int]]:
    """回傳每個點的 SCC 編號，以及每個 SCC 的權重總和。"""

    node_count = len(graph)

    visited = [False] * node_count
    order: list[int] = []
    for start in range(node_count):
        if visited[start]:
            continue

        stack = [(start, 0)]
        visited[start] = True
        while stack:
            node, next_index = stack[-1]
            if next_index < len(graph[node]):
                neighbor = graph[node][next_index]
                stack[-1] = (node, next_index + 1)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, 0))
            else:
                order.append(node)
                stack.pop()

    component_id = [-1] * node_count
    component_sum: list[int] = []
    for start in reversed(order):
        if component_id[start] != -1:
            continue

        current_component = len(component_sum)
        stack = [start]
        component_id[start] = current_component
        total = 0
        while stack:
            node = stack.pop()
            total += weights[node]
            for neighbor in reverse_graph[node]:
                if component_id[neighbor] == -1:
                    component_id[neighbor] = current_component
                    stack.append(neighbor)
        component_sum.append(total)

    return component_id, component_sum


def solve(data: bytes) -> str:
    """直接回傳答案字串。"""

    scanner = FastScanner(data)
    node_count = scanner.next_int()
    if node_count is None:
        return ""

    edge_count = scanner.next_int()

    graph = [[] for _ in range(node_count)]
    reverse_graph = [[] for _ in range(node_count)]

    for _ in range(edge_count):
        start = scanner.next_int() - 1
        end = scanner.next_int() - 1
        graph[start].append(end)
        reverse_graph[end].append(start)

    # 每個路口的 ATM 金額。
    weights = [scanner.next_int() for _ in range(node_count)]

    start_node = scanner.next_int() - 1
    bar_count = scanner.next_int()
    bar_nodes = [scanner.next_int() - 1 for _ in range(bar_count)]

    component_id, component_sum = build_scc(graph, reverse_graph, weights)

    component_count = len(component_sum)
    start_component = component_id[start_node]
    is_bar_component = [False] * component_count
    for bar in bar_nodes:
        is_bar_component[component_id[bar]] = True

    # 把 SCC 縮成 DAG，先用 set 去重以避免重複邊（減少 indegree/重複遍歷）。
    condensed_sets = [set() for _ in range(component_count)]
    for node in range(node_count):
        source_component = component_id[node]
        for neighbor in graph[node]:
            target_component = component_id[neighbor]
            if source_component != target_component:
                condensed_sets[source_component].add(target_component)

    condensed_graph = [list(s) for s in condensed_sets]
    indegree = [0] * component_count
    for u, neighs in enumerate(condensed_graph):
        for v in neighs:
            indegree[v] += 1

    # 在 DAG 上做最長路徑 DP。
    dp = [-1] * component_count
    dp[start_component] = component_sum[start_component]

    queue = deque(i for i in range(component_count) if indegree[i] == 0)
    while queue:
        component = queue.popleft()
        # 合併兩個迴圈：若當前有可達值就傳遞給鄰居，同時減少鄰居 indegree
        neighbors = condensed_graph[component]
        val = dp[component]
        for neighbor in neighbors:
            if val != -1:
                candidate = val + component_sum[neighbor]
                if candidate > dp[neighbor]:
                    dp[neighbor] = candidate
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    answer = 0
    for component in range(component_count):
        if is_bar_component[component] and dp[component] > answer:
            answer = dp[component]

    return str(answer)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.buffer.read()))


if __name__ == "__main__":
    main()