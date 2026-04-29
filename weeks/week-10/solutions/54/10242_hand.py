#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10242. ATM 搶劫（手打版）"""

from collections import defaultdict, deque


def solve_10242() -> int:
    nodes, edges = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(edges):
        start, end = map(int, input().split())
        graph[start - 1].append(end - 1)

    atm_values = []
    for _ in range(nodes):
        atm_values.append(int(input()))

    start, bar_count = map(int, input().split())
    start -= 1
    bars = set()
    for item in input().split():
        bars.add(int(item) - 1)

    best = 0
    queue = deque([(start, frozenset([start]))])
    visited = {(start, frozenset([start]))}

    while queue:
        node, robbed = queue.popleft()

        if node in bars:
            total = 0
            for index in robbed:
                total += atm_values[index]
            if total > best:
                best = total

        for next_node in graph[node]:
            next_robbed = robbed | frozenset([next_node])
            state = (next_node, next_robbed)
            if state in visited:
                continue
            if len(visited) >= 10_000:
                continue
            visited.add(state)
            queue.append(state)

    return best


if __name__ == '__main__':
    print(solve_10242())
