#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10252. 費馬點（手打版）"""

import math


def total_distance(point: tuple[int, int], points: list[tuple[int, int]]) -> float:
    x, y = point
    total = 0.0
    for px, py in points:
        total += math.hypot(x - px, y - py)
    return total


def solve_10252() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        point_count = int(input())
        points: list[tuple[int, int]] = []
        for _ in range(point_count):
            x, y = map(int, input().split())
            points.append((x, y))

        if point_count == 1:
            print("0 1")
            continue

        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        min_x = min(xs) - 1
        max_x = max(xs) + 1
        min_y = min(ys) - 1
        max_y = max(ys) + 1

        best_distance = float('inf')
        best_count = 0

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                current_distance = total_distance((x, y), points)
                if current_distance < best_distance:
                    best_distance = current_distance
                    best_count = 1
                elif abs(current_distance - best_distance) < 1e-9:
                    best_count += 1

        print(f"{int(round(best_distance))} {best_count}")


if __name__ == '__main__':
    solve_10252()
