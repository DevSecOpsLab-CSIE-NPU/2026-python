#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict, deque

def solve_10242():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)

    atm_values = [int(input()) for _ in range(n)]

    start, p = map(int, input().split())
    start -= 1
    bars = set(int(x) - 1 for x in input().split())

    max_money = 0
    visited = set()
    queue = deque([(start, frozenset([start]))])
    visited.add((start, frozenset([start])))

    while queue:
        node, robbed = queue.popleft()

        if node in bars:
            max_money = max(max_money, sum(atm_values[x] for x in robbed))

        for next_node in graph[node]:
            new_robbed = robbed | frozenset([next_node])
            state = (next_node, new_robbed)

            if state not in visited and len(visited) < 10000:
                visited.add(state)
                queue.append(state)

    return max_money


if __name__ == '__main__':
    result = solve_10242()
    print(result)
