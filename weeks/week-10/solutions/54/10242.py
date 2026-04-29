#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10242. ATM 搶劫（翻新版）"""

from collections import defaultdict, deque


def solve_10242() -> int:
    nodes, edges = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(edges):
        start, end = map(int, input().split())
        graph[start - 1].append(end - 1)

    atm_values = [int(input()) for _ in range(nodes)]

    start, bar_count = map(int, input().split())
    start -= 1
    bars = {int(x) - 1 for x in input().split()}

    best = 0
    visited = {(start, frozenset([start]))}
    queue = deque([(start, frozenset([start]))])

    while queue:
        node, robbed = queue.popleft()

        if node in bars:
            total = sum(atm_values[index] for index in robbed)
            if total > best:
                best = total

        for next_node in graph[node]:
            next_robbed = robbed | frozenset([next_node])
            state = (next_node, next_robbed)
            if state not in visited and len(visited) < 10_000:
                visited.add(state)
                queue.append(state)

    return best


if __name__ == '__main__':
    print(solve_10242())
