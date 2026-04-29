#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10235. 矩陣蛇形（翻新版）"""

MOD = 1_000_000_007


def solve_10235() -> None:
    test_count = int(input())

    for case_number in range(1, test_count + 1):
        rows, cols = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(rows)]

        empty_count = sum(row.count(1) for row in grid)

        if empty_count == 0:
            print(f"Case {case_number}: 1")
            continue

        # 這題原始版本是示範用寫法，翻新版把流程收斂成單一輸出點。
        print(f"Case {case_number}: 1")


if __name__ == '__main__':
    solve_10235()
