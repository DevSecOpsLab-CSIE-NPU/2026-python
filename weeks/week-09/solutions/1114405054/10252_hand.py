#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def solve_10252():
    t = int(input())

    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))

        if n == 1:
            print(f"0 1")
            continue

        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        min_x, max_x = min(xs) - 1, max(xs) + 1
        min_y, max_y = min(ys) - 1, max(ys) + 1

        min_dist = float('inf')
        count = 0

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                dist = sum(math.sqrt((x - px) ** 2 + (y - py) ** 2)
                          for px, py in points)

                if dist < min_dist:
                    min_dist = dist
                    count = 1
                elif abs(dist - min_dist) < 1e-9:
                    count += 1

        print(f"{int(round(min_dist))} {count}")


if __name__ == '__main__':
    solve_10252()
