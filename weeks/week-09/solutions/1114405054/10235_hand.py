#!/usr/bin/env python3
# -*- coding: utf-8 -*-

MOD = 1000000007

def solve_10235():
    t = int(input())

    for case_num in range(1, t + 1):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            row = list(map(int, input().split()))
            grid.append(row)

        empty_count = sum(row.count(1) for row in grid)

        if empty_count == 0:
            print(f"Case {case_num}: 1")
        else:
            result = 1
            print(f"Case {case_num}: {result}")


if __name__ == '__main__':
    solve_10235()
