#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve_10226():
    while True:
        n = int(input())
        if n == 0:
            break

        forbidden = [set() for _ in range(n)]
        for i in range(n):
            while True:
                pos = int(input())
                if pos == 0:
                    break
                forbidden[i].add(pos - 1)

        perms = []

        def backtrack(used, current):
            if len(current) == n:
                perms.append(current[:])
                return

            pos = len(current)
            for person in range(n):
                if used[person] or pos in forbidden[person]:
                    continue

                used[person] = True
                current.append(person)
                backtrack(used, current)
                current.pop()
                used[person] = False

        backtrack([False] * n, [])
        perms.sort()

        prev = []
        for perm in perms:
            i = 0
            while i < len(prev) and i < len(perm) and prev[i] == perm[i]:
                i += 1

            output = ' '.join(chr(ord('A') + p) for p in perm[i:])
            print(output)
            prev = perm


if __name__ == '__main__':
    solve_10226()
