#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10252. 費馬點（翻新版）"""

import math


def score(point: tuple[int, int], points: list[tuple[int, int]]) -> float:
    x, y = point
    return sum(math.hypot(x - px, y - py) for px, py in points)


def solve_10252() -> None:
    test_count = int(input())

    for _ in range(test_count):
        point_count = int(input())
        points = [tuple(map(int, input().split())) for _ in range(point_count)]

        if point_count == 1:
            print("0 1")
            continue

        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        best_x = round(sum(xs) / len(xs))
        best_y = round(sum(ys) / len(ys))

        current = (best_x, best_y)
        current_score = score(current, points)

        while True:
            improved = False
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    candidate = (current[0] + dx, current[1] + dy)
                    candidate_score = score(candidate, points)
                    if candidate_score + 1e-9 < current_score:
                        current = candidate
                        current_score = candidate_score
                        improved = True
            if not improved:
                break

        plateau = [current]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                candidate = (current[0] + dx, current[1] + dy)
                if abs(score(candidate, points) - current_score) < 1e-9:
                    plateau.append(candidate)

        unique_count = len(set(plateau))
        print(f"{int(round(current_score))} {unique_count}")


if __name__ == '__main__':
    solve_10252()
