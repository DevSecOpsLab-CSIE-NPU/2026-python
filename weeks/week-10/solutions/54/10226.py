#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10226. 排列問題（翻新版）"""


def solve_10226() -> None:
    while True:
        n = int(input())
        if n == 0:
            break

        forbidden = [set() for _ in range(n)]
        for person in range(n):
            while True:
                position = int(input())
                if position == 0:
                    break
                forbidden[person].add(position - 1)

        permutations = []

        def backtrack(used: list[bool], current: list[int]) -> None:
            if len(current) == n:
                permutations.append(current[:])
                return

            position = len(current)
            for person in range(n):
                if used[person] or position in forbidden[person]:
                    continue
                used[person] = True
                current.append(person)
                backtrack(used, current)
                current.pop()
                used[person] = False

        backtrack([False] * n, [])
        permutations.sort()

        previous: list[int] = []
        for permutation in permutations:
            prefix = 0
            while prefix < len(previous) and prefix < len(permutation) and previous[prefix] == permutation[prefix]:
                prefix += 1

            print(" ".join(chr(ord('A') + person) for person in permutation[prefix:]))
            previous = permutation


if __name__ == '__main__':
    solve_10226()
