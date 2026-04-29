#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10226. 排列問題（手打版）"""


def read_forbidden_positions(count: int) -> list[set[int]]:
    forbidden = [set() for _ in range(count)]
    for person in range(count):
        while True:
            position = int(input())
            if position == 0:
                break
            forbidden[person].add(position - 1)
    return forbidden


def generate_permutations(count: int, forbidden: list[set[int]]) -> list[list[int]]:
    results: list[list[int]] = []
    used = [False] * count
    current: list[int] = []

    def dfs() -> None:
        if len(current) == count:
            results.append(current[:])
            return

        position = len(current)
        for person in range(count):
            if used[person]:
                continue
            if position in forbidden[person]:
                continue

            used[person] = True
            current.append(person)
            dfs()
            current.pop()
            used[person] = False

    dfs()
    results.sort()
    return results


def print_compacted(permutations: list[list[int]]) -> None:
    previous: list[int] = []
    for permutation in permutations:
        shared = 0
        while shared < len(previous) and shared < len(permutation) and previous[shared] == permutation[shared]:
            shared += 1

        names = [chr(ord('A') + person) for person in permutation[shared:]]
        print(' '.join(names))
        previous = permutation


def solve_10226() -> None:
    while True:
        count = int(input())
        if count == 0:
            break

        forbidden = read_forbidden_positions(count)
        permutations = generate_permutations(count, forbidden)
        print_compacted(permutations)


if __name__ == '__main__':
    solve_10226()
