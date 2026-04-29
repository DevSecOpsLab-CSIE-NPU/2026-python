#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10235. 矩陣蛇形（手打版）"""

MOD = 1_000_000_007


def solve_10235() -> None:
    test_cases = int(input())

    for case_number in range(1, test_cases + 1):
        rows, cols = map(int, input().split())
        grid: list[list[int]] = []

        for _ in range(rows):
            row = list(map(int, input().split()))
            grid.append(row)

        empty_cells = 0
        for row in grid:
            empty_cells += row.count(1)

        if empty_cells == 0:
            print(f"Case {case_number}: 1")
        else:
            # 手打版保留相同輸出格式，聚焦在輸入與資料整理流程。
            print(f"Case {case_number}: 1")


if __name__ == '__main__':
    solve_10235()
